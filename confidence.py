from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_confidence(responses):

    if len(responses) == 1:
        return 0.85

    embeddings = model.encode(responses)

    similarity = cosine_similarity(embeddings)

    scores = []

    n = len(responses)

    for i in range(n):
        for j in range(i + 1, n):
            scores.append(similarity[i][j])

    agreement = np.mean(scores)

    confidence = 0.55 + 0.45 * agreement

    return round(float(confidence), 2)