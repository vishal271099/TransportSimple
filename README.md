# TransportSimple

This project is a simple clone of the Quora platform using Django. It includes features like user registration, login, logout, adding questions, answering questions, and liking answers.

Table of Contents
Installation

Setup
Usage
Features
Technologies Used
Contributing
License
Installation
Follow the steps
 below to set up the project on your local machine:

Clone the repository

bash
Copy
git clone https://github.com/yourusername/QuoraProject.git
cd QuoraProject
Create a virtual environment

It's recommended to use a virtual environment to manage your project dependencies:

bash
Copy
python3 -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install required dependencies

Install the required Python packages using pip:

bash
Copy
pip install -r requirements.txt
Configure your database

Ensure your database is set up correctly. For example, if you're using SQLite (default for Django), no additional configuration is required. If you're using a different database like PostgreSQL, MySQL, etc., ensure your settings in settings.py are properly configured.

Run the following command to apply database migrations:

bash
Copy
python manage.py migrate
Create a superuser (optional)

You can create a superuser to manage the application via Django's admin panel:

bash
Copy
python manage.py createsuperuser
Run the development server

Finally, run the Django development server:

bash
Copy
python manage.py runserver
You can now access the project in your browser at http://127.0.0.1:8000.

Setup
The following settings are required to run the project:

STATIC_URL and MEDIA_URL settings in settings.py should be correctly configured for static and media files.

Make sure to add django.contrib.auth in INSTALLED_APPS in settings.py for user authentication.

Usage
Registration, Login, and Logout
Registration: Users can register with their email and password.

Login: After registration, users can log in using their credentials.

Logout: Users can log out of the application.

Add Question
Users can add a question to the platform. A question has a title and a description.

Go to the home page.

Click on the "Add Question" button.

Fill in the title and description, then submit the form.

Answer Question
After a question is created, users can add answers to the questions.

Go to the question detail page.

Click on the "Add Answer" button.

Fill in the answer and submit it.

Like Answer
Users can like answers to show appreciation.

On the question detail page, click on the "Thumbs Up" button next to an answer to like it.

The like count will update.

Features
User Authentication: Register, login, and logout functionality.

Question Management: Users can add, view, and interact with questions.

Answering: Users can answer questions.

Like Answers: Users can like answers to show appreciation.

Responsive Design: The application is responsive and works on both desktop and mobile devices.

Technologies Used
Django: Python web framework for building the backend.

SQLite (or any other database you prefer): Database for storing users, questions, answers, and likes.

HTML/CSS/JavaScript: For the frontend interface.

Font Awesome: For icons (e.g., thumbs up for like button).

Bootstrap (optional): For responsive design.

Contributing
Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -am 'Add your feature').

Push to the branch (git push origin feature/your-feature-name).

Create a new Pull Request.

We welcome contributions to enhance the functionality and improve the project.

License
This project is open-source and available under the MIT License.