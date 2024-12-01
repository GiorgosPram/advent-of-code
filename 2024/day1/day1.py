import pandas as pd

df = pd.read_csv("day1_input.txt", delimiter='   ', names=['left', 'right'], engine='python')

def problem_1():
    sorted_left = df['left'].sort_values().reset_index(drop=True)
    sorted_right = df['right'].sort_values().reset_index(drop=True)

    # Part 1
    return abs(sorted_right - sorted_left).sum()

def problem_2():
    right_counts = df['right'].value_counts()
    left_counts = df['left'].map(right_counts).fillna(0).astype(int)

    # Part 2
    return (left_counts * df['left']).sum()


print(problem_1())
print(problem_2())