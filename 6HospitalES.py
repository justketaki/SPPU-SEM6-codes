class HospitalTriageSystem:
    def __init__(self):
        self.symptom_data = {
            "Chest Pain": False,
            "Shortness of Breath": False,
            "Heavy Bleeding": False,
            "High Fever": False,
            "Recent Injury": False,
            "Dizziness or Fainting": False,
            "Severe Stomach Pain": False
        }

    def get_input(self):
        """Collect symptoms from the user."""
        print("\nSelect Symptoms (Y/N):")
        for symptom in self.symptom_data:
            while True:
                user_input = input(f"{symptom}? ").lower()
                if user_input in ['y', 'n']:
                    self.symptom_data[symptom] = user_input == 'y'
                    break
                else:
                    print("Invalid input! Please enter 'Y' for Yes or 'N' for No.")

    def determine_department_and_advice(self, age):
        """Determine which department the patient should visit based on symptoms."""
        if self.symptom_data["Heavy Bleeding"] or self.symptom_data["Recent Injury"]:
            department = "Emergency Room (ER)"
            advice = "Immediate attention required. Proceed to the ER."
        elif self.symptom_data["Chest Pain"] or self.symptom_data["Shortness of Breath"]:
            department = "Cardiology"
            advice = "Cardiac symptoms detected. Visit Cardiology immediately."
        elif self.symptom_data["High Fever"] and age < 12:
            department = "Pediatrics"
            advice = "High fever in child. Visit Pediatrics urgently."
        elif self.symptom_data["High Fever"]:
            department = "General Medicine"
            advice = "Consult a general physician for evaluation."
        elif self.symptom_data["Dizziness or Fainting"]:
            department = "Neurology"
            advice = "Neurological symptoms present. Visit Neurology."
        elif self.symptom_data["Severe Stomach Pain"]:
            department = "Gastroenterology"
            advice = "Visit a gastroenterologist for further diagnosis."
        else:
            department = "Outpatient (OPD)"
            advice = "No critical symptoms. You may proceed to OPD."

        return department, advice

    def print_report(self, name, department, advice):
        """Print the patient's report."""
        print("\n=== Patient Report ===")
        print(f"Name: {name}")
        print(f"Recommended Department: {department}")
        print(f"Advice: {advice}")

    def run_triage(self):
        """Run the triage system."""
        print("=== Hospital Expert System: Patient Triage Assistant ===")
        
        name = input("Enter Patient Name: ")
        
        while True:
            try:
                age = int(input("Enter Age: "))
                if age <= 0:
                    raise ValueError("Age must be a positive number.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid age.")

        self.get_input()

        department, advice = self.determine_department_and_advice(age)

        self.print_report(name, department, advice)


if __name__ == "__main__":
    triage_system = HospitalTriageSystem()
    triage_system.run_triage()
