def is_valid(numbers: list):
    is_increasing = all(0 < (b - a) <= 3 for a, b in zip(numbers, numbers[1:]))
    is_decreasing = all(-3 <= (b - a) < 0 for a, b in zip(numbers, numbers[1:]))

    return is_increasing or is_decreasing

def problem_1():
    count = 0
    with open ('day2_input.txt', 'r') as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))
            if not numbers:
                continue
            if is_valid(numbers):
                count += 1
    return count



def problem_2():
    count = 0
    with open ('day2_input.txt', 'r') as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))
            if not numbers or len(numbers) <= 1:
                continue
            if is_valid(numbers):
                count += 1
                continue
            else:
                for i in range(len(numbers)):
                    numbers_new = numbers[:i] + numbers[i+1:]
                    if is_valid(numbers_new):
                        count += 1
                        break
    return count


print(problem_1())
print(problem_2())