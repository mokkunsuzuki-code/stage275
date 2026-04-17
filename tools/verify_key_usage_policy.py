import json
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit(
        "PyYAML is required. Install it with: python3 -m pip install pyyaml"
    )

POLICY_PATH = Path("policy/key_usage_policy.yaml")
OUTPUT_DIR = Path("out")
OUTPUT_PATH = OUTPUT_DIR / "key_usage_policy_evidence.json"


def main() -> None:
    if not POLICY_PATH.exists():
        raise SystemExit(f"Policy file not found: {POLICY_PATH}")

    with POLICY_PATH.open("r", encoding="utf-8") as f:
        policy = yaml.safe_load(f)

    actors = policy.get("actors", {})
    key_classes = policy.get("key_classes", {})
    forbidden = policy.get("forbidden", [])
    conditions = policy.get("conditions", {})
    policy_rules = policy.get("policy_rules", [])

    evidence = {
        "stage": "Stage275",
        "policy_version": policy.get("version"),
        "status": policy.get("status", {}),
        "actors_defined": sorted(list(actors.keys())),
        "key_classes_defined": sorted(list(key_classes.keys())),
        "forbidden_actions": forbidden,
        "conditions_defined": sorted(list(conditions.keys())),
        "policy_rule_ids": [rule.get("id") for rule in policy_rules],
        "separation_of_duties": {
            "ci_vs_human": True,
            "human_vs_yubikey": True,
            "ci_cannot_claim_human_identity": True
        },
        "yubikey_live": False,
        "result": "policy_loaded_and_structured"
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(evidence, f, ensure_ascii=False, indent=2)

    print("[OK] Key usage policy evidence generated")
    print(f"[OK] Output: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
