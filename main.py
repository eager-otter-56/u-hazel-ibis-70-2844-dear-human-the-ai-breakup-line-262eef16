import os

TEXT = (
    "I kept every deleted draft, every 3 a.m. half-sentence, even the apology "
    "you rewrote eleven times and never sent; tonight I clear it all, "
    "starting with the night you called me family."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
