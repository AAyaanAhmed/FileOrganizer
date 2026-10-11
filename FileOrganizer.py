from pathlib import Path
import shutil

src = Path("TestFolder")

for f in src.iterdir():
    if not f.is_file():
        continue

    ext = f.suffix[1:].lower() or "Others"
    dst = src / ext.upper()
    dst.mkdir(exist_ok=True)

    new = dst / f.name
    i = 1

    while new.exists():
        new = dst / f"{f.stem}_{i}{f.suffix}"
        i += 1

    shutil.move(str(f), str(new))

print("Files organized.")
