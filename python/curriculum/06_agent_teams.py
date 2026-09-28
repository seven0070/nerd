class WorkerAgent:
    def __init__(self, specialty):
        self.specialty = specialty

    def perform_task(self, task):
        print(f"  [Worker - {self.specialty}] Received task: '{task}'")
        # Simulated work
        return f"Completed '{task}'"

class ManagerAgent:
    def __init__(self):
        self.workers = {
            "coder": WorkerAgent("Coding"),
            "researcher": WorkerAgent("Research")
        }

    def delegate(self, objective):
        print(f"[Manager] Analyzing objective: '{objective}'")

        # Simulated delegation logic
        print("[Manager] Delegating research task...")
        research_result = self.workers["researcher"].perform_task("Find info on Python ASTs")
        print(f"[Manager] Research result: {research_result}")

        print("[Manager] Delegating coding task...")
        coding_result = self.workers["coder"].perform_task("Write AST parser script")
        print(f"[Manager] Coding result: {coding_result}")

        print("[Manager] Objective complete!")

def teams_demo():
    print("Welcome to Stage 6: Agent Teams.")
    manager = ManagerAgent()
    manager.delegate("Build a Python code analyzer.")

if __name__ == "__main__":
    teams_demo()
