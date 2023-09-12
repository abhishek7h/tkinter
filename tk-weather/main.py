# Import Tkinter and other modules

import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

root = ttkbootstrap.Window(themename="morph")
root.title("Weather App")
root.geometry("400x400")

# Entry widget to enter the name of the city

city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

# Button wdiget to start searching for the weather

search_button = ttkbootstrap.Button(root, text="Enter Location", command="search", bootstyle="warning")
search_button.pack(pady=10)