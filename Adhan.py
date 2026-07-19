from adhanpy.calculation.CalculationMethod import CalculationMethod
from adhanpy.PrayerTimes import PrayerTimes
from datetime import date, datetime
from geopy.geocoders import Nominatim
from tkinter import Tk, Label, Entry, Button, Frame
from PIL import Image, ImageTk
from zoneinfo import ZoneInfo
from timezonefinder import TimezoneFinder
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

bg_color = "#f5f5ee"
widget_bg_color = "#ffd7ba"

window = Tk()
window.title("Adhan app")
window.geometry("800x500")
window.resizable(False, False)
window.configure(bg=bg_color)
window.wm_iconbitmap(resource_path("app_icons/favicon.ico"))

tf = TimezoneFinder()

geolocator = Nominatim(user_agent="adhan")

prayers = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]

adhan_icon = Image.open(resource_path("app_icons/adhan_icon.png"))
adhan_icon = adhan_icon.resize((200, 200), Image.LANCZOS)
adhan_icon = ImageTk.PhotoImage(adhan_icon)
adhan_icon_label = Label(window, image=adhan_icon, bg=bg_color)
adhan_icon_label.pack(pady=10)

entry = Entry(window, width=35, bg="white", fg="black")
entry.place(relx=0.5, rely=0.5, anchor="center")
entry.config(font=("sans", 23))

result_label = Label(window, text="", bg=bg_color, fg="black", font=("sans", 14), justify="left")
result_label.place(relx=0.5, rely=0.6, anchor="center")

prayer_frame = Frame(window, bg=bg_color)
prayer_frame.pack(pady=90)
# Dictionary to hold each prayer's frame and time label
prayer_widgets = {}
for i, prayer in enumerate(prayers):
    frame = Frame(prayer_frame, bg=widget_bg_color, width=90, height=70, highlightbackground="#fec89a", highlightthickness=2)
    frame.grid(row=0, column=i, padx=10)

    name_label = Label(frame, text=prayer,bg=widget_bg_color, fg="black", font=("free ink", 20,"bold"))
    name_label.pack(pady=(10, 2))

    time_label = Label(frame, text="--:--", bg=widget_bg_color, fg="#333333", font=("sans", 25,"bold"))
    time_label.pack()

    prayer_widgets[prayer] = time_label


def get_prayer_times():
    city = entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")   
        prayer_widgets["Fajr"].config(text="--:--")
        prayer_widgets["Dhuhr"].config(text="--:--")
        prayer_widgets["Asr"].config(text="--:--")
        prayer_widgets["Maghrib"].config(text="--:--")
        prayer_widgets["Isha"].config(text="--:--")
        return

    try:
        location = geolocator.geocode(city)
        if location is None:
            result_label.config(text="City not found. Please enter a valid city name.")
            return
        
        coords = (location.latitude, location.longitude)
        tz_name = tf.timezone_at(lat=location.latitude, lng=location.longitude)
        local_zone = ZoneInfo(tz_name)

        today = date.today()

        prayer_times = PrayerTimes(coords, today, CalculationMethod.MOON_SIGHTING_COMMITTEE,time_zone=local_zone)

        prayer_widgets["Fajr"].config(text=prayer_times.fajr.strftime('%H:%M'))
        prayer_widgets["Dhuhr"].config(text=prayer_times.dhuhr.strftime('%H:%M'))
        prayer_widgets["Asr"].config(text=prayer_times.asr.strftime('%H:%M'))
        prayer_widgets["Maghrib"].config(text=prayer_times.maghrib.strftime('%H:%M'))
        prayer_widgets["Isha"].config(text=prayer_times.isha.strftime('%H:%M'))

        result_label.config(text=location.address)

    except Exception as e:
          result_label.config(text=f"Error: {str(e)}")


search_button = Button(window, text="⌕", bg="white", fg="gray", font=("sans", 16), width=3, height=1, command=get_prayer_times)
search_button.place(relx=0.85, rely=0.5, anchor="center")

entry.bind("<Return>", lambda event: get_prayer_times())

window.mainloop()