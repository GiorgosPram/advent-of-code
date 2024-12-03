import re

MUL_PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
SEGMENTATION_PATTERN = re.compile(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))")

DO = "do()"
DONT = "don't()"

def problem_1():
    total_summary = 0
    with open ('day3_input.txt', 'r') as file:
            for line in file:

                for number1, number2 in re.findall(MUL_PATTERN, line):
                    total_summary += int(number1) * int(number2)

    return total_summary

def problem_2():
    total_summary = 0
    keep = True
    with open ('day3_input.txt', 'r') as file:
            for line in file:
                list_to_iterate = re.findall(SEGMENTATION_PATTERN, line)
                for element in list_to_iterate:
                    if element == DO:
                        keep = True
                        continue
                    elif element == DONT:
                        keep = False
                    elif 'mul' in element and keep:
                        number1, number2 = map(int, re.match(MUL_PATTERN, element).groups())
                        total_summary += number1 * number2

    return total_summary

print(problem_1())
print(problem_2())

