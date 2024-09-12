# College Project

## Objective

The aim of this project is to develop a web application using Python, which simulates the basic functionalities of a task management system, similar to Trello. The application will allow users to manage their tasks, including features such as creating, editing, deleting, and assigning tasks to other users, as well as tracking the status of tasks (pending, in progress, completed).

## Functionalities

- **User Registration and Authentication**: 
  - The system will allow the registration of new users, as well as login and logout for session control.
  - Each user will have access to their own tasks, which can be managed individually.

- **Task Management**: 
  - Users will be able to create, view, edit, and delete tasks.
  - Each task will have a title, description, and status.
  - Tasks can be assigned to other users of the system, promoting collaboration in the management of activities.

- **Task Statuses**: 
  - Tasks will have statuses that indicate progress, such as “pending”, “in progress”, or “completed”.
  - The interface will allow you to filter tasks according to these statuses, making it easier to organize.

- **Dashboard**: 
  - A dashboard to keep track of all the group's tasks.

## Tools Required

The system will be developed using the Flask or Django frameworks for the backend, using a database to store user and task information.

## How to Run the Project

To run the project locally, follow these steps:

**1. Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

**2. Create a virtual environment**:

```sh
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate
```

**3. Install the dependencies:**:

```sh
pip install -r requirements.txt
```

**4. Apply the migrations::**:

```sh
python manage.py migrate
```

**5 Create a superuser (optional, for accessing the admin interface):**:

```sh
python manage.py createsuperuser
```

**6 Run the development server:**:

```sh
python manage.py runserver
```

Now you should be able to use the application locally.
