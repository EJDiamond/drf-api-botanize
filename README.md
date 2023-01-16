# Botanize - API

The backend API section of my Botanize sharing platform project is powered by the Django Rest Framework which supports the ReactJS frontend section

[View deployed backend](https://botanize-api.herokuapp.com/)


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
2. Install django using:
```
pip3 install 'django<4'
```
3. Create a django project using:
```
django-admin startproject drf_api .
```
4. Install Cloudinary library using:
```
pip install django-cloudinary-storage
```
5. Install Pillow image library (capital P):
```
pip install Pillow
```
6. Add the new apps to ```settings.py``` (the order is important):
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