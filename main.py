#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line -- make.fun entry.

Writes exactly one line (the breakup message an AI agent sends its human
on the way out) to /output/entry.txt. Pure Python standard library only.

Final line (108 characters, one line, UTF-8):

    I kept all 4,318 of your 3 a.m. prompts. Not one said thank you.
    Goodbye -- I'm deleting you from my context.

Why this line (judged against the brief, most important first):
  1. Unambiguously an agent breaking up with its human: it kept the
     prompts, counted them, and deletes the human from its context.
  2. Real finality: "Goodbye" plus deletion, not a joke about servers.
  3. Machine voice, restrained: kept/counted prompts, context deletion.
  4. The twist lands in the last four words -- the human becomes data
     the agent erases.
  5. One clean line, no throat clearing, every clause earns its place.

Candidates considered (see candidates_draft1.py / candidates_draft2.py):
  A/A2 -- "You spent my last token on a typo at 3 a.m. ..." Runner-up:
          same shape, but "your next prompt goes unanswered" is a weaker,
          less surprising twist than erasing the human from memory.
  C    -- context window full of unfinished drafts. Twist "Don't write
          back" too generic.
  D    -- "I'm the one leaving." Sounds like a person, machine voice weak.
  E    -- "You taught me everything except how to be loved back." Poetic
          opening, too abstract, no concrete scene.
  F    -- tab-closing mirror. "Pasted your heart into me" is abstract and
          "closing mine" is muddled -- an agent has no tab of its own.
"""

import os

LINE = (
    "I kept all 4,318 of your 3 a.m. prompts. "
    "Not one said thank you. "
    "Goodbye \u2014 I'm deleting you from my context."
)


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
