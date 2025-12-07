# Django News Portal

A simple **Django-based news portal** where users can **sign up, log in, and comment on articles**. Users can create, read, update, and delete articles, and interact with other users through comments.

---

## Features

- **User Authentication**
  - Sign up, log in, and log out
- **Article Management**
  - Create, read, update, and delete articles
- **Comments**
  - Users can comment on articles
- **Clean and responsive UI**
  - Built using Bootstrap for styling

---
## Tech Stack

- **Backend:** Django  
- **Frontend:** Bootstrap, HTML, CSS  
- **Database:** SQLite (default Django database)  
- **Python Version:** 3.12+  
- **Django Version:** 5.0+
---

## Installation

Follow these steps to run the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/AryankaR-hub/django_news_artical.git
   cd django_news_artical
   ```
2.Create a virtual environment:
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  
3.Install dependencies:
  pip install -r requirements.txt
  
4.Apply migrations:
  python manage.py migrate
  
5.Create a superuser (optional, for admin access):
  python manage.py createsuperuser
  
6.Run the development server:
  python manage.py runserver


