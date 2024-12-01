import pandas as pd

df = pd.read_csv("day1_input.txt", delimiter='   ', names=['left', 'right'], engine='python')

sorted_left = df['left'].sort_values().reset_index(drop=True)
sorted_right = df['right'].sort_values().reset_index(drop=True)
differences = abs(sorted_right - sorted_left)

# Part 1
print(differences.sum())

right_counts = df['right'].value_counts()
left_counts = df['left'].map(right_counts).fillna(0).astype(int)
similarity_score = left_counts * df['left']

# Part 2
print(similarity_score.sum())