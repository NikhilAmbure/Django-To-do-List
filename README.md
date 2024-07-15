## Django To-Do List Project

This is a simple To-Do List web application built using Django, HTML, CSS, Python, and Bootstrap. The project explores CRUD (Create, Read, Update, Delete) operations within the Django framework.

### Features

- **Add Tasks**: Users can add new tasks to the list.
- **View Tasks**: Users can view all tasks.
- **Update Tasks**: Users can update the details of existing tasks.
- **Delete Tasks**: Users can delete tasks that are no longer needed.

### Technologies Used

- **Django**: Backend framework for building the web application.
- **HTML/CSS**: Frontend for the user interface.
- **Bootstrap**: For responsive and modern design.
- **Python**: Programming language for backend logic.

### Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todo-list-django.git
    cd todo-list-django
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and go to `http://127.0.0.1:8000/` to see the application in action.
