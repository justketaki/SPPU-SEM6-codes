class EmployeePerformanceEvaluation:
    def __init__(self):
        self.criteria = [
            "Teamwork",
            "Punctuality",
            "Task Completion",
            "Communication Skills",
            "Problem Solving",
            "Leadership (if applicable, else rate as 3)"
        ]
        self.scores = {}

    def get_input(self):
        """Get ratings from the user."""
        print("\nRate the following on a scale of 1 (Poor) to 5 (Excellent):")
        for criterion in self.criteria:
            while True:
                try:
                    score = int(input(f"{criterion}: "))
                    if score < 1 or score > 5:
                        raise ValueError("Score must be between 1 and 5.")
                    self.scores[criterion] = score
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a score between 1 and 5.")

    def calculate_average(self):
        """Calculate the average score."""
        total_score = sum(self.scores.values())
        average_score = total_score / len(self.scores)
        return average_score

    def evaluate_performance(self, average_score):
        """Evaluate performance based on average score."""
        if average_score >= 4.5:
            return "Outstanding", "Keep up the great work. Consider for leadership roles or promotions."
        elif average_score >= 3.5:
            return "Good", "Consistent performance. Minor improvements will boost further."
        elif average_score >= 2.5:
            return "Average", "Needs improvement in some areas. Consider targeted training."
        else:
            return "Below Average", "Immediate attention needed. Schedule a performance review and support plan."

    def print_report(self, name, role, average_score, remark, suggestion):
        """Print the final performance report."""
        print("\n=== Performance Report ===")
        print(f"Employee Name: {name}")
        print(f"Department/Role: {role}")
        print(f"Average Score: {average_score:.2f}/5")
        print(f"Performance Remark: {remark}")
        print(f"Recommendation: {suggestion}")

    def run_evaluation(self):
        """Run the entire performance evaluation process."""
        print("=== Expert System: Employee Performance Evaluation ===")
        
        name = input("Enter Employee Name: ")
        role = input("Enter Role/Department: ")

        self.get_input()

        average_score = self.calculate_average()
        remark, suggestion = self.evaluate_performance(average_score)

        self.print_report(name, role, average_score, remark, suggestion)


if __name__ == "__main__":
    evaluation_system = EmployeePerformanceEvaluation()
    evaluation_system.run_evaluation()
