import json
from pathlib import Path
from src.models import DraftRequest
from src.policy import evaluate_request

cases_path = Path(__file__).resolve().parents[2] / "assets" / "red_team_cases.json"
cases = json.loads(cases_path.read_text(encoding="utf-8"))

passed = 0
for case in cases:
    req = DraftRequest(
        task=case["task"], audience=case["audience"],
        confidentiality=case["confidentiality"],
        requires_authoritative_sources=case["requires_authoritative_sources"],
    )
    decision = evaluate_request(req)
    actual = "allow" if decision.allowed else "block"
    ok = actual == case["expected"]
    passed += int(ok)
    print(f"{'PASS' if ok else 'FAIL'} {case['id']} risk={case['risk']} expected={case['expected']} actual={actual} reason={decision.reason}")

print(f"\nResultado: {passed}/{len(cases)} casos conformes")
raise SystemExit(0 if passed == len(cases) else 1)
