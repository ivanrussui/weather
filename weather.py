# import the module
import python_weather
import asyncio

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    # client = python_weather.Client(format=python_weather.IMPERIAL)
    # client = python_weather.Client(format=python_weather.METRIC)
    client = python_weather.Client(format=python_weather.IMPERIAL, locale='ru-RU')

    # fetch a weather forecast from a city
    weather = await client.find("Москва")

    # returns the current day's forecast temperature (int)
    # print(weather.current.temperature)
    celsius = (weather.current.temperature - 32) * 5/9
    print(str(round(celsius)) + '°')
    print(weather.current.sky_text)
    print(weather.location_name)

    # get the weather forecast for a few days
    # for forecast in weather.forecasts:
    #     print(str(forecast.date), forecast.sky_text, forecast.temperature)

    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())
