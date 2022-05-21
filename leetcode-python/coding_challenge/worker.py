import json
import logging
import time
from threading import Event
import random

from shelf import Room
from queue import PriorityQueue
import settings

logger = logging.getLogger(__name__)

queue = PriorityQueue()


def producer(args, room: Room, event: Event):
    try:
        with open(args.input) as fp:
            orders = json.load(fp)
            for order in orders:
                room.place_order(order)
                time.sleep(1 / args.orders)
                logger.info("[received] order id [%s] order [%s] to shelves [%s], total: %d",
                            order['id'], order['temp'], room.description(), room.count())

                sleep_seconds = random.randint(*settings.COURIER_RANDOM_RANGE)
                time_stamp = time.time() + sleep_seconds
                #     Entries are typically tuples of the form:  (priority number, data).
                queue.put((time_stamp, {"order_id": order['id'], "sleep_seconds": time_stamp}))

            # set event to let consumer stop
            logger.info("[producer] produced all orders [%d], total [%d] in room", len(orders), room.count())
    finally:
        event.set()


def consumer(room: Room, event: Event):
    random.seed(time.time())
    while True:
        if not event.is_set() and queue.empty():
            continue

        priority, data = queue.get()
        logger.info("[debug] %s, %s", priority, data)

        order_id = data['order_id']
        random_second = data["sleep_seconds"] - time.time()
        if random_second > 0:
            time.sleep(random_second)

        logger.info("[consumer] [picked_up] order [%s]", order_id)
        order = room.pick_order(order_id)

        if order:
            logger.info("[consumer] [picked_up] order [%s] from shelf[%s], [%s], left: %d",
                        order['name'], order['temp'], room.description(), room.count())

        # if producer stopped and there is no order in shelves, exist
        if event.is_set() and room.is_empty():
            logger.info("[consumer] finished all jobs")
            break
