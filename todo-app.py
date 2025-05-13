from fastapi import FastAPI
from typing import List

app = FastAPI()

# Simple in-memory storage using a list of dictionaries
todos = []
serial_counter = 1

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/todos")
def list_todos():
    return {
        "todos": [
            {
                "serial_number": todo["serial_number"],
                "task": todo["task"],
                "completed": todo["completed"]
            }
            for todo in todos
        ]
    }

@app.get("/todo/{task}")  # Added GET support
@app.post("/todo/{task}")
def add_todo(task: str):
    global serial_counter
    new_todo = {
        "serial_number": serial_counter,
        "task": task,
        "completed": False
    }
    todos.append(new_todo)
    serial_counter += 1
    return {"message": "Task added successfully", "task": new_todo}

@app.get("/todo/{serial_number}/completed")
@app.put("/todo/{serial_number}/completed")
def complete_todo(serial_number: int):
    for todo in todos:
        if todo["serial_number"] == serial_number:
            todo["completed"] = True
            return {"message": "Task marked as completed", "task": todo}
    return {"message": "Task not found"}