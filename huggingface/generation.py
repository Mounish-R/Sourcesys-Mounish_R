from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

result = generator(
    "AI will change",
    max_new_tokens=30,
    do_sample=True,
    temperature=0.7
)

print(result[0]['generated_text'])