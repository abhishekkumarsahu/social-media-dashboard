# Social Media Dashboard

## Overview
Social Media Dashboard is a web-based platform built with Django that allows users to fetch and interact with their Facebook and X (formerly Twitter) posts. Users can like, comment, and engage with their social media content directly from the dashboard.

## Features
- **User Authentication**: Signup, login, and profile management.
- **Social Media Integration**: Fetch posts from Facebook and X (Twitter).
- **Post Interactions**: Users can like and comment on posts.
- **Analytics Dashboard**: View key metrics like total posts, likes, and comments.

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/social-media-dashboard.git
cd social-media-dashboard
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root and set up the following:
```ini
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
SOCIAL_AUTH_FACEBOOK_KEY=your_facebook_API_key
SOCIAL_AUTH_FACEBOOK_SECRET=your_facebook_secret_key
SOCIAL_AUTH_TWITTER_KEY=your_twitter_key
SOCIAL_AUTH_TWITTER_SECRET=your_twitter_secret
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
```

### 5. Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### 7. Run the Development Server
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`.

## Usage
1. **Register/Login**: Create an account or log in.
2. **Connect Social Media**: Fetch posts from Facebook and Twitter.
3. **Engage with Posts**: Like and comment on posts.
4. **View Analytics**: See user activity statistics.

## Screenshots

## Project Structure
```
/social_media_dashboard
│── dashboard/                # Main application directory
│   ├── templates/            # HTML templates
│   ├── static/               # Static assets (CSS, JS, Images)
│   ├── models.py             # Database models
│   ├── views.py              # Django views
│   ├── urls.py               # URL routing(app)
│   ├── forms.py              # Forms for user input
│   ├── twitter.py            # Twitter API integration
│   ├── facebook.py           # Facebook API integration
│── social_dashboard/         # Project settings
|   ├── settings.py           # configuration of Django installation
|   ├── urls.py               # URL routing(project)
│── db.sqlite3                # SQLite database (for development)
│── manage.py                 # Django management script
│── requirements.txt          # Dependencies list
│── README.md                 # Project documentation
```

## API Integration
### Fetch Facebook Posts
The platform fetches Facebook posts via the Graph API. Make sure to generate an access token and configure it in the `.env` file.

### Fetch Twitter Posts
Uses Twitter API v2 to retrieve user tweets.

## Deployment
For production, use a robust database like PostgreSQL and configure a WSGI server such as Gunicorn.
```bash
pip install gunicorn
```
Set up an `.env` file and use a cloud service like AWS, DigitalOcean, or Heroku for deployment.

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m 'Add new feature'`.
4. Push to branch: `git push origin feature-name`.
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Contact
For inquiries or contributions, reach out via [abhishek1813051005@gmail.com or GitHub profile].

