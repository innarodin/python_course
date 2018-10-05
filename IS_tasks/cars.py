from random import randint


class Car:
    CAR_SPECS = {
        'ferrary': {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26},
        'bugatti': {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32},
        'toyota': {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40},
        'lada': {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56},
        'sx4': {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44},
    }

    def __init__(self, name, max_speed, drag_coef, time_to_max):
        self.name = name
        self.max_speed = max_speed
        self.drag_coef = drag_coef
        self.time_to_max = time_to_max

    @classmethod
    def instance(cls, car):
        return cls(
            car,
            cls.CAR_SPECS[car]["max_speed"],
            cls.CAR_SPECS[car]["drag_coef"],
            cls.CAR_SPECS[car]["time_to_max"],
        )


class Weather:
    def __init__(self, max_wind_speed):
        self._wind_speed = randint(0, max_wind_speed)

    @property
    def wind_speed(self):
        return self._wind_speed


class Competition:
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self, distance):
        self._distance = distance

    def set_cars(self, competitors):
        self.competitors = competitors

    def set_weather(self, max_wind):
        weather = Weather(max_wind)
        self.weather = weather

    def start(self):
        results = {}

        for competitor in self.competitors:
            competitor_time = 0

            for distance in range(self._distance):
                if competitor_time == 0:
                    _speed = 1
                else:
                    _speed = (competitor_time / competitor.time_to_max) * competitor.max_speed
                    if _speed > self.weather.wind_speed:
                        _speed -= (competitor.drag_coef * self.weather.wind_speed)
                    if _speed > competitor.max_speed:
                        _speed = competitor.max_speed

                competitor_time += float(1) / _speed

            print("Car <%s> result: %f" % (competitor.name, competitor_time))
            results[competitor.name] = competitor_time

        print("WINNER! {} wins!".format(sorted(results.items(), key=lambda x: x[1])[0][0]))


if __name__ == '__main__':
    cars = ['ferrary', 'bugatti', 'toyota', 'lada', 'sx4']
    competitors = []
    for car in cars:
        car_instance = Car.instance(car)
        competitors.append(car_instance)

    competition = Competition(10000)
    competition.set_cars(competitors)
    competition.set_weather(20)
    competition.start()

