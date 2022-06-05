# required envs:

> Python3.9, pipenv

## if you haven't installed Python, see following to install it:

> https://www.python.org/downloads/

## if you haven't installed pipenv, see following to install it:

> pip install pipenv

# init running env

## 1. go to code folder

## 2. run following command to init env

```shell
pipenv shell
```

## 3. install requied packages

```shell
pipenv install --skip-lock
```

## 4. run command with help

```shell
python main.py -h
usage: main.py [-h] [--debug] --input INPUT [--couriers COURIERS] [--orders ORDERS]

Code Challenge

optional arguments:
  -h, --help           show this help message and exit
  --debug              Enable debug
  --input INPUT        the path of raw data of order
  --couriers COURIERS  the number of couriers will run on parallel
  --orders ORDERS      the number of orders, it will produce every second
```

## 5. run command

```shell
python main.py --input orders.json --orders 5 --couriers 10
```

## 6. run unit test cases

```shell
pytest
```

### info of pytest

```shell
$ git:(master) pytest
=========================================================================================== test session starts ============================================================================================
platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/bdmd/test/coding_challenge/python_version
collected 5 items

test_shelf.py .....                                                                                                                                                                                  [100%]

============================================================================================ 5 passed in 0.04s =============================================================================================
```

# extra where I can optimize

> I plan to add function "usage" on Shelf Class. When I pick up an order from Shelf, I will sort shelves by usage.
> And then pick the highest one, and get order from it.
