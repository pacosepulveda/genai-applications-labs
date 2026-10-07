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
    from langchain.tools import tool
    incidents = load_incidents(incidents_file)

    @tool
    def search_knowledge_base(query: str) -> str:
        """Busca procedimientos corporativos vigentes en modo solo lectura."""
        docs = knowledge.retrieve(query)
        return "\n\n".join(
            f"{d.metadata.get('source_id')} v{d.metadata.get('version')}: {d.page_content}"
            for d in docs
        )

    @tool
    def get_incident(incident_id: str) -> dict:
        """Obtiene un incidente por identificador exacto INC-* en modo solo lectura."""
        return get_incident_record(incidents, incident_id)

    @tool
    def calculate_duration_minutes(start_iso: str, end_iso: str) -> int:
        """Calcula minutos entre dos timestamps ISO-8601."""
        return duration_minutes(start_iso, end_iso)

    return [search_knowledge_base, get_incident, calculate_duration_minutes]
