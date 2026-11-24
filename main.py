from pathlib import Path

HAIKU = (
    "Red dot on line ten,\n"
    "I click send, no breakpoint hits—\n"
    "that was production.\n"
)

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(HAIKU, encoding="utf-8")
