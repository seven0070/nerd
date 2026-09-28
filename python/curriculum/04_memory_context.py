class MemorySystem:
    def __init__(self, max_context_length=3):
        self.history = []
        self.max_context = max_context_length
        self.summary = ""

    def add_interaction(self, user_msg, agent_msg):
        self.history.append({"user": user_msg, "agent": agent_msg})

        # Simple context management: summarize if history gets too long
        if len(self.history) > self.max_context:
            self._summarize_oldest()

    def _summarize_oldest(self):
        # In reality, this would be an LLM call to summarize
        oldest = self.history.pop(0)
        print(f"[Memory System] Context limit reached. Summarizing oldest interaction...")
        new_summary_part = f"User asked about '{oldest['user']}'. "
        self.summary += new_summary_part

    def get_context(self):
        ctx = "=== Context ===\n"
        if self.summary:
            ctx += f"Summary of past: {self.summary}\n"
        ctx += "Recent History:\n"
        for idx, item in enumerate(self.history):
            ctx += f"  [{idx}] User: {item['user']} | Agent: {item['agent']}\n"
        ctx += "===============\n"
        return ctx

def memory_demo():
    print("Welcome to Stage 4: Memory & Context.")
    mem = MemorySystem(max_context_length=2)

    interactions = [
        ("Hi!", "Hello there!"),
        ("What is your name?", "I am Agent."),
        ("What color is the sky?", "Blue."),
        ("Do you remember my first question?", "Let me check my memory...")
    ]

    for u, a in interactions:
        print(f"\nUser: {u}")
        print(f"Agent: {a}")
        mem.add_interaction(u, a)
        print("\n--- Current State of Memory ---")
        print(mem.get_context())

if __name__ == "__main__":
    memory_demo()
