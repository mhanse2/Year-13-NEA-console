# the highest level the player can achieve
CAP = 12

# question order
order = [
    'Addition',             # add
    'Subtraction',          # add
    'NegativeSubtraction',  # add
    'Multiplication',       # mult
    'Division',             # mult
    'Power',
    'Root',
    'SquareArea',           # mult
    'SquarePerimeter',      # mult
    'Triangle',             # mult
    'CirclePerimeter',      # mult
    'CircleArea'
]

# used for Addition, Subtraction & NegativeSubtraction
add_values = [
    [1, 2, 3, 4, 5],
    [2, 4, 5, 6, 8, 10],
    [5, 7, 11, 15, 18],
    [10, 11, 13, 15, 20],
    [13, 15, 19, 21, 25],
    [19, 23, 25, 27, 30],
    [24, 27, 30, 35, 37],
    [30, 35, 36, 38, 40],
    [36, 40, 42, 45, 47],
    [45, 48, 50, 52, 55],
    [50, 53, 55, 57, 60],
    [55, 58, 60, 63, 65],
    [60, 63, 66, 69, 70]
]

# used for Multiplication, Division, Triangle, 
# SquareArea, SquarePerimeter and CirclePerimeter
mult_values = [
    [2, 4],
    [2, 3, 4, 10],
    [2, 3, 4, 6, 10],
    [3, 4, 6, 8, 10],
    [4, 6, 8, 9, 10, 12],
    [5, 6, 8, 9, 10, 12],
    [6, 7, 8, 9, 12, 15],
    [7, 9, 12, 15, 20],
    [7, 12, 15, 20, 25],
    [12, 15, 18, 20, 25]
]
