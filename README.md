
# DAHP: Dynamic Adaptive Hallucination Prevention Framework

An adaptive multi-perspective reasoning framework that reduces LLM hallucinations by dynamically allocating reasoning budget based on query complexity, measuring semantic agreement between generated responses, and producing a consensus answer.

## Overview

Traditional self-consistency methods generate a fixed number of responses for every query, leading to unnecessary API calls and increased computational cost. DAHP introduces an adaptive pipeline that determines how many perspectives are actually needed for each query.

The framework estimates query risk, allocates an appropriate reasoning budget, measures semantic agreement using Sentence Transformers, and stops generating additional responses once sufficient confidence has been achieved.

## Features

- Adaptive Risk Prediction
- Dynamic Perspective Allocation
- Multi-Perspective Response Generation
- Semantic Confidence Estimation
- Adaptive Early Stopping
- Consensus Answer Generation
- Benchmarking Pipeline
- Automatic Logging
- Performance Visualization

## Architecture

```
                    User Query
                         │
                         ▼
                Risk Prediction
                         │
                         ▼
          Adaptive Budget Allocation
                         │
                         ▼
          Multi-Perspective Generation
                         │
                         ▼
      Semantic Confidence Estimation
                         │
                         ▼
          Adaptive Early Stopping
                         │
                         ▼
            Consensus Generation
                         │
                         ▼
                 Final Response
                         │
                         ▼
        Benchmarking & Visualization
```

---

## Project Structure

```
DAHP/
│
├── app.py                 # Interactive application
├── pipeline.py            # Complete DAHP pipeline
├── llm.py                 # LLM interface
├── risk.py                # Query risk predictor
├── allocator.py           # Adaptive response allocation
├── adaptive.py            # Early stopping logic
├── confidence.py          # Semantic confidence calculation
├── consensus.py           # Consensus generation
├── decision.py            # Confidence classification
├── logger.py              # Benchmark logging
├── benchmark.py           # Automated benchmark runner
├── visualize.py           # Performance visualization
├── prompt.py              # Perspective prompts
├── questions.csv          # Benchmark dataset
├── results/
│   └── results.csv
├── graphs/
└── README.md
```

---

## Pipeline

1. User submits a query.
2. Risk Predictor estimates query complexity.
3. Adaptive Allocator assigns the maximum reasoning budget.
4. Multiple perspectives are generated using different prompting strategies.
5. Sentence Transformers compute semantic similarity between responses.
6. If confidence exceeds a threshold, generation stops early.
7. Remaining responses (if needed) are generated.
8. A consensus engine produces the final answer.
9. Results are logged for benchmarking and visualization.

---

## Technologies Used

- Python
- OpenRouter API
- Sentence Transformers
- Scikit-learn
- NumPy
- Pandas
- Matplotlib

---

## Installation

```bash
git clone https://github.com/<your-username>/DAHP.git

cd DAHP

pip install -r requirements.txt
```

Create a `.env` file

```
OPENROUTER_API_KEY=your_api_key
```

---

## Running

### Interactive Mode

```bash
python app.py
```

### Benchmark

```bash
python benchmark.py
```

### Generate Graphs

```bash
python visualize.py
```

---

## Example Output

```
Risk Score          : 0.45
Maximum Budget      : 3

Responses Generated : 2
API Calls Saved     : 3
Final Confidence    : 0.94
Decision            : HIGH CONFIDENCE
```

---

## Benchmark Metrics

DAHP records:

- Risk Score
- Allocated Budget
- Responses Generated
- API Calls Saved
- Confidence Score
- Final Decision

Generated graphs include:

- Risk Distribution
- Confidence Distribution
- Budget vs Responses
- API Calls Saved
- Decision Distribution

---

## Motivation

Large Language Models often hallucinate when answering complex or ambiguous queries. Existing self-consistency approaches improve reliability but require generating a fixed number of responses regardless of query difficulty.

DAHP introduces adaptive reasoning, allocating computational resources only when necessary, thereby reducing API usage while maintaining response quality.

---

## Future Work

- Reinforcement Learning based risk prediction
- Entropy-based confidence estimation
- Multi-model ensemble reasoning
- Retrieval-Augmented Generation (RAG)
- Knowledge graph integration
- Human evaluation benchmark
- IEEE publication and large-scale benchmarking

---

## Author

**Ujjwal Moolchandani**

Dayananda Sagar College of Engineering

B.E. Computer Science

```

I think this README is strong enough for both your GitHub portfolio and your project presentation. It explains the motivation, architecture, implementation, and usage without overselling the project.
