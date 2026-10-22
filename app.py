from llm import generate
from risk import get_risk
from allocator import allocate
from prompt import PROMPTS
from confidence import calculate_confidence

question = input("Enter your question: ")

risk = get_risk(question)
num = allocate(risk)

print(f"\nRisk Score: {risk}")
print(f"Perspectives: {num}")

responses = []

for i in range(num):

    answer = generate(question, PROMPTS[i])

    responses.append(answer)

    print(f"\n========== Perspective {i+1} ==========\n")

    print(answer)

confidence = calculate_confidence(responses)

print("\n=========================")
print(f"Confidence : {confidence:.2f}")