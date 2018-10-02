from random import randint


class Car:
    CAR_SPECS = {
        'ferrary': {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26},
        'bugatti': {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32},
        'toyota': {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40},
        'lada': {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56},
        'sx4': {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44},
    }

    def __init__(self, max_speed, drag_coef, time_to_max):
        self.max_speed = max_speed
        self.drag_coef = drag_coef
        self.time_to_max = time_to_max

    @classmethod
    def instance(cls, car):
        return cls(
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

    def start(self, competitors, wind):
        weather = Weather(wind)
        wind_speed = weather.wind_speed
        results = {}

        for competitor_name in competitors:
            competitor_time = 0
            car = Car.instance(competitor_name)

            for distance in range(self._distance):
                if competitor_time == 0:
                    _speed = 1
                else:
                    _speed = (competitor_time / car.time_to_max) * car.max_speed
                    if _speed > wind_speed:
                        _speed -= (car.drag_coef * wind_speed)
                    if _speed > car.max_speed:
                        _speed = car.max_speed

                competitor_time += float(1) / _speed

            print("Car <%s> result: %f" % (competitor_name, competitor_time))
            results[competitor_name] = competitor_time

        print("WINNER!", sorted(results.items(), key=lambda x: x[1])[0][0], "wins!")


cars = ['ferrary', 'bugatti', 'toyota', 'lada', 'sx4']
competition = Competition(10000)
competition.start(cars, 20)  #get competitors and max_wind_speed

