# read file
with open ('day1_input.txt') as f:
    lines = f.readlines()
    f.close()

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
total_sum = 0

for line in lines:
    first = ''
    last = ''
    for letter in line:
        # print(letter)
        if letter in numbers:
            print(int(letter))
            if first == '':
                first = int(letter)
            else:
                last = int(letter)

        
    if last == '':
        last = first
    print("MY NUMBERS: ", first, last)
    total_sum += first*10 + last

print(total_sum)
        