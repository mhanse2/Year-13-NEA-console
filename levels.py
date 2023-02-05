# the highest level the player can achieve
CAP = 12

# question order
order = [
    'Addition',             # add - 0
    'Subtraction',          # add - 1
    'NegativeSubtraction',  # add - 2
    'Multiplication',       # mult - 3
    'Division',             # mult - 4
    'Power',                # pow - 5
    'Root',                 # root - 6
    'SquareArea',           # mult - 7
    'SquarePerimeter',      # mult - 8
    'Triangle',             # mult - 9
    'CirclePerimeter',      # mult - 10
    'CircleArea'            # pow - 11
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
# SquareArea, SquarePerimeter & CirclePerimeter
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

# used for Power & CircleArea
pow_values = [
    [   # indices
        [2],
        [2, 3]
    ],
    [   # values
        [2, 3, 4, 5],
        [3, 4, 5, 10],
        [3, 5, 6, 9, 10]
    ]
]

# used for Root
# due to the precise nature of roots, values are stored in a dictionary
root_values = [
    [4, 16, 32, 64],
    [9, 27, 64]
]
