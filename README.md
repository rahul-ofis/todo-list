# Simple FastAPI Todo Application

A basic todo application with three columns: Serial Number, Todo, and Completed status.

## Features

- Health check endpoint
- List all todos with their completion status
- Add new todos
- Mark todos as completed

## API Endpoints

1. **Health Check**
   - URL: `/health`
   - Method: GET
   - Returns the health status of the application

2. **List All Todos**
   - URL: `/todos`
   - Method: GET
   - Shows all todo items with their serial number, task description, and completion status

3. **Add New Todo**
   - URL: `/todo/{task}`
   - Method: POST
   - Add a new task by specifying it in the URL
   - Example: `/todo/buy-groceries`

4. **Mark Todo as Completed**
   - URL: `/todo/{serial_number}/completed`
   - Method: PUT
   - Mark a task as completed using its serial number
   - Example: `/todo/1/completed`

## Setup and Installation

1. Install required packages:
```bash
pip install fastapi uvicorn
```

2. Run the application:
```bash
uvicorn todo-app:app --reload
```

The application will start on `http://localhost:8000`

## Examples

1. Check health:
   ```
   GET http://localhost:8000/health
   ```

2. Add a new todo:
   ```
   POST http://localhost:8000/todo/buy-groceries
   ```

3. List all todos:
   ```
   GET http://localhost:8000/todos
   ```

4. Mark a todo as completed:
   ```
   PUT http://localhost:8000/todo/1/completed
   ```
