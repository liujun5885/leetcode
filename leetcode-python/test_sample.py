def inc(x):
    return x + 1


def get_position_of_spot(spot_id, spot_list):
    if len(spot_list) == 0:
        return 0

    start = 0
    end = len(spot_list) - 1
    while start <= end:
        i = (start + end) // 2
        if spot_id > spot_list[i]:
            start = i + 1
        else:
            end = i - 1

    return start


def test_answer():
    spot_list = [1, 2, 4, 7, 10, 20]
    assert get_position_of_spot(10, spot_list) == 4
