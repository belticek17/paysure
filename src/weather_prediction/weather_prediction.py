import abc
import json
import os
from datetime import datetime


class WeatherModelBase(abc.ABC):
    @abc.abstractmethod
    def get_weather(self, date: datetime.date, city: str) -> [dict]:
        pass


class DummyWeatherModel(WeatherModelBase):
    _BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        with open(os.path.join(self._BASE_DIR, "resources/weather_source.json")) as weather_file_content:
            self.weather_source = json.load(weather_file_content)

    def get_weather(self, date: datetime.date, city: str) -> [dict]:
        try:
            return self.weather_source[str(date)][city]
        except KeyError:
            raise KeyError("No weather information for this combination of date and city")
