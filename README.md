# Project Management System

A **Django + DRF + JWT + MySQL** project management system for teams to manage projects, tasks, and users with authentication and role-based permissions.

## Features

- User registration, login (session & JWT), and logout
- Role-based access: **Owner**, **Member**, **Superuser**
- Project CRUD, member management, and dashboard
- Task management: create, assign, update, comment, delete
- Profile management
- API-first backend with browsable DRF API
- Responsive Django templates (Bootstrap) for login, logout, dashboard, and project detail

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (`djangorestframework-simplejwt`)
- **Database**: MySQL
- **Frontend**: Django templates + Bootstrap
- **Deployment**: Configurable via `.env`

## Quickstart

1. Clone the repo and set up a virtual environment:
   ```bash
   git clone https://github.com/Wamamili/project_management.git
   cd project_management
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your MySQL credentials, secret key, etc.
   ```

3. Create the database and run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Access the app:
   - API root: `http://127.0.0.1:8000/api/`
   - Admin: `http://127.0.0.1:8000/admin/`
   - Login: `/login/` (session-based)
   - Dashboard: `/dashboard/` (after login)

## API Endpoints

### Accounts
- `POST /api/accounts/register/` — Register
- `POST /api/accounts/login/` — JWT login
- `POST /api/accounts/token/refresh/` — Refresh token
- `GET /api/accounts/me/` — Current user
- `POST /api/accounts/logout/` — Logout (session)
- `GET /dashboard/` — Dashboard (template, login required)

### Projects
- `GET /api/projects/` — List projects for current user
- `POST /api/projects/` — Create project (returns `{ "message": "Project successful created", ...project data... }`)
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

## Templates

- `login.html`, `logout.html`, `dashboard.html` in `templates/`
- `project_detail.html` in `templates/projects/`

## Project Structure

```
project_management/
├── accounts/        # User management, authentication, profiles
├── projects/        # Project models, views, and APIs
├── tasks/           # Task models, views, and APIs
├── project_management/  # Core settings and URLs
├── templates/       # HTML templates (login, logout, dashboard, etc.)
```

## Development & Deployment

- Default timezone: **Africa/Nairobi**
- Custom `User` model with a `role` field:
  ```python
  AUTH_USER_MODEL = "accounts.User"
  ```
- Configurable with `.env` for DB credentials, secret key, and debug mode
- Deployment ready for Heroku, Render, or DigitalOcean

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
POST /api/accounts/login/ → login with username & password
POST /api/accounts/logout/ → logout
GET /api/accounts/dashboard/ → dashboard (auth required)
GET/PUT /api/accounts/profile/ → get/update profile
POST /api/accounts/change-password/ → change password

Session-based login (via api_login + api_logout)
OR JWT-based login (via /api/token/)

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
