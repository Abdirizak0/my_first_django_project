# my_first_django_project

This is a full-stack blog application built with Django, featuring user authentication, role-based access control, and a RESTful API.

## Features

- User authentication (login, logout, registration)
- Role-based access control (admin, author, reader)
- CRUD operations for blog posts
- Comment system
- RESTful API using Django Rest Framework
- Responsive design using Bootstrap

## Technologies Used

- Python
- Django
- Django Rest Framework
- SQLite (development) / PostgreSQL (production)
- HTML/CSS/JavaScript
- Bootstrap
- Gunicorn (for deployment)

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/django-blog-project.git
   cd django-blog-project
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000` in your browser to see the application.

## Deployment

This project is configured for deployment on Heroku:

1. Create a new Heroku app.
2. Set the following config vars in Heroku:
   - `DJANGO_SECRET_KEY`: Your Django secret key
   - `DJANGO_DEBUG`: Set to 'False'
   - `DJANGO_ALLOWED_HOSTS`: Your app's domain name
3. Add the PostgreSQL addon to your Heroku app.
4. Deploy the code to Heroku.
5. Run migrations on Heroku:
   ```
   heroku run python manage.py migrate
   ```

## Testing

To run the tests, use the following command:

```
python manage.py test
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)