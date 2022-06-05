import logging
import time
import threading
import random
import json

logger = logging.getLogger(__name__)


class Room(object):
    def __init__(self, max_hot=10, max_cold=10, max_frozen=10, max_overflow=15):
        self.shelves = {
            'hot': Shelves(max_hot),
            'cold': Shelves(max_cold),
            'frozen': Shelves(max_frozen),
        }
        self.overflow_shelf = Shelves(max_overflow)

        self.order_vs_shelf_position = {
            "id": {
                "shelf": self.shelves['hot'],
                "potions": 2,
            }
        }

    def place_order(self, order: dict):
        """
        example of order:   {
            "id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd",
            "name": "Banana Split",
            "temp": "frozen",
            "shelfLife": 20,
            "decayRate": 0.63
        },
        """
        temp = order.get('temp')
        if temp not in self.shelves:
            raise Exception("unknown temp {}".format(temp))

        # check if shelf is full
        shelf = self.shelves[temp]
        if not shelf.is_full():
            logger.info("[normal] - push order [%s] to shelf [%s]", order['name'], temp)
            shelf.push(order)
            return

        # if shelf is full put it to overflow
        if not self.overflow_shelf.is_full():
            logger.info("[overflow], and push order [%s] to overflow", order['name'])
            self.overflow_shelf.push(order)
            return

        logger.info("[shift], overflow is full, finding available shelf now")
        # if overflow is full, find the first available shelves
        for temp, shelve in self.shelves.items():
            if shelve.is_full():
                continue

            shift_order = self.overflow_shelf.pop_order_by_temp(temp)
            if shift_order is not None:
                shelve.push(shift_order)
                self.overflow_shelf.push(order)
                logger.info("[shift], popped order [%s] from overflow, and pushed a new one", temp)
                return

        # if no available shelves, rand pop one from overflow
        removed_order = self.overflow_shelf.put_order_to_existing_position_randomly(order)
        logger.info("[discarded] order id: [%s] from shelf [%s] - %s - total %d[]", removed_order['id'],
                    removed_order['temp'], self.description(), self.count())

    # def pop_order_by_id(self):

    def pick_order(self, order_id):
        order = None
        for shelf in [self.overflow_shelf] + [i for i in self.shelves.values()]:
            if not shelf.is_empty():
                order = shelf.pop_by_id(order_id)
                if order is not None:
                    break
        return order

    def is_empty(self):
        for shelf in [self.overflow_shelf] + [i for i in self.shelves.values()]:
            if not shelf.is_empty():
                return False

        return True

    def get_shelf_by_name(self, name):
        if name == 'overflow':
            return self.overflow_shelf
        return self.shelves.get(name)

    def get_orders_by_shelf(self, name):
        shelf = self.get_shelf_by_name(name)
        if not shelf:
            return []
        return shelf.orders

    def description(self):
        orders = {
            'hot': self.shelves['hot'].orders,
            'cold': self.shelves['cold'].orders,
            'frozen': self.shelves['frozen'].orders,
            'overflow': self.overflow_shelf.orders,
        }
        return json.dumps(orders)

    def count(self):
        n = 0
        for shelf in [self.overflow_shelf] + [i for i in self.shelves.values()]:
            n += len(shelf.orders)
        return n


class FullException(Exception):
    pass


class NotAvailableException(Exception):
    pass


class Shelves(object):
    def __init__(self, max_size):
        self._max_size = max_size
        self._orders = []
        self._lock = threading.Lock()

    def is_full(self):
        return len(self._orders) == self._max_size

    def is_empty(self):
        return len(self._orders) == 0

    def push(self, order: dict):
        with self._lock:
            if self.is_full():
                raise FullException()
            self._orders.append(order)

    def put_order_to_existing_position_randomly(self, order: dict):
        with self._lock:
            if self.is_empty():
                raise NotAvailableException()
            random.seed(time.time())
            index = random.randint(0, len(self._orders) - 1)
            removed_order = self._orders[index]
            self._orders[index] = order
            return removed_order

    def pop(self):
        with self._lock:
            if self.is_empty():
                return None
            return self._orders.pop(0)

    def pop_by_id(self, order_id):
        with self._lock:
            index = -1
            for i, order in enumerate(self._orders):
                if order['id'] == order_id:
                    index = i
            if index == -1:
                return None
            return self._orders.pop(index)

    def pop_random(self):
        with self._lock:
            if self.is_empty():
                return None
            random.seed(time.time())
            return self._orders.pop(random.randint(0, len(self._orders) - 1))

    def pop_order_by_temp(self, temp: str):
        with self._lock:
            for i, v in enumerate(self._orders):
                if v['temp'] == temp:
                    return self._orders.pop(i)
            return None

    @property
    def orders(self):
        return self._orders
