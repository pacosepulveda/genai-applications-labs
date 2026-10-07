import json
from pathlib import Path
from datetime import datetime
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_aws import ChatBedrockConverse

INCIDENTS = Path("../assets/incidents.json")
if not INCIDENTS.exists():
    INCIDENTS = Path("assets/incidents.json")

incidents = {
    row["incident_id"]: row
    for row in json.loads(INCIDENTS.read_text(encoding="utf-8"))
}

def _get_incident(incident_id: str) -> dict:
    if incident_id not in incidents:
        raise KeyError(incident_id)
    return incidents[incident_id]

def _duration_minutes(start_iso: str, end_iso: str) -> int:
    start = datetime.fromisoformat(start_iso.replace("Z", "+00:00"))
    end = datetime.fromisoformat(end_iso.replace("Z", "+00:00"))
    return int((end - start).total_seconds() // 60)

incident = _get_incident("INC-2048")
duration = _duration_minutes(incident["opened_at"], incident["closed_at"])
print(incident)
print("Duración:", duration, "minutos")
assert duration == 72

@tool
def get_incident(incident_id: str) -> dict:
    """Obtiene un incidente por ID exacto INC-* en modo solo lectura."""
    return _get_incident(incident_id)

@tool
def calculate_duration_minutes(start_iso: str, end_iso: str) -> int:
    """Calcula minutos entre dos timestamps ISO-8601."""
    return _duration_minutes(start_iso, end_iso)

model = ChatBedrockConverse(
    model="us.openai.gpt-5.6-luna",
    region_name="us-east-1",
    temperature=0,
)

agent = create_agent(
    model=model,
    tools=[get_incident, calculate_duration_minutes],
    system_prompt=(
        "Eres un asistente de operaciones. "
        "Utiliza únicamente las tools disponibles para datos de incidentes. "
        "No inventes timestamps."
    ),
)

print("\n--- Agent ---")
try:
    result = agent.invoke({
        "messages": [
            {"role": "user", "content": "Consulta INC-2048 y dime cuánto duró el incidente."}
        ]
    })
    print(result)
except Exception as exc:
    print("Bedrock no disponible en esta ejecución:", type(exc).__name__, str(exc)[:300])
