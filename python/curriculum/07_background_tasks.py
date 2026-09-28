import threading
import time

def agent_background_task(task_name, duration, progress_callback):
    """Simulates a long-running agent task."""
    print(f"\n[Agent Process] Starting task: '{task_name}'")
    for i in range(1, duration + 1):
        time.sleep(1) # Simulate work
        progress_callback(f"Working... {i}/{duration} seconds elapsed.")
    print(f"[Agent Process] Task '{task_name}' finished!\n")

def on_progress(msg):
    print(f"   -> [UI Update] {msg}")

def background_demo():
    print("Welcome to Stage 7: Background Tasks.")
    print("Main thread is free while the agent works in the background.")

    # Start agent task in a thread
    t = threading.Thread(
        target=agent_background_task,
        args=("Analyze big dataset", 5, on_progress)
    )
    t.start()

    # Main loop remains responsive
    for i in range(3):
        print(f"[Main Thread] Doing other things... ({i+1})")
        time.sleep(1.5)

    print("[Main Thread] Waiting for agent to finish...")
    t.join()
    print("All done!")

if __name__ == "__main__":
    background_demo()
