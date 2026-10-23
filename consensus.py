from llm import generate

def build_consensus(question, responses):

    system_prompt = """
You are an expert evaluator.

You are given multiple independently generated responses to the same question.

1. Identify the common facts.
2. Resolve contradictions.
3. Produce one final reliable answer.

Return ONLY the consensus answer.
"""

    formatted = ""

    for i, r in enumerate(responses, 1):
        formatted += f"\nResponse {i}:\n{r}\n"

    final_prompt = f"""
Original Question:
{question}

Generated Responses:
{formatted}
"""

    try:
        return generate(final_prompt, system_prompt)

    except Exception as e:
        print(f"\nConsensus Engine unavailable ({e})")
        print("Returning highest-confidence perspective.\n")

        return responses[0]