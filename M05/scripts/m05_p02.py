
import torch
from torch.nn.functional import cosine_similarity
from transformers import AutoTokenizer, AutoModel

MODEL_ID = "google/bert_uncased_L-2_H-128_A-2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModel.from_pretrained(MODEL_ID)
model.eval()

sentences = [
    "The bank approved the loan.",
    "The engineer sat on the bank of the river.",
]

def locate_token(text, token_text="bank"):
    encoded = tokenizer(text, return_tensors="pt")
    tokens = tokenizer.convert_ids_to_tokens(encoded["input_ids"][0])
    try:
        index = tokens.index(token_text)
    except ValueError:
        raise RuntimeError(f"No encontré {token_text!r} en {tokens}")
    return encoded, tokens, index

enc1, tokens1, idx1 = locate_token(sentences[0])
enc2, tokens2, idx2 = locate_token(sentences[1])
print(tokens1, idx1)
print(tokens2, idx2)

# Embedding de entrada: mismo token ID -> mismo vector antes del Transformer
embedding_layer = model.get_input_embeddings()
id1 = enc1["input_ids"][0, idx1]
id2 = enc2["input_ids"][0, idx2]

input_vec1 = embedding_layer(id1)
input_vec2 = embedding_layer(id2)
print("Mismo token id:", int(id1), int(id2))
print("Cosine input embedding:", float(cosine_similarity(input_vec1, input_vec2, dim=0)))

# Embedding contextual: depende de toda la frase
with torch.no_grad():
    out1 = model(**enc1).last_hidden_state[0, idx1]
    out2 = model(**enc2).last_hidden_state[0, idx2]

print("Cosine contextual bank/bank:", float(cosine_similarity(out1, out2, dim=0)))

# Mean pooling con máscara
def mean_pool(last_hidden_state, attention_mask):
    mask = attention_mask.unsqueeze(-1).to(last_hidden_state.dtype)
    summed = (last_hidden_state * mask).sum(dim=1)
    counts = mask.sum(dim=1).clamp(min=1e-9)
    return summed / counts

batch = [
    "The server is unavailable.",
    "The service is down.",
    "A river crosses the mountain.",
]

encoded = tokenizer(batch, padding=True, return_tensors="pt")
with torch.no_grad():
    hidden = model(**encoded).last_hidden_state

sentence_vectors = mean_pool(hidden, encoded["attention_mask"])
normalized = torch.nn.functional.normalize(sentence_vectors, p=2, dim=1)
sim_matrix = normalized @ normalized.T
print("\nCosine similarity matrix")
print(sim_matrix)

# Pooling incorrecto: incluye padding como si fuera contenido
wrong_pool = hidden.mean(dim=1)
wrong_norm = torch.nn.functional.normalize(wrong_pool, p=2, dim=1)
wrong_matrix = wrong_norm @ wrong_norm.T

print("\nDiferencia por ignorar la máscara")
print(sim_matrix - wrong_matrix)
