from lib.tyre import Tyre

# Initialise with position


def test_initialise_with_position():
    front_right = Tyre("Front Right")
    assert front_right.position == "Front Right"


# Initialise with pressure and tread_depth


def test_initialise_details_dict():
    front_right = Tyre("Front Right")
    assert front_right.details.get("pressure") == 4
    assert front_right.details.get("tread_depth") == 3


# get tyre details


def test_get_tyre_details():
    front_right = Tyre("Front Right")
    assert front_right.get_details() == {
        "Front Right": {"pressure": 4, "tread_depth": 3}
    }


