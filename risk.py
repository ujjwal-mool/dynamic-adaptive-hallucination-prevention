TECHNICAL_KEYWORDS = [
    "quantum", "transformer", "llm", "rag", "bert",
    "gpu", "cuda", "decoherence", "superconducting",
    "neural", "reinforcement", "bayesian", "diffusion",
    "embedding", "token", "inference", "fine-tuning",
    "cryptography", "compiler", "kernel"
]

TEMPORAL_KEYWORDS = [
    "latest", "current", "today", "recent", "new",
    "2024", "2025", "2026", "2030", "2035"
]

def get_risk(question):

    q = question.lower()

    score = 0

    # Long questions
    if len(q) > 50:
        score += 0.15

    # Complex reasoning words
    if any(word in q for word in ["why", "how", "explain", "compare", "analyze"]):
        score += 0.2

    # Technical topics
    tech_count = sum(word in q for word in TECHNICAL_KEYWORDS)
    score += min(tech_count * 0.1, 0.3)

    # Time-sensitive questions
    if any(word in q for word in TEMPORAL_KEYWORDS):
        score += 0.3

    return min(score, 1.0)

print(get_risk("What is the weather?"))
print(get_risk("How does quantum computing work?"))
print(get_risk("What is the latest GPU technology in 2026?"))