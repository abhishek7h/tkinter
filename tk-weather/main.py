# Import Tkinter and other modules
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

# Function to get weather from OpenWeatherMap.org API


def get_weather(city):
    API_key = "986b29fcfda6b87b7e6aca64adf3e080"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error 404", "City not found")
        return None

    # Parse the response JSON to get weather data
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    # Get the icon URL and all weather data
    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# Function to search weather for location


def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    # If the city is found, unpack the data
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    # Get the weather icon image from the URL and update it
    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    # Update the temperature and description labels
    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")


root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

# Entry widget to enter the name of the city
city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# Button wdiget to start searching for the weather
search_button = ttkbootstrap.Button(
    root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# Label widget to display the location's name
location_label = ttkbootstrap.Label(root, font="Helvetica, 25")
location_label.pack(pady=20)

# Label widget to display the weather icons
icon_label = tk.Label(root)
icon_label.pack()

# Label widget to show the temperature
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

# Label widget to show the weather description
description_label = tk.Label(root, font="Helvetica, 20")
description_label.pack()

root.mainloop()
