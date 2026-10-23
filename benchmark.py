import pandas as pd
import time
from pipeline import run_pipeline
df = pd.read_csv("datasets/questions.csv")

questions = df["Question"].dropna().tolist()

print("=" * 60)
print(f"Loaded {len(questions)} benchmark questions")
print("=" * 60)

for i, question in enumerate(questions):

    print("\n" + "=" * 70)
    print(f"Question {i+1}/{len(questions)}")
    print("Query :", question)
    print("=" * 70)

    try:
        run_pipeline(question)

    except Exception as e:
        print("\nERROR OCCURRED")
        print(e)
        print("\nWaiting 15 seconds before continuing...\n")
        time.sleep(15)
        continue

    time.sleep(5)

print("\n" + "=" * 70)
print("BENCHMARK COMPLETED")
print("=" * 70)