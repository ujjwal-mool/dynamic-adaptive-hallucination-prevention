import csv
import os
from datetime import datetime

RESULTS_DIR = "results"
RESULTS_FILE = os.path.join(RESULTS_DIR, "results.csv")


def log_result(question, risk, max_budget, responses_generated,api_calls_saved,
               confidence, decision):

    os.makedirs(RESULTS_DIR, exist_ok=True)

    file_exists = os.path.isfile(RESULTS_FILE)

    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Question",
                "Risk Score",
                "Maximum Budget",
                "Responses Generated",
                "API Calls Saved",
                "Confidence",
                "Decision"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            question,
            round(risk, 2),
            max_budget,
            responses_generated,
            api_calls_saved,
            round(confidence, 2),
            decision
        ])