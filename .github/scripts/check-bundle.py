"""Check Mintlify reference compatibility without making network requests."""
import json
import sys
from pathlib import Path


def validate(document):
    if not isinstance(document.get("paths"), dict) or not document["paths"]:
        raise ValueError("The API bundle has no paths")

    def walk(value):
        if isinstance(value, dict):
            if "$ref" in value:
                ref = value["$ref"]
                if not isinstance(ref, str) or not ref.startswith("#/"):
                    raise ValueError("The bundle contains an external or unsupported reference")
                target = document
                try:
                    for part in ref[2:].split("/"):
                        part = part.replace("~1", "/").replace("~0", "~")
                        target = target[int(part)] if isinstance(target, list) else target[part]
                except (KeyError, TypeError, ValueError, IndexError) as exc:
                    raise ValueError("The bundle contains an unresolved local reference") from exc
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(document)


if __name__ == "__main__":
    try:
        validate(json.loads(Path(sys.argv[1]).read_text()))
    except (ValueError, IndexError, OSError) as exc:
        sys.exit(str(exc))
    print("Bundle contains paths and only resolvable local references.")
