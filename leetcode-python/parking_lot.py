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
        self.TOTAL_MOTORCYCLE = 100
        self.TOTAL_CAR = 100
        self.TOTAL_LARGE = 100

        # key is plate number, value is spot_ids
        self.PARKED_MOTORCYCLE = {}
        self.PARKED_CAR = {}
        self.PARKED_VAN = {}

        self.SPOT_MOTORCYCLE = []
        self.SPOT_CAR = []
        self.SPOT_LARGE = []

        self.TYPE_VS_SPOT = {
            "motorcycle": self.SPOT_MOTORCYCLE,
            "car": self.SPOT_CAR,
            "large": self.SPOT_LARGE
        }
        self.TYPE_VS_CARS = {
            "motorcycle": self.PARKED_MOTORCYCLE,
            "car": self.PARKED_CAR,
            "van": self.PARKED_VAN
        }

    @staticmethod
    def get_position_of_spot(spot_id, spot_list):
        if len(spot_list) == 0:
            return 0

        start = 0
        end = len(spot_list) - 1
        while start < end:
            i = (start + end) // 2
            if spot_id > spot_list[i]:
                start = i + 1
            else:
                end = i - 1

        return start

    @staticmethod
    def put_spot_in_spot_list(spot_id, spot_list):
        index = ParkingLot.get_position_of_spot(spot_id, spot_list)
        return spot_list[:index] + [spot_id] + spot_list[index:]

    @staticmethod
    def pop_spot_from_spot_list(spot_id, spot_list):
        index = ParkingLot.get_position_of_spot(spot_id, spot_list)
        return spot_list[:index] + spot_list[index + 1:]

    def _park_car(self, spot_type, num=1):
        spot = self.type_vs_spot[spot_type]
        if len(spot['available']) < num:
            return False

        i_list = []
        spot_list = []
        for i, j in enumerate(spot['available']):
            if i + num - 1 == j + num - 1:
                i_list.append(i)
                spot_list.append(j)
                num -= 1
            if num == 0:
                break
        if num != 0:
            return False

        spot['available'] = spot['available'][:i_list[0]] + spot['available'][i_list[-1] + 1:]

        position = self.get_position_of_spot(spot['available'][i_list[0]], spot['occupied'])
        spot['occupied'] = spot['occupied'][:position] + spot_list + spot['occupied'][position:]

        return True

    def park_car(self, car_type):
        car_type_vs_parking_lot_types = {
            'motorcycle': [
                {
                    'type': 'motorcycle',
                    'spots': 1,
                },
                {
                    'type': 'car',
                    'spots': 1,
                },
                {
                    'type': 'large',
                    'spots': 1,
                },
            ],
            'car': [
                {
                    'type': 'car',
                    'spots': 1,
                },
                {
                    'type': 'large',
                    'spots': 1,
                },
            ],
            'var': [
                {
                    'type': 'large',
                    'spots': 3,
                },
            ]
        }

        for info in car_type_vs_parking_lot_types[car_type]:
            if self._park_car(info['type'], info['spots']):
                return True
        return False

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
