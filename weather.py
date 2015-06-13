import Tkinter as tk
import requests
import ast
from PIL import Image, ImageTk
from StringIO import StringIO

#setting labels that show data global
global longitudeLbl2, latitudeLbl2, temperatureLbl2, humidityLbl2, pressureLbl2, windSpeedLbl2, windDirLbl2, weatherDescriptionLbl2, weatherMainLbl2

#get the weather stats based on the provided location
def getWeather(locationEnt, mn):
    req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+locationEnt.get()+'&type=like&units=imperial')
    #remove brackets from response text so it can be translated to dictionary
    reqText = req.text.replace('[', '').replace(']', '')
    #translate the response text value to a dictionary
    reqDict = ast.literal_eval(reqText)
    #retrieve icon image
    img_file = requests.get('http://openweathermap.org/img/w/'+str(reqDict['weather']['icon'])+'.png')
    webImage = Image.open(StringIO(img_file.content))
    #store image width/height
    imgwidth, imgheight = webImage.size

    #update labels
    longitudeLbl2.config(text=reqDict['coord']['lon'])
    latitudeLbl2.config(text=reqDict['coord']['lat'])
    temperatureLbl2.config(text=reqDict['main']['temp'])
    humidityLbl2.config(text=reqDict['main']['humidity'])
    pressureLbl2.config(text=reqDict['main']['pressure'])
    windSpeedLbl2.config(text=reqDict['wind']['speed'])
    windDirLbl2.config(text=reqDict['wind']['deg'])
    weatherDescriptionLbl2.config(text=reqDict['weather']['description'])
    weatherMainLbl2.config(text=reqDict['weather']['main'])
    
    
    #create canvas and show the icon
    #NOTE - this is creating duplicates on each button press, bad practice
    iconCanvas = tk.Canvas(mn, width=imgwidth, height=imgheight)
    photo = ImageTk.PhotoImage(webImage)
    iconCanvas.create_image(imgwidth/2, imgheight/2, image=photo)
    iconCanvas.image = photo #NOTE - seems garbage collection discards the image and shows blank without this
    iconCanvas.grid(row=13, column=2, rowspan=2, columnspan=2)
    
    
#create main window    
main = tk.Tk()
main.title("Weather")
main.geometry("320x380")

#create gui objects
#NOTE - For some reason trying to place these objects on the main form in the same line they are created in causes
#NOTE - the variables to reference NoneType objects, so the grid placement was done at the end.
locationLbl = tk.Label(main, text="Enter Location:")
locationEntry = tk.Entry(main)
longitudeLbl = tk.Label(main, text="Longitude: ")
latitudeLbl = tk.Label(main, text="Latitude: ")
temperatureLbl = tk.Label(main, text="Temperature (F): ")
humidityLbl = tk.Label(main, text="Humidity: ")
pressureLbl = tk.Label(main, text="Atmospheric Pressure: ")
windSpeedLbl = tk.Label(main, text="Wind Speed (mph): ")
windDirLbl = tk.Label(main, text="Wind Direction (deg): ")
weatherDescriptionLbl = tk.Label(main, text="Weather Description: ")
weatherMainLbl = tk.Label(main, text="Current Condition: ")
#create blank result labels
longitudeLbl2 = tk.Label(main, text="")
latitudeLbl2 = tk.Label(main, text="")
temperatureLbl2 = tk.Label(main, text="")
humidityLbl2 = tk.Label(main, text="")
pressureLbl2 = tk.Label(main, text="")
windSpeedLbl2 = tk.Label(main, text="")
windDirLbl2 = tk.Label(main, text="")
weatherDescriptionLbl2 = tk.Label(main, text="")
weatherMainLbl2 = tk.Label(main, text="")

showButton = tk.Button(main, text="Get Weather", command=lambda:getWeather(locationEntry, main))

#place gui objects
#objects that show text
locationLbl.grid(row=1, column=1, columnspan=2)
locationEntry.grid(row=1, column=3, columnspan=2)
showButton.grid(row=2, column=2, columnspan=2)
longitudeLbl.grid(row=4, column=1, columnspan=2)
latitudeLbl.grid(row=5, column=1, columnspan=2)
temperatureLbl.grid(row=6, column=1, columnspan=2)
humidityLbl.grid(row=7, column=1, columnspan=2)
pressureLbl.grid(row=8, column=1, columnspan=2)
windSpeedLbl.grid(row=9, column=1, columnspan=2)
windDirLbl.grid(row=10, column=1, columnspan=2)
weatherDescriptionLbl.grid(row=11, column=1, columnspan=2)
weatherMainLbl.grid(row=12, column=1, columnspan=2)
#result labels that show no text initially
longitudeLbl2.grid(row=4, column=3, columnspan=2)
latitudeLbl2.grid(row=5, column=3, columnspan=2)
temperatureLbl2.grid(row=6, column=3, columnspan=2)
humidityLbl2.grid(row=7, column=3, columnspan=2)
pressureLbl2.grid(row=8, column=3, columnspan=2)
windSpeedLbl2.grid(row=9, column=3, columnspan=2)
windDirLbl2.grid(row=10, column=3, columnspan=2)
weatherDescriptionLbl2.grid(row=11, column=3, columnspan=2)
weatherMainLbl2.grid(row=12, column=3, columnspan=2)

main.mainloop()