import json
from pathlib import Path
from src.tools import load_incidents, get_incident_record, duration_minutes

def test_incident_lookup_is_read_only_data():
    incidents = load_incidents(Path("data/incidents.json"))
    inc = get_incident_record(incidents,"INC-2048")
    assert inc["status"] == "RESOLVED"

def test_incident_duration():
    assert duration_minutes(
        "2026-09-29T08:00:00Z",
        "2026-09-29T09:12:00Z",
    ) == 72
