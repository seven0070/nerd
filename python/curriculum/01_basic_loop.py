def mock_llm_call(prompt):
    """Simulate an LLM response."""
    return f"I am a simulated AI. I received your message: '{prompt}'"

def basic_agent_loop():
    print("Welcome to Stage 1: Basic Agent Loop.")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Agent: Goodbye!")
                break

            response = mock_llm_call(user_input)
            print(f"Agent: {response}\n")
        except EOFError:
            break

if __name__ == "__main__":
    basic_agent_loop()
