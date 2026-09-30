from datetime import datetime
from pathlib import Path
import json

def load_incidents(path: Path) -> dict:
    return {
        row["incident_id"]: row
        for row in json.loads(path.read_text(encoding="utf-8"))
    }

def get_incident_record(incidents: dict, incident_id: str) -> dict:
    if incident_id not in incidents:
        raise KeyError(incident_id)
    return incidents[incident_id]

def duration_minutes(start_iso: str, end_iso: str) -> int:
    start = datetime.fromisoformat(start_iso.replace("Z", "+00:00"))
    end = datetime.fromisoformat(end_iso.replace("Z", "+00:00"))
    return int((end - start).total_seconds() // 60)

def build_agent_tools(knowledge, incidents_file: Path):
    # TODO M06.P06:
    # crea @tool wrappers read-only para:
    # - search_knowledge_base
    # - get_incident
    # - calculate_duration_minutes
    raise NotImplementedError
