from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'hyderabad'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0ca0ce081605356f5e30738979ba0355'
    PARAMS = {'units': 'metric'}

    API_KEY = 'AIzaSyBhz_FvzpMf_GgG3k7dFrMo2MMUIGI7iC0'  #  Google API key here
    SEARCH_ENGINE_ID = '20733f87e50934a15'  #  Search Engine ID here

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    # Default fallback image URL in case image search fails
    image_url = None

    try:
        data = requests.get(city_url).json()
        search_items = data.get("items")
        
        # Check if search_items is a list with at least 2 items
        if search_items and len(search_items) > 1:
            image_url = search_items[1].get('link')
        else:
            image_url = None

    except Exception as e:
        # Log error if you want, or just silently fail
        image_url = None

    try:
        data = requests.get(url, params=PARAMS).json()
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url
        })

    except KeyError:
        messages.error(request, 'Entered data is not available to API')
        day = datetime.date.today()
        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'city': 'indore',
            'exception_occurred': True,
            'image_url': image_url  # fallback image or None
        })
