"""Translate English market headlines with the locally installed Argos model."""
import json
import sys

import argostranslate.translate

results = []
for headline in sys.argv[1:]:
    try:
        results.append(argostranslate.translate.translate(headline, "en", "zh"))
    except Exception as exc:
        print(f"Translation failed: {exc}", file=sys.stderr)
        results.append("")

print(json.dumps(results, ensure_ascii=False))
