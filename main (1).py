import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
def get_image():
  global img, image_Label
  icon_url = f"https://openweathermap.org/img/wn/{icon}@2x.png"
  response = requests.get(icon_url)
  image = Image.open(BytesIO(response.content))
  img = ImageTk.PhotoImage(image)
  image_Label.config(image=img)
  image_Label.pack(side = "bottom", fill = "both", expand = "yes")

def get_weather():
  global icon
  city = city_entry.get()
  password = "d872258c216b817fb79e5d07d9934231"
  weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={password}")
  if weather.json()["cod"] == "404":
    result_Label.config(text=f"No city found with the name {city}")
  else:
    result_Label.config(text=f"the weather in "+city+" is "+str(weather.json()["weather"][0]["description"])+" with a temperature of "+str(weather.json()["main"]["temp"])+" degrees Fahrenheit")

  icon = weather.json()["weather"][0]["icon"]
  get_image()
    


pinecone = tk.Tk()
pinecone.title("Pinecone")
tk.Label(pinecone, text="Enter a city").pack()
city_entry = tk.Entry(pinecone)
city_entry.pack()
tk.Button(pinecone, text="Get Weather", command=get_weather).pack()
image_Label = tk.Label(pinecone)
image_Label.pack_forget()
result_Label = tk.Label(pinecone, text="result")
result_Label.pack()
pinecone.mainloop()