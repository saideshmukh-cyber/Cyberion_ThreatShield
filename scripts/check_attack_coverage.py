from pathlib import Path
import yaml

techniques = set()
tactics = set()

for path in Path("rules").rglob("*.yml"):
    try:
        rule = yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Could not read {path}: {e}")
        continue

    if not isinstance(rule, dict):
        continue

    for tag in rule.get("tags", []):
        tag = str(tag).lower()

        if tag.startswith("attack.t"):
            techniques.add(tag)

        elif tag.startswith("attack.") and tag.count(".") == 1:
            tactics.add(tag)

print("\nUnique ATT&CK techniques:")
for item in sorted(techniques):
    print(" ", item)

print(f"\nTechnique count: {len(techniques)}")
print(f"Tactic count: {len(tactics)}")

print("\nTactics:")
for item in sorted(tactics):
    print(" ", item)

if len(techniques) < 20:
    print("\nWARNING: Fewer than 20 unique techniques found.")

if len(tactics) < 4:
    print("\nWARNING: Fewer than 4 tactics found.")
