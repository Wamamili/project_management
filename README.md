# Project Management System

A **Django + Django REST Framework (DRF) + JWT + MySQL** based project management system that allows teams to manage projects, tasks, and user access with authentication and role-based permissions.  


## Features

- User registration, login, and JWT authentication  
- Role-based access with **Owner**, **Member**, and **Superuser** permissions  
- Project creation, updating, deletion, and member management  
- Task management within projects (create, assign, update, comment, delete)  
- Profile management with password update and profile editing  
- API-first backend with browsable DRF API  
- Dashboard view for logged-in members showing assigned projects  

## Tech Stack

- **Backend**: Django, Django REST Framework  
- **Authentication**: JWT (via `djangorestframework-simplejwt`)  
- **Database**: MySQL  
- **Frontend (templates)**: Django templates with Bootstrap  
- **Deployment Ready**: Configurable via `.env` file  

## Quickstart

1. Clone the repo and create a virtual environment:
   ```bash
   git clone https://github.com/your-username/project_management.git
   cd project_management
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Setup environment variables:
   ```bash
   cp .env.example .env
   # fill in MySQL credentials, secret key, and debug values
   ```

3. Create database and run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run server:
   ```bash
   python manage.py runserver
   ```

5. Access the app:
   - API root: `http://127.0.0.1:8000/api/`  
   - Admin: `http://127.0.0.1:8000/admin/`  
   - Dashboard (after login): `http://127.0.0.1:8000/api/accounts/dashboard/`  

## API Endpoints

### Accounts
- `POST /api/accounts/register/` — Register
- `POST /api/accounts/login/` — JWT login
- `POST /api/accounts/token/refresh/` — Refresh token
- `GET /api/accounts/me/` — Current user
- `GET /api/accounts/dashboard/` — User dashboard
- `GET /api/accounts/profile/` — Profile page

### Projects
- `GET /api/projects/` — List projects for current user
- `POST /api/projects/` — Create project
- `GET /api/projects/<id>/` — Retrieve
- `PUT /api/projects/<id>/` — Update (owner only)
- `DELETE /api/projects/<id>/` — Delete (owner only)
- `POST /api/projects/<id>/add_member/` — Add team member

### Tasks
- `GET /api/projects/<project_id>/tasks/` — List tasks
- `POST /api/projects/<project_id>/tasks/` — Create task
- `GET /api/tasks/<id>/` — Retrieve
- `PUT /api/tasks/<id>/` — Update (assignee or owner)
- `DELETE /api/tasks/<id>/` — Delete (owner or creator)
- `POST /api/tasks/<id>/comment/` — Add comment

## Project Structure

```
project_management/
├── accounts/        # User management, authentication, profiles
├── projects/        # Project models, views, and APIs
├── tasks/           # Task models, views, and APIs
├── project_management/  # Core settings and URLs

```

## Development & Deployment

- Default timezone: **Africa/Nairobi**  
- Custom `User` model with a `role` field:
  ```
  AUTH_USER_MODEL = "accounts.User"
  ```
- Configurable with `.env` for DB credentials, secret key, and debug mode  
- Deployment ready on **Heroku, Render, or DigitalOcean**  

## CI/CD Pipeline

- **GitHub Actions** for tests and lint checks  
- **Docker** for containerized deployments  
- **Coverage reports** for testing  


## Contribution Guidelines

1. Fork the repo  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Commit changes (`git commit -m "Add feature"`)  
4. Push branch (`git push origin feature-name`)  
5. Open a Pull Request  
