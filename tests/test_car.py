from datetime import date

from lib.car import *
from lib.tyre import *

# get tyres takes position and then returns details


def test_get_tyre_details():
    car = Car()
    Tyre("Front Right")
    assert car.get_tyre_details("Front Right") == {
        "Front Right": {"pressure": 4, "tread_depth": 3}
    }


# add multiple tyres


def test_add_multiple_tyres():
    car = Car()
    Tyre("Front Right")
    Tyre("Front Left")
    Tyre("Rear Right")
    Tyre("Rear Left")
    assert car.get_all_tyre_details() == {
        "Front Right": {"pressure": 4, "tread_depth": 3},
        "Front Left": {"pressure": 4, "tread_depth": 3},
        "Rear Right": {"pressure": 4, "tread_depth": 3},
        "Rear Left": {"pressure": 4, "tread_depth": 3},
    }


# initialise with history dict


def test_car_initialise_with_history_dict():
    car = Car()
    assert car.history == {}


# test add tyre details to history


def test_history_added_with_date_and_details():
    car = Car()
    Tyre("Front Right")
    Tyre("Front Left")
    Tyre("Rear Right")
    Tyre("Rear Left")
    assert car.add_to_car_history() == {
        date.today().strftime("%Y-%m-%d"): {
            "Front Right": {"pressure": 4, "tread_depth": 3},
            "Front Left": {"pressure": 4, "tread_depth": 3},
            "Rear Right": {"pressure": 4, "tread_depth": 3},
            "Rear Left": {"pressure": 4, "tread_depth": 3},
        }
    }
