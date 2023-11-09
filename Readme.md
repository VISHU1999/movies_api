# My Movie List API Project

- This is a small project that fetches film data from the "Ghibli API" (https://ghibliapi.vercel.app/films), processes the data, and provides a Movies List API. It also includes user registration and login functionality as we are using token authentication for our list API

- Pre-commit Integration: Pre-commit hooks are set up to enforce code quality standards and formatting guidelines.

## Use of asyncio
The project utilizes asyncio to efficiently send people API requests in parallel, making it possible to hit multiple API endpoints simultaneously. This improves the speed of fetching data from external sources.

## Caching Behavior

- When the Movies List API is accessed for the first time, it may take some time to fetch and process the film data. Subsequent requests within the same minute will return the cached data for improved performance.

- After 1 minute, the project will automatically re-fetch the film data from the Ghibli API to ensure the content is up-to-date.

## Project Overview

The project has the following main components:

- **Movies List API:** It fetches film data from the Ghibli API and replaces people URLs with actual values, providing a Movies List API. The data is cached for 1 minute to improve performance.

- **User Registration and Login:** The project includes user registration and login endpoints that use token authentication. Registered users can obtain a token to access protected resources.

## Installation and Usage

1. Clone the project repository:

   ```bash
   git clone

   pip install -r requirements.txt

   python manage.py migrate

   python manage.py runserver
   ```
2. Curl Example how we call movies API
   ```bash
   curl --location --request GET 'http://127.0.0.1:8000/movies/' \
   --header 'Authorization: ghiblikey c47352c34df5ba5c15165b8f2502cd0b51dfee91' \
   --header 'Cookie: csrftoken=HVyEEzU8kKlK9fHd7ocysaXirQIdAIHU'
   ```
