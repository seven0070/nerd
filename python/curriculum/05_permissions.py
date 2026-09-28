def delete_file_tool(filename):
    """A dangerous tool."""
    return f"File '{filename}' has been deleted."

def read_file_tool(filename):
    """A safe tool."""
    return f"Contents of '{filename}'..."

TOOLS = {
    "delete_file": {"func": delete_file_tool, "requires_permission": True},
    "read_file": {"func": read_file_tool, "requires_permission": False}
}

def execute_with_permissions(tool_name, arguments):
    if tool_name not in TOOLS:
        return "Tool not found."

    tool_info = TOOLS[tool_name]

    if tool_info["requires_permission"]:
        print(f"\n[SECURITY ALERT] The agent wants to run '{tool_name}' with args {arguments}.")
        choice = input("Do you allow this? (y/n): ")
        if choice.lower() != 'y':
            return "Execution denied by user."

    print(f"[System] Executing '{tool_name}'...")
    return tool_info["func"](**arguments)

def permissions_demo():
    print("Welcome to Stage 5: Permissions System.")

    print("\nAgent tries to read a file...")
    result1 = execute_with_permissions("read_file", {"filename": "data.txt"})
    print(f"Result: {result1}")

    print("\nAgent tries to delete a file...")
    result2 = execute_with_permissions("delete_file", {"filename": "important_data.txt"})
    print(f"Result: {result2}")

if __name__ == "__main__":
    permissions_demo()
