"""
# Assumptions:
# - The parking lot can hold motorcycles, cars and vans
# - The parking lot has motorcycle spots, car spots and large spots
# - A motorcycle can park in any spot
# - A car can park in a single compact spot, or a regular spot
# - A van can park, but it will take up 3 regular spots
# - These are just a few assumptions. Feel free to ask your interviewer about more assumptions as needed
#
# Here are a few methods that you should be able to run:
# - Tell us how many spots are remaining
# - Tell us how many total spots are in the parking lot
# - Tell us when the parking lot is full
# - Tell us when the parking lot is empty
# - Tell us when certain spots are full e.g. when all motorcycle spots are taken
# - Tell us how many spots vans are taking up
"""


class ParkingLot(object):
    def __init__(self):
        self.motorcycle = {
            "available": [],
            "occupied": [],
        }
        self.car = {
            "available": [],
            "occupied": [],
        }
        self.large = {
            "available": [],
            "occupied": [],
        }
        self.type_vs_spot = {
            "motorcycle": self.motorcycle,
            "car": self.car,
            "large": self.large
        }

    def get_available_spot(self, spot_type, num=1, is_consecutive=False):
        spot = self.type_vs_spot[spot_type]
        if len(spot['available']) < num:
            return []

        available_spot = spot['available'][:num]
        spot['occupied'].extend(available_spot)
        spot['available'] = spot['available'][num:]

        return available_spot

    def part_car(self, car_type):
        if car_type == "motorcycle":
            spot_ids = self.get_available_spot("motorcycle")

    def remaining_spots(self, spot_type=None):
        return self._spot_num(["available"], [spot_type] if spot_type is not None else None)

    def total_spots(self, spot_type=None):
        return self._spot_num(spots=[spot_type] if spot_type is not None else None)

    def is_full(self, spot_type=None):
        return self._spot_num(["available"], [spot_type] if spot_type is not None else None) == 0

    def is_empty(self, spot_type=None):
        return self._spot_num(["occupied"], [spot_type] if spot_type is not None else None) == 0

    def _spot_num(self, types=None, spots=None):
        if spots is None:
            spots = [self.motorcycle, self.car, self.large]
        if types is None:
            types = ['available', 'occupied']

        total = 0
        for s in spots:
            for t in types:
                total += len(s[t])
        return total


if __name__ == '__main__':
    parking_lot = ParkingLot()
    print(parking_lot.remaining_spots())
    print(parking_lot.total_spots())
    print(parking_lot.is_full())
    print(parking_lot.is_empty())
