from transformers import AutoTokenizer
MODEL_ID = "HuggingFaceTB/SmolLM2-135M-Instruct"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

text = "El servicio estará disponible después del mantenimiento."
ids = tokenizer(text, add_special_tokens=False)["input_ids"]
tokens = tokenizer.convert_ids_to_tokens(ids)
print("texto:", text)
print("tokens:", tokens)
print("ids:", ids)
print("n_tokens:", len(ids))

technical = ["CVE-2026-1234","customer_id","/api/v2/status","192.168.10.25","OpenTelemetry","Kubernetes"]
print("\nIDENTIFICADORES TÉCNICOS")
for item in technical:
    item_ids = tokenizer(item, add_special_tokens=False)["input_ids"]
    print(f"{item:24s} -> {len(item_ids):2d} tokens -> {tokenizer.convert_ids_to_tokens(item_ids)}")

long_text = "inicio " + ("detalle " * 300) + " INFORMACION_CRITICA_FINAL"
encoded = tokenizer(long_text, max_length=64, truncation=True, return_tensors="pt")
decoded = tokenizer.decode(encoded["input_ids"][0], skip_special_tokens=True)
print("\n¿Sobrevive INFORMACION_CRITICA_FINAL?", "INFORMACION_CRITICA_FINAL" in decoded)

def token_count(tokenizer, value):
    return len(tokenizer(value, add_special_tokens=False)["input_ids"])

def estimate_budget(tokenizer, system, history, user, output_reserve, context_limit):
    input_tokens = token_count(tokenizer, system)
    input_tokens += sum(token_count(tokenizer, turn) for turn in history)
    input_tokens += token_count(tokenizer, user)
    total_reserved = input_tokens + output_reserve
    return {"input_tokens": input_tokens,"total_reserved": total_reserved,"fits": total_reserved <= context_limit,"remaining": context_limit-total_reserved}

print("\nCabe:", estimate_budget(tokenizer,"Eres un asistente técnico.",["estado","operativo"],"Resume el incidente.",64,256))
print("No cabe:", estimate_budget(tokenizer,"Eres un asistente técnico.",["detalle "*80,"contexto "*80],"Resume el incidente.",80,256))
