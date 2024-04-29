from weather_forecast import WeatherForecast 

def main():
    weather_app = WeatherForecast()
    while True:
        try:
            city = input("Enter a city to get its weather forecast or exit to quit")
            if city.lower() == "exit":
                break
            weather_app.display_weather(city)
        except Exception as e:
            print('An error occured:', e)
            
if __name__ == "__main__":
    main()