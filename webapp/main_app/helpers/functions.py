import random
from datetime import datetime
import datetime as date

def generate_random(start, end, count):
    """
    Generate a tuple of unique random numbers within the specified range.

    Parameters:
    - start (int): The start of the range (inclusive).
    - end (int): The end of the range (exclusive).
    - count (int): The number of unique random numbers to generate.

    Returns:
    - tuple: A tuple of unique random numbers.
    """
    if start >= end:
        raise ValueError("Start must be less than end.")

    if count > end - start:
        raise ValueError("Count must be less than or equal to the range size.")

    random_numbers = tuple(random.sample(range(start, end), count))
    return random_numbers

def now_time():
    current_datetime = datetime.now()

    moment1 = date.datetime(2024, 1, 1, 0, 0, 0)
    moment2 = date.datetime(
        current_datetime.year,
        current_datetime.month,
        current_datetime.day,
        current_datetime.hour,
        current_datetime.minute,
        current_datetime.second
    )
    delta = moment2 - moment1

    delta_s = delta.total_seconds()
    if delta_s < 0 :
        print('Something wrong with your time')
    else:
        delta_s = int(int(delta_s)/3600)
    return delta_s



if __name__ == '__main__':
    # Example usage:
    # start_range = 1
    # end_range = 100
    # number_of_random_numbers = 5
    #
    # random_numbers = generate_random(start_range, end_range, number_of_random_numbers)
    # print(random_numbers)

    print(now_time())
