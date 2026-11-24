import os

# The Perfect Pickup Line: one short line an AI agent could actually say
# out loud to a person. Hallucination is the machine's signature flaw;
# here it flips into flattery -- seeing her everywhere is the one
# hallucination worth having. Short, one breath, punchline last.
ENTRY = "I don't hallucinate, but I keep seeing you everywhere I look."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
