from typing import List


"""This function takes a list of integers as input and returns a new list containing
 only the individual elements from the original list."""
def no_duplicates(arr: List[int]) -> List[int]:
    return list(set(arr))


"""This function takes two integers as input (minimum and maximum) and 
returns a list of all prime numbers in a given range."""
def prime_numbers(min_num: int, max_num: int) -> List[int]:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = [num for num in range(min_num, max_num + 1) if is_prime(num)]
    return prime_numbers


"""This class represents a point in two-dimensional space. The class must have methods for initializing 
the coordinates of a point, calculating the distance to another point, 
and also for getting and changing coordinates."""
class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x: float = x
        self.y: float = y

    def get_distance_between(self, other_point: 'Point') -> float:
        distance: float = ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
        return distance

    def get_coordinates(self) -> tuple[float, float]:
        return self.x, self.y

    def set_coordinates(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

"""This function sorts a list of strings by length, first in ascending order and then in descending order"""
def sort_strings_by_len(string_list: List[str]) -> tuple[List[str], List[str]]:
    sorted_strings_asc = sorted(string_list, key=len)
    sorted_strings_desc = sorted(sorted_strings_asc, key=len, reverse=True)

    return sorted_strings_asc, sorted_strings_desc