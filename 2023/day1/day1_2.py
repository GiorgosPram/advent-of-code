# read file
with open ('day1_input.txt') as f:
    lines = f.readlines()
    f.close()

numbers = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
total_sum = 0

for line in lines:

    first = ''
    last = ''
    temporal_indexes = {}
    min = None
    max = None
    
    print("CURRENT LINE: ", line)

    for number in numbers:
        if number in line:
            print(number, numbers[number])
            if min is None:
                min = line.find(number)
                first = numbers[number]
            elif line.find(number) < min:
                min = line.find(number)
                first = numbers[number]

            if max is None:
                max =  line.rfind(number)
                last = numbers[number] 
            elif line.rfind(number) > max:
                max =  line.rfind(number)
                last = numbers[number]


    print("LINE SUM: ", first*10 + last)
    
    print("NEW LINE: ")
    total_sum += first*10 + last

print(total_sum)
        