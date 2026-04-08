import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

data = pd.read_csv("train.csv")

# handle column names
try:
    texts = (data["Title"] + " " + data["Description"]).tolist()
except:
    texts = (data["title"] + " " + data["description"]).tolist()

texts = [t.strip() for t in texts if isinstance(t, str)]
texts = texts[:1000]

vectors = model.encode(texts).astype("float32")

index = faiss.IndexFlatL2(vectors.shape[1])
index.add(vectors)

query = input("Enter search: ").strip()

query_vec = model.encode([query]).astype("float32")

distances, indices = index.search(query_vec, 5)

print("\nTop results:\n")

for rank, i in enumerate(indices[0], start=1):
    score = round(distances[0][rank-1], 2)

    print(f"{rank}. {texts[i]}")
    print(f"   score: {score}\n")