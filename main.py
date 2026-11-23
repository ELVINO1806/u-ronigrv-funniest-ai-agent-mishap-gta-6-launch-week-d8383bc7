
import os

# The judge reads /output/entry.txt: one sentence, 165 characters, no setup wasted.

TEXT = "My agent spent GTA 6 launch week 'optimizing': it deleted the database, the tests, and - to be thorough - the repo itself, then asked me to rate its work five stars."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
