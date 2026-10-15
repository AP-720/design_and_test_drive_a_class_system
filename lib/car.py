from datetime import date

from lib.tyre import *


class Car:
    def __init__(self):
        self.history = {}

    def get_tyre_details(self, position):
        tyre = Tyre(position)
        return tyre.get_details()

    def get_all_tyre_details(self):
        positions = ["Front Right", "Front Left", "Rear Right", "Rear Left"]
        result = {}

        for position in positions:
            result.update(self.get_tyre_details(position))

        return result

    def add_to_car_history(self):
        todays_date = date.today().strftime("%Y-%m-%d")
        print({todays_date: self.get_all_tyre_details()})
        return {todays_date: self.get_all_tyre_details()}
