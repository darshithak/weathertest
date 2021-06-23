import requests, json

CITY = input("Enter city name: ")
API_KEY = "38089eef75e8f952e99eceba9d6d2c13"
URL = "https://api.openweathermap.org/data/2.5/weather?" + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)

if response.status_code == 200:
   data = response.json()
   main = data['main']
   temperature = main['temp']
   humidity = main['humidity']
   pressure = main['pressure']
   sys = data['sys']
   sunrise = sys['sunrise'] 
   sunset = sys['sunset'] 
   report = data['weather']
   file1 = open("Whether.txt","w+")
   file1.write("* " + CITY + " *" + "\n")
   file1.write("Temperature: "+ str(temperature) + "\n")
   file1.write("Humidity: "+ str(humidity) + "\n")
   file1.write("Pressure: "+ str(pressure) +" \n")
   file1.write("Weather Report: "+ str(report[0]['description']) +" \n")
   file1.write(f"Sunrise: {sunrise} \n")
   file1.write(f"Sunset: {sunset} \n")
   print("Data succesfully written to the file..")
else:
   print("Error in fetching data")