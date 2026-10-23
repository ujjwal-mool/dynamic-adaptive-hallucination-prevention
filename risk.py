TECHNICAL_KEYWORDS = [
    "quantum", "transformer", "llm", "rag", "bert",
    "gpu", "cuda", "decoherence", "superconducting",
    "neural", "reinforcement", "bayesian", "diffusion",
    "embedding", "token", "inference", "fine-tuning",
    "cryptography", "compiler", "kernel",
    "docker", "kubernetes", "blockchain", "sql",
    "tcp", "udp", "database", "cloud", "api"
]

TEMPORAL_KEYWORDS = [
    "latest", "current", "today", "recent", "new",
    "2024", "2025", "2026", "2030", "2035"
]

REASONING_KEYWORDS = [
    "compare", "difference", "advantages", "disadvantages",
    "limitations", "future", "impact", "should",
    "better", "versus", "vs", "tradeoff", "evaluate"
]


def get_risk(question):

    q = question.lower()

    score = 0

    # Length
    if len(q) > 50:
        score += 0.10

    if len(q) > 90:
        score += 0.10

    # Explain / How / Why
    if any(word in q for word in ["why", "how", "explain"]):
        score += 0.15

    # Comparative reasoning
    if any(word in q for word in REASONING_KEYWORDS):
        score += 0.25

    # Technical complexity
    tech_count = sum(word in q for word in TECHNICAL_KEYWORDS)
    score += min(tech_count * 0.10, 0.30)

    # Time-sensitive
    if any(word in q for word in TEMPORAL_KEYWORDS):
        score += 0.25

    return round(min(score, 1.0), 2)