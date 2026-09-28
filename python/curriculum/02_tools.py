import json

def get_weather(location):
    """A simulated tool."""
    return f"The weather in {location} is 72°F and sunny."

TOOLS = {
    "get_weather": get_weather
}

def mock_llm_call_with_tools(prompt):
    """Simulate an LLM deciding to use a tool."""
    if "weather" in prompt.lower() and "seattle" in prompt.lower():
        # Simulate a tool call JSON response
        return '{"action": "tool_call", "tool_name": "get_weather", "arguments": {"location": "Seattle"}}'
    return f"I am just a simple AI. I don't know the answer to '{prompt}'"

def execute_tool(tool_name, arguments):
    if tool_name in TOOLS:
        func = TOOLS[tool_name]
        print(f"[System] Executing tool '{tool_name}' with args {arguments}...")
        return func(**arguments)
    return f"Error: Tool {tool_name} not found."

def tool_agent_loop():
    print("Welcome to Stage 2: Tool Usage.")
    print("Ask about the weather in Seattle, or type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ['exit', 'quit']:
                break

            response = mock_llm_call_with_tools(user_input)

            # Very basic parsing
            try:
                data = json.loads(response)
                if data.get("action") == "tool_call":
                    tool_result = execute_tool(data["tool_name"], data["arguments"])
                    print(f"Agent (Tool Result): {tool_result}\n")
                else:
                    print(f"Agent: {response}\n")
            except json.JSONDecodeError:
                 print(f"Agent: {response}\n")

        except EOFError:
            break

if __name__ == "__main__":
    tool_agent_loop()
