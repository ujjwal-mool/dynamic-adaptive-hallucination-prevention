from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load once when program starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_confidence(responses):

    # If only one response exists
    if len(responses) == 1:
        return 1.0

    embeddings = model.encode(responses)

    similarity_matrix = cosine_similarity(embeddings)

    similarities = []

    n = len(responses)

    for i in range(n):
        for j in range(i + 1, n):
            similarities.append(similarity_matrix[i][j])

    confidence = np.mean(similarities)

    return float(confidence)