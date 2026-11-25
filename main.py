"""Snooze button roast entry writer — validates the gate and writes /output/entry.txt."""
import os

LINE = "Alarm at 6 AM on Saturday: congrats, you are not punctual, you are just a tiny terrorist with a snooze button."
MIN_CHARS = 1
MAX_CHARS = 200

def main():
    assert LINE.strip(), "entry line must be non-blank"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert MIN_CHARS <= len(LINE) <= MAX_CHARS, "entry length out of gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))
    print(len(LINE))

if __name__ == "__main__":
    main()
