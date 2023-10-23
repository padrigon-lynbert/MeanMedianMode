from math_algorithms.mean import mean
from math_algorithms.median import median
from math_algorithms.mode import mode

from icecream import ic

print("SEPARATE INDIVIDUAL DATA USING SPACES")
get_input = input(": ").split()
data = list(map(float, get_input))

print(f"Mean: {mean(data)} \nMedian: {median(data)} \nMode: {mode(data)}")

# Calculate the mean, median, and mode of a list using an easy-to-read input method. Already with a basic example. This is a very straightforward submodule.
