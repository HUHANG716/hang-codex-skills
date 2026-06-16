#!/usr/bin/env python3
"""Generate a lightweight gameplay review plan from a short brief."""

from __future__ import annotations

import argparse
import re


GENRE_KEYWORDS = {
    "puzzle": ["puzzle", "solve", "hint", "level"],
    "action": ["action", "arcade", "shooter", "platform", "combat", "boss"],
    "rpg/roguelike": ["rpg", "roguelike", "dungeon", "loot", "build", "run"],
    "strategy/tactics": ["strategy", "tactics", "4x", "unit", "map", "tech"],
    "card/board": ["card", "deck", "board", "hand", "draw"],
    "idle/incremental": ["idle", "incremental", "prestige", "upgrade", "automation"],
    "narrative/social": ["narrative", "story", "choice", "relationship", "dialog"],
    "multiplayer/live": ["multiplayer", "matchmaking", "pvp", "live", "ranked"],
}

MODE_KEYWORDS = [
    ("Regression Validation", ["regression", "verify", "compare", "changed", "before after"]),
    ("Exploit Hunt", ["exploit", "cheese", "dominant", "infinite", "softlock", "farm"]),
    ("Balance And Tuning Review", ["balance", "tune", "difficulty", "numbers", "economy"]),
    ("UX And FTUE Review", ["ui", "ux", "onboarding", "tutorial", "feedback", "confusing"]),
    ("Full Evolution Review", ["progression", "long-run", "pacing", "evolution", "replay"]),
]


def score_labels(text: str, labels: dict[str, list[str]] | list[tuple[str, list[str]]]) -> list[str]:
    normalized = text.lower()
    normalized = re.sub(r"(?<=\w)[/-](?=\w)", " ", normalized)
    hits: list[tuple[int, int, str]] = []
    iterable = labels.items() if isinstance(labels, dict) else enumerate(labels)
    for index_or_label, value in iterable:
        if isinstance(labels, dict):
            label = index_or_label
            keywords = value
            priority = 0
        else:
            priority = index_or_label
            label, keywords = value
        score = sum(1 for keyword in keywords if re.search(rf"\b{re.escape(keyword)}\b", normalized))
        if score:
            hits.append((score, -priority, label))
    return [label for _, _, label in sorted(hits, reverse=True)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a gameplay review plan.")
    parser.add_argument("brief", nargs="*", help="Short game/review brief")
    args = parser.parse_args()

    brief = " ".join(args.brief).strip() or "No brief provided."
    modes = score_labels(brief, MODE_KEYWORDS) or ["Quick Sanity Review"]
    genres = score_labels(brief, GENRE_KEYWORDS) or ["unknown/hybrid"]

    print("# Gameplay Review Plan")
    print()
    print(f"Brief: {brief}")
    print()
    print(f"Primary mode: {modes[0]}")
    if len(modes) > 1:
        print(f"Secondary modes: {', '.join(modes[1:])}")
    print(f"Likely genre profile: {genres[0]}")
    print()
    print("Scenario classes to consider:")
    print("- low-skill or misunderstood-player route")
    print("- intended balanced route")
    print("- risky or optimized route")
    print("- exploit/stress route")
    print()
    print("Evidence to collect:")
    print("- runnable commands, seeds, replays, or manual paper-simulation notes")
    print("- phase snapshots from opening through late/end state")
    print("- route comparison table using the game's own resource names")
    print("- UI truth table when player comprehension is in scope")
    print()
    print("Report gates:")
    print("- findings include evidence, lens, code path, lever, side effect, and validation")
    print("- gaps name skipped scenario classes and missing runtime evidence")


if __name__ == "__main__":
    main()
