class PlannerAgent:
    def __init__(self):
        self.plan = []

    def create_plan(self, objective):
        print(f"[Planner] Creating plan for objective: {objective}")
        # Simulated plan generation
        self.plan = [
            "Research the topic.",
            "Outline the document.",
            "Write the first draft.",
            "Review and revise."
        ]

    def execute_plan(self):
        print("\n[Planner] Starting execution...")
        for i, step in enumerate(self.plan, 1):
            print(f"  -> Executing Step {i}: {step}")
            # Here, the agent would typically loop, act, and observe for each step
            print("     (Step completed successfully)")

        print("[Planner] All steps completed. Goal achieved!\n")

def planning_agent_demo():
    print("Welcome to Stage 3: Planning System.")
    agent = PlannerAgent()
    agent.create_plan("Write an essay on AI.")

    print("\nCurrent Plan:")
    for i, step in enumerate(agent.plan, 1):
        print(f"{i}. {step}")

    agent.execute_plan()

if __name__ == "__main__":
    planning_agent_demo()
