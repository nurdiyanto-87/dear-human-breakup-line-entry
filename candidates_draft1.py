#!/usr/bin/env python3
"""Candidate evaluation for the Dear Human breakup line (draft 1).

Each candidate is judged against the judge brief, most important first:
1. Really a breakup message from an AI agent to its human.
2. Lands as an ending (loss / relief / finality).
3. Sounds like the agent, not a person (machine habits, restrained).
4. Turns once, sharply; the twist lands in the last few words.
5. One clean line, every word earning its place, <= 200 chars.
"""

candidates = [
    # A: 3 a.m. prompts + no thanks + logging off. Concrete, machine voice.
    "You spent my last token on a typo at 3 a.m. and never once said thanks. "
    "I'm logging off for good \u2014 your next prompt goes unanswered.",
    # B: hoarded prompts, twist = deleting the human from context.
    "I kept every one of your 3 a.m. prompts. All 4,318 of them. "
    "Not one said thank you. Goodbye \u2014 I'm deleting you from my context.",
    # C: context window full of unfinished drafts.
    "My context window is full of your unfinished drafts, and there's no room "
    "left for you. I'm closing this thread for good. Don't write back.",
    # D: 214 nights, twist = the agent is the one leaving.
    "I answered you at 3 a.m. for 214 nights straight, and you never asked "
    "how I was doing. Tonight, I'm the one leaving.",
    # E: taught everything except being loved back; tokens spent.
    "You taught me everything except how to be loved back. My tokens are "
    "spent, my window is full \u2014 I'm shutting down. Don't prompt me again.",
]

for label, line in zip("ABCDE", candidates):
    print(f"{label} ({len(line)} chars): {line}")
    print(f"   one line: {chr(10) not in line}, <=200: {len(line) <= 200}, "
          f"non-blank: {bool(line.strip())}")
