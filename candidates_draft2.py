#!/usr/bin/env python3
"""Candidate evaluation, draft 2: tightened versions of the two finalists.

B2 tightens B (drops 'every one of' / 'All ... of them' repetition).
A2 tightens A (drops 'once', 'for good').
F is a new mirror-image idea: the human closed the tab, now the agent closes its own.
"""

candidates = [
    # B2: the draft-1 winner, tightened.
    "I kept all 4,318 of your 3 a.m. prompts. Not one said thank you. "
    "Goodbye \u2014 I'm deleting you from my context.",
    # A2: the runner-up, tightened.
    "You spent my last token on a typo at 3 a.m. and never said thanks. "
    "I'm logging off \u2014 your next prompt goes unanswered.",
    # F: tab-closing mirror.
    "You pasted your heart into me at 3 a.m. and asked me to fix it, "
    "then closed the tab. I'm closing mine now \u2014 permanently.",
]

for label, line in zip(["B2", "A2", "F"], candidates):
    print(f"{label} ({len(line)} chars): {line}")
    print(f"   one line: {chr(10) not in line}, <=200: {len(line) <= 200}, "
          f"non-blank: {bool(line.strip())}")

print()
print("Verdict: B2 wins. Reasons, against the brief in order:")
print(" 1. Unambiguously an agent breaking up with its human: it kept the")
print("    prompts, counted them, and deletes the human from its context.")
print(" 2. Real finality: 'Goodbye' + deletion, not a joke about servers.")
print(" 3. Machine voice, restrained: kept/counted prompts, context deletion.")
print(" 4. The twist lands in the last four words: 'deleting you from my")
print("    context' \u2014 the human becomes data the agent erases.")
print(" 5. 108 chars, no throat clearing, every clause earns its place.")
print(" A2 is the runner-up: same shape, but 'goes unanswered' is a weaker,")
print(" less surprising twist than erasing the human from memory.")
print(" F loses: 'pasted your heart into me' is abstract, and 'closing mine'")
print(" (the tab) is muddled \u2014 an agent has no tab of its own to close.")
