from weather_fetcher import WeatherDataFetcher
from user_interface import UserInterface
from data_parser import DataParser

def main():
    weather_fetcher = WeatherDataFetcher()
    data_parser = DataParser()
    user_interface = UserInterface(weather_fetcher, data_parser)


    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            forecast = user_interface.get_detailed_forecast(city)
        else:
            forecast = user_interface.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()
