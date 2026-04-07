import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# load model once
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Method 1: manual text
print("\n--- Manual Text Search ---")

manual_texts = [
    "Machine learning is amazing",
    "Python is useful for data science",
    "Deep learning gives powerful models",
    "FAISS helps in fast similarity search"
]

manual_vectors = model.encode(manual_texts).astype("float32")

index1 = faiss.IndexFlatL2(manual_vectors.shape[1])
index1.add(manual_vectors)

query = "what is deep learning"
query_vec = model.encode([query]).astype("float32")

dist, idx = index1.search(query_vec, 2)

for i in idx[0]:
    print(manual_texts[i])


# Method 2: read from file
print("\n--- File Text Search ---")

with open("texts.txt", "r", encoding="utf-8") as f:
    file_texts = [line.strip() for line in f if line.strip()]

file_vectors = model.encode(file_texts).astype("float32")

index2 = faiss.IndexFlatL2(file_vectors.shape[1])
index2.add(file_vectors)

query2 = "what is ai"
query_vec2 = model.encode([query2]).astype("float32")

dist2, idx2 = index2.search(query_vec2, 2)

for i in idx2[0]:
    print(file_texts[i])


# Method 3: combine both
print("\n--- Combined Search ---")

all_texts = manual_texts + file_texts

all_vectors = model.encode(all_texts).astype("float32")

index3 = faiss.IndexFlatL2(all_vectors.shape[1])
index3.add(all_vectors)

query3 = "machine learning"
query_vec3 = model.encode([query3]).astype("float32")

dist3, idx3 = index3.search(query_vec3, 3)

for i in idx3[0]:
    print(all_texts[i])