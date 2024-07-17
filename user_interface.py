class UserInterface:
    def __init__(self, weather_fetcher, data_parser):
        self.weather_fetcher = weather_fetcher
        self.data_parser = data_parser


    def get_detailed_forecast(self, city):
        data = self.weather_fetcher.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)

    def display_weather(self, city):
        data = self.weather_fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.data_parser.parse_weather_data(data)
            print(weather_report)
            return weather_report
