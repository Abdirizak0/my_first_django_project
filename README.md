# my_first_django_project

This is a simple blog application built with Django as part of a learning project.

## Features

- User authentication (login/logout)
- Create, Read, Update, and Delete blog posts
- Pagination of blog posts
- Responsive design using Bootstrap

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/my_first_django_project.git
   cd my_first_django_project
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply the database migrations:
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

7. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

- To access the admin panel, go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials.
- To create a new blog post, log in and click on "New Post" in the navigation bar.
- To edit or delete a post, go to the post detail page while logged in as the author of the post.

## Contributing

This is a learning project, but if you'd like to contribute, please feel free to submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).