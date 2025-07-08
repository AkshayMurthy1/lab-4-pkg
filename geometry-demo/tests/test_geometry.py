import pytest
from geometry.shapes import * 
from geometry.utils import *
import math

def test_circle_area_zero_and_positive():
 # Arrange: choose side lengths
 # Act: compute areas
 # Assert: use pytest.approx to compare with expected
 side_lengths = [0,4,5]
 for sl in side_lengths:
  assert Circle(sl).area() == sl**2*math.pi

def test_square_area_zero_and_positive():
 # Arrange: choose side lengths
 # Act: compute areas
 # Assert: use pytest.approx to compare with expected
 side_lengths = [0,4,5]
 for sl in side_lengths:
  assert Square(sl).area() == sl**2

def test_stats_keys_and_values():
 # Arrange: create several shapes
 # Act: call area_stats
 # Assert: stats is dict, has correct keys, and values are numbers
 circle1 = Circle(3)
 circle2 = Circle(10)
 square1 = Square(5)
 ret = area_stats(circle1,circle2,square1)
 assert type(ret)==dict
 assert list(ret.keys()) == ["n","total","mean","min","max"]
 assert all([type(val) in [float,int] for val in ret.values()])

def test_stats_raises_without_shapes():
 # Assert that calling area_stats() raises ValueError
 with pytest.raises(ValueError):
  area_stats()