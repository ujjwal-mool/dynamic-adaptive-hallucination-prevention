import pandas as pd
import matplotlib.pyplot as plt
import os


os.makedirs("graphs", exist_ok=True)

df = pd.read_csv("results/results.csv")

os.makedirs("graphs", exist_ok=True)



plt.figure(figsize=(8,5))
plt.hist(df["Risk Score"], bins=10)

plt.title("Risk Score Distribution")
plt.xlabel("Risk Score")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("graphs/risk_distribution.png")
plt.close()



plt.figure(figsize=(8,5))
plt.hist(df["Confidence"], bins=10)

plt.title("Confidence Distribution")
plt.xlabel("Confidence")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("graphs/confidence_distribution.png")
plt.close()



plt.figure(figsize=(8,5))

plt.scatter(
    df["Maximum Budget"],
    df["Responses Generated"]
)

plt.title("Budget vs Responses Generated")
plt.xlabel("Allocated Budget")
plt.ylabel("Responses Generated")

plt.tight_layout()
plt.savefig("graphs/budget_vs_generated.png")
plt.close()



saved = df["API Calls Saved"].value_counts().sort_index()

plt.figure(figsize=(8,5))

saved.plot(kind="bar")

plt.title("API Calls Saved")
plt.xlabel("Calls Saved")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("graphs/api_saved.png")
plt.close()



plt.figure(figsize=(7,7))

df["Decision"].value_counts().plot(kind="pie", autopct="%1.1f%%")

plt.ylabel("")
plt.title("Decision Distribution")

plt.tight_layout()
plt.savefig("graphs/decision_distribution.png")
plt.close()

print("\nGraphs generated successfully!")
print("Saved inside graphs/ folder.")