import json
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser

class IncidentAnalysis(BaseModel):
    incident_id: str
    category: str
    requires_review: bool

parser = PydanticOutputParser(pydantic_object=IncidentAnalysis)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Analiza el incidente.\n{format_instructions}"),
    ("user", "ID: {incident_id}\nServicio: {service}\nResumen: {summary}"),
]).partial(format_instructions=parser.get_format_instructions())

data = {
    "incident_id": "INC-2048",
    "service": "payments-api",
    "summary": "Degradación causada por una configuración incorrecta del balanceador.",
}

def deterministic_demo(prompt_value):
    return json.dumps({
        "incident_id": "INC-2048",
        "category": "AVAILABILITY",
        "requires_review": True,
    })

mock_model = RunnableLambda(deterministic_demo)
chain = prompt | mock_model | parser
result = chain.invoke(data)
print(result)
assert isinstance(result, IncidentAnalysis)

from langchain_aws import ChatBedrockConverse

model = ChatBedrockConverse(
    model="us.openai.gpt-5.6-luna",
    region_name="us-east-1",
    temperature=0,
)
structured_model = model.with_structured_output(IncidentAnalysis)
real_chain = prompt | structured_model

print("\n--- GPT-5.6 Luna ---")
try:
    real_result = real_chain.invoke(data)
    print(real_result)
    assert isinstance(real_result, IncidentAnalysis)
except Exception as exc:
    print("Bedrock no disponible en esta ejecución:", type(exc).__name__, str(exc)[:300])
