# Botanize - API

The backend API section of my Botanize sharing platform project is powered by the Django Rest Framework which supports the ReactJS frontend section

- [View deployed backend](https://botanize-api.herokuapp.com/)
- [View front end delpoyed](https://botanize.herokuapp.com/)
- [Front end repository](https://github.com/EJDiamond/botanize)


# Table of contents
1. [Database Structure](#database-structure)
2. [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Manual Testing](#manual-testing)
    - [Bugs](#bugs)
3. [Technologies](#technologies)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programs](#-frameworks-Libraries-programs)
4. [Inital Project Setup](#initial-project-setup)
5. [Deployment](#deployment)
    - [JSON Web Tokens](#json-web-tokens)
    - [Prepare API for Heroku deployment](#prepare-api-for-heroku-deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Bug Fix dj-rest-auth](#bug-fix-dj-rest-auth)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

# Database Structure

![Database](/static/database.png)

# Testing

## Validator Testing

All code was put through the [PEP8](https://pep8ci.herokuapp.com/) validator, where all but the drf_api > settings.py file passed. The results are shown below.

![Settings validator PEP8 results ](/static/pep8_drf_api_settings.png)

The problematic lines of code where not changed as I felt it affected the readability of the code.

Below are the results of the Bookmarks app showing no errors:

![Bookmarks Models PEP8 results](/static/pep_8_bookmarks_models.png)
![Bookmarks Serializers PEP8 results](/static/pep8_bookmarks_serializers.png)
![Bookmarks Views PEP8 results](/static/pep8_bookmarks-views.png)

## Manual Testing

1. Previewed each url and ensured all opened with no errors found.
2. Checked the search and filter features work for the Posts and Profiles, in both the development environment and the deployed app.
3. Ensured the CRUD functionality is in place and working for the Profiles, Posts, Bookmarks, Answers, Following and Likes apps. This was done using the following steps in both the develpoment environment and the deployed app:
    - Creating a new item.
    - Opening the new item URL path
    - Ensuring the counts where incrementing (Followers, Following, Posts, Likes)
    - Updating items (Profiles, Posts and Answers)
    - Deleting items (Posts, Bookmarks, Answers and Likes)

## Bugs

Yet to find any bugs.

# Technologies

## Languages

- Python

## Frameworks, Libraries and Programs

- DrawSQL - used to plan out database tables and how they are linked to one another.
- Django
- Django RestFramework
- Cloudinary
- Pillow
- Django Rest Auth
- Cors Headers
- Heroku
- ElephantSQL

# Initial Project Setup

1. Using Code Institutes Template, create a Github Repository.
2. Install django using the following command in the terminal
    ```
    pip3 install 'django<4'
    ```
3. Create a django project
    ```
    django-admin startproject drf_api .
    ```
4. Install Cloudinary library
    ```
    pip install django-cloudinary-storage
    ```
5. Install Pillow image library (capital P)
    ```
    pip install Pillow
    ```
6. Add the new apps to ```settings.py``` (the order is important)
    ```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'cloudinary_storage',
        'django.contrib.staticfiles',
        'cloudinary',
    ]
    ```
7. Create an ```env.py``` file in the project's top directory.
8. Add cloudinary URL to ```env.py```:
    ```
    import os
    os.environ["CLOUDINARY_URL"] = "cloudinary://API KEY HERE"
    ```
9. Add cloudinary credentials to the ```settings.py```:
    ```
    import os

    if os.path.exists('env.py'):
        import env

    CLOUDINARY_STORAGE = {
        'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
    }
    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    ```

# Deployment

## JSON web tokens

1. Install the Django rest authentication library
    ```
    pip install dj-rest-auth
    ```
2. Add the following to the ```setting.py``` file
    ```
    'rest_framework.authtoken',
    'dj_rest_auth',
    ```
3. In the main app ```urls.py```` add the rest url to the urlpatterns list
    ```
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    ```
4. Migrate the database using the following command in the terminal
    ```
    python manage.py migrate
    ```
5. Adding feature to be allow userst to register
    ```
    pip install 'dj-rest-auth[with_social]'
    ```
6. In ```settings.py``` add the following to installed apps below ```'dj_rest_auth',```
    ```
     'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    ```
7. In ```settings.py``` add the site id below the installed apps
    ```SITE_ID = 1```
8. In the main app ```urls.py```` add the registration urls to the urlpatterns list
    ```
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    ```
9. Install the JSON tokens
    ```
    pip install djangorestframework-simplejwt
    ```
10. In ```env.py``` set DEV to 1 (checks whether in development)
    ```
    os.environ['DEV'] = '1'
    ```
11. In ```settings.py``` under ```SITE_ID``` add if statement to check if in devolopment or production.
    ```
    ​​REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    ```
12. In ```settings.py``` add the following below above step, to enable token authentication, ensure tokens are sent to HTTPS only and to declare the cookie names for the access and refresh tokens
    ```
    REST_USE_JWT = True # enables token authentication
    JWT_AUTH_SECURE = True # tokens sent over HTTPS only
    JWT_AUTH_COOKIE = 'my-app-auth' #access token
    JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' #refresh token
    ```
13. Create a ```serializers.py``` file in the outer most level of the ```DRF_API_BOTANIZE```
14. Insert the Django documentation USERDETAILSERIALIZERS into the ```serializers.py``` just created
    ```
    from dj_rest_auth.serializers import UserDetailsSerializer
    from rest_framework import serializers


    class CurrentUserSerializer(UserDetailsSerializer):
        """Serializer for Current User"""
        profile_id = serializers.ReadOnlyField(source='profile.id')
        profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """Meta class to to specify fields"""
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
    ```
15. Overwrite the default USer Detail Serializer in ```settings.py```
    ```
    REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
    }
    ```
16. Run migrations
    ```
    python manage.py migrate
    ```
17. Update the requirements file with new installed apps.
    ```
    pip freeze > requirements.txt
    ```
18. Save, add, commit and push to Github

## Prepare API for Heroku deployment

1. In DRF-API_BOTOANIZE create a ```views.py``` file
2. Import the api_view  decorator and the Response class
    ```
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    ```
3. Create the root_route and return  a Response with a custom message.
    ```
    @api_view()
    def root_route(request):
    return Response({
        "message": "Botanize API"
    })
    ```
4. import it the ```drf_api/urls.py``` file and add it to the urlpatterns list
    ```
    from .views import root_route

    urlpatterns = [
    path('', root_route),
    ```
5. Set up page pagination in ```settings.py``` inside REST_FRAMEWORK
    ```
    REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
    'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    }
    ```
6. In ```settings.py```set the default renderer to JSON for the production environment
    ```
    if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
    ```
7. Under PAGE_SIZE in ```settings.py``` make the date for CREATED_ON readable
    ```
    'DATETIME_FORMAT': '%d %b %y',
    ```
8. Save, add, commit and push to Github

## Heroku Deployment

1. Login to Heroku and on the dashboard select create new app
3. Login to ElephantSQL and create a new instance, selecting tiny turtle plan and the region. Got to the URL section and copy the database URL.
2. Back in Heroku, in the settings tab, reveal Config Vars and add DATABASE_URL with the value set to the databse URL from ELEPHANTSQL.
3. Back in the Gitpod workspace, install dj_database_url and psycopg2
    ```
    pip install dj_database_url_psycopg2
    ```
4. In ```settings.py``` under import os add
    ```
    import dj_database_url
    ```
5. In ```settings.py``` update the DATABASES section to allow for development to use the sqlite database and the deployed version, the ElephantSQL
    ```
    if 'DEV' in os.environ:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    else:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
        }
    ```
6. In ```env.py``` add a new environment variable with the key set to DATABASE_URL, and the value to the ElephantSQL database URL.
    ```
    os.environ.setdefault("DATABASE_URL", "<your PostgreSQL URL here>")
    ```
7. Comment out the DEV environment variable (temporary so Gitpod can connect to ElephantSQL database)
    ```
    # os.environ['DEV'] = '1'
    ```
8. Migrate the database models to the new database
    ```
    python3 manage.py migrate
    ```
9. Create a superuser for the new database using the following terminal command and adding a username and password.
    ```
    python3 manage.py createsuperuser
    ```
10. Install Gunicorn library
    ```
    pip install gunicorn
    ```
11. Update the requirements.txt
    ```
    pip freeze --local > requirements.txt
    ```
12. Create a Profile and add the following two commands
    ```
    release: python manage.py makemigrations && python manage.py migrate
    web: gunicorn drf_api.wsgi
    ```
13. In ```settings.py``` update value of ALLOWED_HOSTS
    ```
    ALLOWED_HOSTS = ['localhost', 'botanize-api.herokuapp.com']
    ```
14. Add corsheaders to INSTALLED_APPS
    ```
    'corsheaders',
    ```
15. In ```settings.py` at the top of the MIDDLEWARE section add
    ```
    'corsheaders.middleware.CorsMiddleware',
    ```
16. Beneath the MIDDLEWARE set the allowed origins for network requests made to the server
    ```
    if 'CLIENT_ORIGIN' in os.environ:
        CORS_ALLOWED_ORIGINS = [
            os.environ.get('CLIENT_ORIGIN'),
            os.environ.get('CLIENT_ORIGIN_DEV')
        ]

    else:
        CORS_ALLOWED_ORIGIN_REGEXES = [
            r"^https://.*\.gitpod\.io$",
        ]
    CORS_ALLOW_CREDENTIALS = True
    ```
17. In ```settings.py``` set jwt samesite to none to ensure the cookies are not blocked
    ```
    JWT_AUTH_SAMESITE = 'None'
    ```
18. In ```settings.py``` replace the secret value
    ```
    SECRET_KEY = os.getenv('SECRET_KEY')
    ```
20. In ```env.py``` set your secret key to a random key
    ```
    os.environ['SECRET_KEY'] = 'random value here'
    ```
21. Change DEBIG from True
    ```
    DEBUG = 'DEV' in os.environ
    ```
22. Comment back DEV = 1 in ```env.py```
    ```
    import os

    os.environ['CLOUDINARY_URL'] = "cloudinary://..."
    os.environ['SECRET_KEY'] = "Z7o..."
    os.environ['DEV'] = '1'
    os.environ['DATABASE_URL'] = "postgres://..."
    ```
23. Update the requirements.txt
    ```
    pip freeze --local > requirements.txt
    ```
24. Save, add, commit and push to Github
25. Back in the settings tab of the Heroku app, add the SECRET_KEY and CLOUDINARY_URL keys with values copied from the ```env.py``` file
26. Add DISABLE_COLLECTSTATIC = 1 to the config vars.
27. Open the deploy tab on the Heroku dashboard and under deployment method select connect to Github and select the project repository.
28. In the manual deploy section selct deploy branch.
29. Once built an open app button will appear, this is clicked to view the deployed app.

## Bug Fix dj-rest-auth

Below is the fix for the bug which doesn't allow users to log out.

1. In drf_api ```views.py``` import JWT_AUTH from ```settings.py```
    ```
    from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
    JWT_AUTH_SECURE,
    ```
2. Create a logout view which sets the value of both the access token (JWT_AUTH_COOKIE) and refresh token (JWT_AUTH_REFRESH_COOKIE) to empty strings. Pass in samesite to none and makes sure the cookies are http only and sent over HTTPS.
    ```
    @api_view(['POST'])
    def logout_route(request):
        response = Response()
        response.set_cookie(
            key=JWT_AUTH_COOKIE,
            value='',
            httponly=True,
            expires='Thu, 01 Jan 1970 00:00:00 GMT',
            max_age=0,
            samesite=JWT_AUTH_SAMESITE,
            secure=JWT_AUTH_SECURE,
    )
        response.set_cookie(
            key=JWT_AUTH_REFRESH_COOKIE,
            value='',
            httponly=True,
            expires='Thu, 01 Jan 1970 00:00:00 GMT',
            max_age=0,
            samesite=JWT_AUTH_SAMESITE,
            secure=JWT_AUTH_SECURE,
    )
    return response
3. In the main ```urls.py``` import the logout route
    ```
    from .views import root_route, logout_route
    ```
4. Add it to the main url patterns above the default dj-rest-auth url
    ```
    path('dj-rest-auth/logout/', logout_route),
    ```
5. Save, add, commit and push to Github
6. Manually deploy the project again and use open app to view the deployed site.

# Credits

- The DRF-API walkthrough project was used to set up this project, modifications were made to customise including adding models, serializers and views to allow users to like answers given by other users and to bookmark post of interest.