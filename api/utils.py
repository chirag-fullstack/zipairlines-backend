from decimal import Decimal

from django.conf import settings


class AirplaneUtils(object):
    def __init__(self, airplane):
        self.airplane = airplane

    @property
    def tank_capacity(self):
        return round((Decimal(self.airplane['id']) * Decimal(settings.FIELD_TANK)), 3)

    @property
    def fuel_required(self):
        return round((Decimal(self.airplane_consumption) + Decimal(
            self.per_passenger_consumption * self.airplane['passengers'])), 3)

    @property
    def per_passenger_consumption(self):
        return round((Decimal(self.airplane['passengers']) * Decimal(
            settings.PER_PASSENGER_CONSUMPTION)), 3)

    @property
    def airplane_consumption(self):
        return round((Decimal(self.airplane['id']) * Decimal(
            settings.PER_PLANE_CONSUMPTION)), 3)

    @property
    def per_minute_fuel_consumption(self):
        return round((self.airplane_consumption + self.per_passenger_consumption), 3)

    @property
    def max_fly_minutes(self):
        return round((self.tank_capacity / self.per_minute_fuel_consumption), 3)
