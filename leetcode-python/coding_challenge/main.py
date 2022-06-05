from argparse import ArgumentParser
import logging
import time
from threading import Thread, Event

from shelf import Room
from worker import consumer, producer

logger = logging.getLogger(__name__)


def get_arguments():
    parser = ArgumentParser(description="Code Challenge")
    parser.add_argument("--debug", dest="debug", default=False, action="store_true", help="Enable debug")
    parser.add_argument("--input", dest="input", help="the path of raw data of order", required=True)
    parser.add_argument("--couriers", dest="couriers", help="the number of couriers will run on parallel",
                        type=int, default=1, required=False)
    parser.add_argument("--orders", dest="orders", help="the number of orders, it will produce every second",
                        type=int, default=2, required=False)
    return parser.parse_args()


def init(args):
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(process)s - %(thread)s - [%(filename)s:%(lineno)s - %(funcName)s()] - %(message)s",
        level=logging.DEBUG if args.debug else logging.INFO)


def main(args):
    room = Room()

    event = Event()

    now = time.time()
    time.sleep(1)
    logger.debug("input file: [%s]", args.input)
    threads = []

    t = Thread(target=producer, args=(args, room, event))
    threads.append(t)
    t.start()

    logger.debug("total couriers [%s]", args.couriers)
    for i in range(args.couriers):
        t = Thread(target=consumer, args=(room, event))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    logger.info("Bye Bye!, spend total [%f]", time.time() - now)


if __name__ == '__main__':
    args = get_arguments()
    init(args)
    main(args)
