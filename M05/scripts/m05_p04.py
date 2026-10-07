import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
MODEL_ID = "HuggingFaceTB/SmolLM2-135M-Instruct"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID)
model.eval()
messages=[{"role":"user","content":"Write a short sentence about monitoring a web service."}]
prompt=tokenizer.apply_chat_template(messages,tokenize=False,add_generation_prompt=True)
inputs=tokenizer(prompt,return_tensors="pt")
input_len=inputs["input_ids"].shape[1]
with torch.no_grad():
    forward=model(**inputs)
probs=torch.softmax(forward.logits[0,-1],dim=-1)
top_probs,top_ids=torch.topk(probs,10)
print("TOP 10 NEXT TOKEN")
for token_id,prob in zip(top_ids.tolist(),top_probs.tolist()):
    print(token_id,repr(tokenizer.decode([token_id])),round(prob,5))

def generate(**kwargs):
    with torch.no_grad(): out=model.generate(**inputs,**kwargs)
    return tokenizer.decode(out[0,input_len:],skip_special_tokens=True)

print("\nGREEDY 1\n",generate(max_new_tokens=40,do_sample=False))
print("\nGREEDY 2\n",generate(max_new_tokens=40,do_sample=False))
for temperature in [0.3,1.0]:
    torch.manual_seed(42)
    print("\nTEMP",temperature,"\n",generate(max_new_tokens=40,do_sample=True,temperature=temperature,top_p=1.0))
torch.manual_seed(42)
print("\nTOP-P\n",generate(max_new_tokens=40,do_sample=True,temperature=0.8,top_p=0.9,top_k=0))
for limit in [20,80]:
    print("\nLIMIT",limit,"\n",generate(max_new_tokens=limit,do_sample=False))
