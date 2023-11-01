class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "fever": "Common Cold",
            "cough": "Bronchitis",
            "headache": "Migraine",
            "fatigue": "Anemia",
            "rash": "Allergic Reaction",
        }

    def diagnose(self, symptoms):
        possible_diagnoses = [self.knowledge_base[symptom] for symptom in symptoms if symptom in self.knowledge_base]
        
        if possible_diagnoses:
            return ", ".join(set(possible_diagnoses))
        else:
            return "No specific diagnosis found."

# Main program
if __name__ == "__main__":
    expert_system = ExpertSystem()

    print("Welcome to the Health Diagnosis Expert System.")
    print("Enter your symptoms, one at a time. Type 'done' when finished.")

    symptoms = []
    while True:
        symptom = input("Enter a symptom (or 'done'): ")
        if symptom.lower() == "done":
            break
        symptoms.append(symptom)

    diagnosis = expert_system.diagnose(symptoms)
    if diagnosis:
        print("Potential Diagnoses:", diagnosis)
    else:
        print("No specific diagnosis found.")
