from pipeline import run_pipeline

question = input("Enter your question: ")

result = run_pipeline(question)

print("\n========================================")
print("DAHP RESULTS")
print("========================================")

print(f"Risk Score          : {result['risk']:.2f}")
print(f"Maximum Budget      : {result['budget']}")

print("\n========================================")
print("GENERATED PERSPECTIVES")
print("========================================")

for i, response in enumerate(result["responses"], start=1):

    print(f"\n========== Perspective {i} ==========\n")

    print(response)

print("\n========================================")
print("CONSENSUS ANSWER")
print("========================================")

print(result["final_answer"])

print("\n========================================")
print("FINAL SUMMARY")
print("========================================")

print(f"Responses Generated : {result['responses_generated']}")
print(f"API Calls Saved     : {result['budget'] - result['responses_generated']}")
print(f"Final Confidence    : {result['confidence']:.2f}")
print(f"Decision            : {result['decision']}")

print("========================================")