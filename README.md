
# 🌤️ Django Weather App

A simple Django-based web application to display current weather information and a beautiful city image using the OpenWeatherMap API and Google Custom Search API.

## 🚀 Features

- Get real-time weather details for any city.
- Displays weather description, temperature, and icon.
- Shows a random 1920x1080 image related to the city using Google Custom Search.
- Handles errors gracefully (e.g., when a city is not found).

---

## 📸 Screenshot

![screenshot](screenshot.png)  
<!-- Replace with actual screenshot of your app -->

---

## 🛠️ Tech Stack

- Python 3
- Django
- HTML/CSS
- Bootstrap (optional)
- OpenWeatherMap API
- Google Custom Search JSON API

---

## 🔑 API Keys Setup

1. **OpenWeatherMap**  
   Get an API key from: https://openweathermap.org/api

2. **Google Custom Search**  
   - Create a Search Engine at: https://programmablesearchengine.google.com/
   - Enable Image Search and get the Search Engine ID (CX).
   - Get an API key from: https://console.developers.google.com/apis

---

## ⚙️ Environment Variables (.env)

Create a `.env` file in your project root with the following content:

