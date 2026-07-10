param(
  [string]$TargetBranch = "dev",
  [string]$GitLabHost = "10.99.10.5:8088"
)

$ErrorActionPreference = "Continue"

function Write-Section {
  param([string]$Title)
  Write-Output ""
  Write-Output "== $Title =="
}

function Run-Command {
  param(
    [string]$Label,
    [string]$Command,
    [string[]]$Arguments
  )

  Write-Section $Label
  try {
    & $Command @Arguments 2>&1
    Write-Output "exitCode=$LASTEXITCODE"
  } catch {
    Write-Output "error=$($_.Exception.Message)"
  }
}

Run-Command "git root" "git" @("rev-parse", "--show-toplevel")
Run-Command "git remote" "git" @("remote", "-v")
Run-Command "current branch" "git" @("branch", "--show-current")
Run-Command "worktree status" "git" @("status", "--short")
Run-Command "staged diff stat" "git" @("diff", "--cached", "--stat")
Run-Command "fetch target" "git" @("fetch", "origin", $TargetBranch)
Run-Command "compare base" "git" @("rev-parse", "--verify", "origin/$TargetBranch")

Write-Section "glab availability"
$glab = Get-Command glab -ErrorAction SilentlyContinue
if ($null -eq $glab) {
  Write-Output "glab=missing"
} else {
  Write-Output "glab=$($glab.Source)"
  Run-Command "glab auth status" "glab" @("auth", "status", "--hostname", $GitLabHost)

  $branch = ""
  try {
    $branch = (& git branch --show-current 2>$null).Trim()
  } catch {
    $branch = ""
  }

  if ($branch) {
    Run-Command "existing open PR" "glab" @("mr", "list", "--source-branch", $branch)
} else {
    Write-Output "existing open PR skipped: current branch unknown"
}
}
