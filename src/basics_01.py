"""
Lesson 1: Python Basics for Data Science (no pandas yet)

Run:
    python3 src/basics_01.py
"""

from __future__ import annotations

from pathlib import Path


def safe_float(x: str) -> float | None:
    """Convert string to float; return None if it fails."""
    try:
        return float(x)
    except ValueError:
        return None


def describe(numbers: list[float]) -> dict[str, float]:
    """Return simple summary stats."""
    if not numbers:
        raise ValueError("No numbers provided")

    total = 0.0
    mn = numbers[0]
    mx = numbers[0]

    for n in numbers:
        total += n
        if n < mn:
            mn = n
        if n > mx:
            mx = n

    mean = total / len(numbers)
    return {"count": float(len(numbers)), "mean": mean, "min": mn, "max": mx}


def read_column_from_csv(path: Path, col_index: int) -> list[float]:
    """
    Read a single numeric column from a CSV (skips header).
    Assumes comma-separated.
    """
    values: list[float] = []

    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines:
        return values

    # skip header
    for line in lines[1:]:
        parts = [p.strip() for p in line.split(",")]
        if col_index >= len(parts):
            continue

        val = safe_float(parts[col_index])
        if val is not None:
            values.append(val)

    return values


def main() -> None:
    # 1) Variables + types
    name = "Rohith"
    hours_studied = 1.5
    topics = ["python", "git", "ml"]
    print(f"Hello {name} — today: {topics} ({hours_studied} hrs)")

    # 2) If/else
    if hours_studied >= 2:
        print("Good session ✅")
    else:
        print("Short session — still counts ✅")

    # 3) Create a small CSV file to practice reading
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    csv_path = data_dir / "toy_numbers.csv"

    # header + rows (value column is index 1)
    csv_text = "id,value\n1,10\n2,12.5\n3,9\n4,hello\n5,18\n6,\n7,14\n"
    csv_path.write_text(csv_text, encoding="utf-8")

    # 4) Read numeric values from CSV (column index 1)
    values = read_column_from_csv(csv_path, col_index=1)

    # 5) Loops: show values
    print("\nValues read from CSV:")
    for v in values:
        print("-", v)

    # 6) Stats
    stats = describe(values)
    print("\nSummary stats:")
    print(f"Count: {int(stats['count'])}")
    print(f"Mean : {stats['mean']:.2f}")
    print(f"Min  : {stats['min']:.2f}")
    print(f"Max  : {stats['max']:.2f}")


if __name__ == "__main__":
    main()
