from app.core import milestone_4

result = milestone_4()

print("\nEVALUATION RESULTS")
print("------------------")

for item in result["results"]:
    print("Employee:", item["employee"])
    print("Actual skill:", item["actual_next_skill"])
    print("Correct prediction:", item["correct"])
    print()

print("Total correct:", result["correct_predictions"])
print("Total predictions:", result["total_predictions"])
print("Accuracy:", round(result["accuracy"], 2), "%")