from shelf import Room


def test_normal():
    room = Room(2, 2, 3)

    orders = [
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "frozen", "shelfLife": 20,
         "decayRate": 0.63}
    ]
    for order in orders:
        room.place_order(order)

    assert room.get_orders_by_shelf('frozen') == orders
    assert room.get_orders_by_shelf('cold') == []
    assert room.get_orders_by_shelf('hot') == []
    assert room.get_orders_by_shelf('overflow') == []


def test_to_overflow():
    room = Room(max_hot=1, max_cold=1, max_frozen=2, max_overflow=2)

    orders = [
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "frozen", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "frozen", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "frozen", "shelfLife": 20,
         "decayRate": 0.63},
    ]
    for order in orders:
        room.place_order(order)

    assert room.get_orders_by_shelf('frozen') == orders[:2]
    assert room.get_orders_by_shelf('cold') == []
    assert room.get_orders_by_shelf('hot') == []
    assert room.get_orders_by_shelf('overflow') == orders[2:]


def test_to_overflow_pick_out_one():
    room = Room(max_hot=1, max_cold=1, max_frozen=1, max_overflow=2)

    orders = [
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "hot", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "hot", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "frozen", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "frozen", "shelfLife": 20,
         "decayRate": 0.63},
    ]
    for order in orders:
        room.place_order(order)

    assert len(room.get_orders_by_shelf('frozen')) == 1
    assert len(room.get_orders_by_shelf('cold')) == 0
    assert len(room.get_orders_by_shelf('hot')) == 1
    assert len(room.get_orders_by_shelf('overflow')) == 2

    shelf = room.get_shelf_by_name('hot')
    shelf.pop()

    assert len(room.get_orders_by_shelf('frozen')) == 1
    assert len(room.get_orders_by_shelf('cold')) == 0
    assert len(room.get_orders_by_shelf('hot')) == 0
    assert len(room.get_orders_by_shelf('overflow')) == 2

    room.place_order(
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "frozen", "shelfLife": 20,
         "decayRate": 0.63}
    )

    assert len(room.get_orders_by_shelf('frozen')) == 1
    assert len(room.get_orders_by_shelf('cold')) == 0
    assert len(room.get_orders_by_shelf('hot')) == 1
    assert len(room.get_orders_by_shelf('overflow')) == 2


def test_remove_from_overflow():
    room = Room(max_hot=1, max_cold=1, max_frozen=1, max_overflow=2)

    orders = [
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "hot", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "hot", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "hot", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "hot", "shelfLife": 20,
         "decayRate": 0.63},
    ]
    for order in orders:
        room.place_order(order)

    assert len(room.get_orders_by_shelf('frozen')) == 0
    assert len(room.get_orders_by_shelf('cold')) == 0
    assert len(room.get_orders_by_shelf('hot')) == 1
    assert len(room.get_orders_by_shelf('overflow')) == 2


def test_room_pick_order():
    room = Room(max_hot=1, max_cold=1, max_frozen=1, max_overflow=2)

    orders = [
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "hot", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "hot", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "hot", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "cold", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "cold", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "cold", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "frozen", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "frozen", "shelfLife": 20,
         "decayRate": 0.63},
        {"id": "a8cfcb76-7f24-4420-a5ba-d46dd77bdffd", "name": "Banana Split", "temp": "frozen", "shelfLife": 20,
         "decayRate": 0.63},
    ]
    for order in orders:
        room.place_order(order)

    total = room.count()
    assert total == 5
    for order in orders:
        room.pick_order(order['id'])
        total -= 1
        assert room.count() == max(total, 0)

    assert room.is_empty() == True
