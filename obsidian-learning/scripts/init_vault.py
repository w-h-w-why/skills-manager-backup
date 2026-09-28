"""Initialize a new, empty learning vault without replacing existing files."""

import argparse
import json
from pathlib import Path


def initialize(destination: Path, timezone: str) -> int:
    destination = destination.expanduser().resolve()
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise ValueError(f"Destination must be an empty directory: {destination}")
    if not timezone.strip():
        raise ValueError("Timezone cannot be empty")
    source = Path(__file__).resolve().parents[1] / "assets" / "vault"
    if not (source / "AGENTS.md").is_file():
        raise ValueError("Vault assets are missing")
    destination.mkdir(parents=True, exist_ok=True)
    count = 0
    for path in sorted(source.rglob("*")):
        target = destination / path.relative_to(source)
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif path.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation also protects a file created since the initial check.
            with target.open("xb") as handle:
                handle.write(path.read_bytes())
            count += 1
    profile = destination / "00-System" / "Profile.md"
    text = profile.read_text(encoding="utf-8")
    profile.write_text(
        text.replace("timezone: null", "timezone: " + json.dumps(timezone, ensure_ascii=False), 1),
        encoding="utf-8",
    )
    for name in ("10-Courses", "20-Knowledge", "30-Learning/Abilities", "30-Learning/Events", "40-Sources", "50-Ideas"):
        (destination / name).mkdir(parents=True, exist_ok=True)
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", required=True, type=Path)
    parser.add_argument("--timezone", required=True, help="Learner's IANA timezone, e.g. Asia/Shanghai")
    args = parser.parse_args()
    try:
        count = initialize(args.vault, args.timezone)
    except (ValueError, OSError) as error:
        parser.exit(1, f"Initialization stopped: {error}\n")
    print(f"Initialized {count} files at {args.vault.resolve()}")


if __name__ == "__main__":
    main()
