# project_management (Django + DRF + JWT + MySQL)

## Quickstart

1. Create and activate a virtualenv, then install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a MySQL database and user, then copy `.env.example` to `.env` and fill values:
   ```bash
   cp .env.example .env
   ```

3. Run migrations and start the server:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

4. Obtain a JWT token:
   - POST `/api/accounts/login/` with `{ "username": "...", "password": "..." }`
   - Use `Authorization: Bearer <access>` in subsequent requests

## API Overview

### Accounts
- `POST /api/accounts/register/` — Register
- `POST /api/accounts/login/` — JWT login
- `POST /api/accounts/token/refresh/` — Refresh token
- `GET /api/accounts/me/` — Current user

### Projects
- `GET /api/projects/` — List projects for current user (owner or member)
- `POST /api/projects/` — Create project (owner = current user)
- `GET /api/projects/<id>/` — Retrieve
- `PUT /api/projects/<id>/` — Update (owner only)
- `DELETE /api/projects/<id>/` — Delete (owner only)
- `POST /api/projects/<id>/add_member/` — Add team member (owner only)

### Tasks
- `GET /api/projects/<project_id>/tasks/` — List tasks in project
- `POST /api/projects/<project_id>/tasks/` — Create task (project member or owner)
- `GET /api/tasks/<id>/` — Retrieve task
- `PUT /api/tasks/<id>/` — Update (assignee or project owner)
- `DELETE /api/tasks/<id>/` — Delete (project owner or task creator)
- `POST /api/tasks/<id>/comment/` — Add comment to task

## Notes
- Default timezone: Africa/Nairobi
- Uses custom `User` model with a `role` field. Remember `AUTH_USER_MODEL=accounts.User`.

