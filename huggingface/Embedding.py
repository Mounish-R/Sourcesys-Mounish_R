from sentence_transformers import SentenceTransformer, util
import numpy as np


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


text_data = [
    "Cricket is my favorite sport",
    "I enjoy outdoor games",
    "The sky looks clear and blue",
    "AI is changing modern industries",
    "Machines can learn patterns from data",
    "Reading books is my hobby",
    "Today's weather feels great",
    "He is developing a new application",
    "Technology keeps advancing",
    "She loves music a lot",
    "Data science is fascinating",
    "Python is widely used for coding",
    "Exploring new places is exciting"
]


vector_embeddings = embedding_model.encode(text_data, convert_to_numpy=True)


print("Embedding shape:", vector_embeddings.shape)


print("\nSample embeddings:\n", vector_embeddings[:2])


similarity_score = util.cos_sim(vector_embeddings[0], vector_embeddings[1])

print("\nSimilarity between first two sentences:", similarity_score.item())