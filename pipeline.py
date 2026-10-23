from llm import generate
from risk import get_risk
from allocator import allocate
from prompt import PROMPTS       
from confidence import calculate_confidence
from adaptive import should_continue
from consensus import build_consensus
from decision import decide
from logger import log_result


def run_pipeline(question):

    risk = get_risk(question)
    max_budget = allocate(risk)

    responses = []


    initial = min(2, max_budget)

    for i in range(initial):

        answer = generate(question, PROMPTS[i])

        responses.append(answer)

    confidence = calculate_confidence(responses)

    current = len(responses)

    

    while should_continue(confidence, current, max_budget, risk):

        answer = generate(question, PROMPTS[current])

        responses.append(answer)

        current += 1

        confidence = calculate_confidence(responses)


    final_answer = build_consensus(question, responses)

    

    decision = decide(confidence, risk)

    api_calls_saved = 5 - len(responses)


    log_result(
        question,
        risk,
        max_budget,
        len(responses),
        api_calls_saved,
        confidence,
        decision
    )


    return {
        "question": question,
        "risk": risk,
        "budget": max_budget,
        "responses": responses,
        "responses_generated": len(responses),
        "confidence": confidence,
        "decision": decision,
        "final_answer": final_answer
    }