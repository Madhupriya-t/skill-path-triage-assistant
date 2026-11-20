"""Skill Path Triage Assistant core functionality."""

from thilimarketbasket.mine import frequent_itemsets, rules
from app.llm import chat


# Milestone 1: Employee skill sequences

EMPLOYEE_SEQUENCES = {
    "E001": ["Python", "SQL", "Machine Learning", "Deep Learning"],
    "E002": ["Python", "SQL", "Data Analytics", "Power BI"],
    "E003": ["Python", "Machine Learning", "Deep Learning", "NLP"],
    "E004": ["SQL", "Python", "Machine Learning", "Deep Learning"],
    "E005": ["Python", "SQL", "Machine Learning", "NLP"],
}


def milestone_1():
    return EMPLOYEE_SEQUENCES


# Milestone 2: Frequent skill transition mining

def milestone_2():
    sequences = milestone_1()
    baskets = []

    for skills in sequences.values():
        transitions = [
            f"{skills[i]} -> {skills[i + 1]}"
            for i in range(len(skills) - 1)
        ]
        baskets.append(transitions)

    itemsets = frequent_itemsets(
        baskets,
        min_support=0.2,
        max_size=3
    )

    association_rules = rules(
        itemsets,
        min_confidence=0.3
    )

    return {
        "itemsets": itemsets,
        "rules": association_rules
    }


# Milestone 3: Next-skill prediction

def milestone_3(current_skills):
    if not current_skills:
        raise ValueError("Please provide at least one existing skill.")

    examples = "\n".join(
        f"{employee}: {' -> '.join(skills)}"
        for employee, skills in EMPLOYEE_SEQUENCES.items()
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are a career skill recommendation assistant. "
                "Recommend one relevant next skill based on existing skills "
                "and employee skill sequences. Explain your recommendation. "
                "Do not recommend a skill the employee already has. "
                "Only make claims supported by the provided sequences."
            )
        },
        {
            "role": "user",
            "content": (
                f"Employee skill sequences:\n{examples}\n\n"
                f"Current employee skills: {', '.join(current_skills)}\n\n"
                "Predict the most suitable next skill and explain why."
            )
        }
    ]

    return chat(
        messages,
        temperature=0.3,
        max_completion_tokens=500,
        reasoning_effort="low",
        include_reasoning=False
    )


# Milestone 4: Evaluate next-skill predictions

def milestone_4():
    results = []

    for employee, skills in EMPLOYEE_SEQUENCES.items():
        current_skills = skills[:-1]
        actual_next_skill = skills[-1]

        prediction = milestone_3(current_skills)

        correct = actual_next_skill.lower() in prediction.lower()

        results.append({
            "employee": employee,
            "current_skills": current_skills,
            "actual_next_skill": actual_next_skill,
            "prediction": prediction,
            "correct": correct
        })

    correct_predictions = sum(
        result["correct"] for result in results
    )

    accuracy = correct_predictions / len(results) * 100

    return {
        "results": results,
        "correct_predictions": correct_predictions,
        "total_predictions": len(results),
        "accuracy": accuracy
    }