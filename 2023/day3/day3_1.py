with open ('day3_input.txt') as f:
    lines = f.readlines()
    f.close()

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['@', '%', '=', '-', '*', '&', '/', '+', '#', '$']

window = []
a = 0
i = 0
while i < len(lines):

    if i == 0:
        j = 0
        while j < len(lines[i])-3:
            # print('hearthbeat', i, j)

            if j == 0:
                if lines[i][j] in numbers and \
                (lines[i][j+1] in symbols \
                or lines[i+1][j] in symbols or lines[i+1][j+1] in symbols):
                    window.append(int(lines[i][j]))
                    j += 1
                
                elif lines[i][j] in numbers and lines[i][j+1] in numbers and \
                    (lines[i][j-2] in symbols or lines[i][j+1] in symbols \
                    or lines[i+1][j-1] in symbols or lines[i+1][j] in symbols or lines[i+1][j+1] in symbols):
                    window.append(int(lines[i][j])*10 + int(lines[i][j+1]))
                    j += 2

                elif lines[i][j] in numbers and lines[i][j+1] in numbers and lines[i][j+2] in numbers and \
                    (lines[i][j+3] in symbols or lines[i][j-1] in symbols \
                    or lines[i+1][j-1] in symbols or lines[i+1][j] in symbols or lines[i+1][j+1] in symbols):
                    window.append(int(lines[i][j])*100 + int(lines[i][j+1])*10 + int(lines[i][j+2]))
                    j += 3

                else:
                    j += 1
            else:
                if lines[i][j] in numbers and \
                (lines[i][j-1] in symbols or lines[i][j+1] in symbols \
                or lines[i+1][j-1] in symbols or lines[i+1][j] in symbols or lines[i+1][j+1] in symbols):
                    window.append(int(lines[i][j]))
                    j += 1
                
                elif lines[i][j] in numbers and lines[i][j+1] in numbers and \
                    (lines[i][j-2] in symbols or lines[i][j+1] in symbols \
                    or lines[i+1][j-1] in symbols or lines[i+1][j] in symbols or lines[i+1][j+1] in symbols):
                    window.append(int(lines[i][j])*10 + int(lines[i][j+1]))
                    j += 2

                elif lines[i][j] in numbers and lines[i][j+1] in numbers and lines[i][j+2] in numbers and \
                    (lines[i][j+3] in symbols or lines[i][j-1] in symbols \
                    or lines[i+1][j-1] in symbols or lines[i+1][j] in symbols or lines[i+1][j+1] in symbols):
                    window.append(int(lines[i][j])*100 + int(lines[i][j+1])*10 + int(lines[i][j+2]))
                    j += 3

                else:
                    j += 1

    elif i > 0 and i < len(lines)-1:
        j = 0
        while j < len(lines[i])-3:
            # print('hearthbeat 2', i,j)
            if lines[i][j] in numbers and \
            (lines[i][j+1] in symbols or lines[i][j-1] in symbols \
            or lines[i-1][j-1] in symbols or lines[i-1][j] in symbols or lines[i-1][j+1] in symbols\
            or lines[i+1][j-1] in symbols or lines[i+1][j] in symbols or lines[i+1][j+1] in symbols):
                window.append(int(lines[i][j]))
                j += 1
            
            elif lines[i][j] in numbers and lines[i][j+1] in numbers and \
                (lines[i][j+2] in symbols or lines[i][j-1] in symbols \
                or lines[i-1][j-1] in symbols or lines[i-1][j] in symbols or lines[i-1][j+1] in symbols\
                or lines[i+1][j-1] in symbols or lines[i+1][j] in symbols or lines[i+1][j+1] in symbols):
                window.append(int(lines[i][j])*10 + int(lines[i][j+1]))
                j += 2

            elif lines[i][j] in numbers and lines[i][j+1] in numbers and lines[i][j+2] in numbers and \
                (lines[i][j+3] in symbols or lines[i][j-1] in symbols \
                or lines[i-1][j-1] in symbols or lines[i-1][j] in symbols or lines[i-1][j+1] in symbols\
                or lines[i+1][j-1] in symbols or lines[i+1][j] in symbols or lines[i+1][j+1] in symbols):
                window.append(int(lines[i][j])*100 + int(lines[i][j+1])*10 + int(lines[i][j+2]))
                j += 3

            else:
                j += 1
    
    else:
        j = 0
        while j < len(lines[i])-3:
            # print('hearthbeat 3', i, j)
            if lines[i][j] in numbers and \
            (lines[i][j+1] in symbols or lines[i][j-1] in symbols \
            or lines[i-1][j-1] in symbols or lines[i-1][j] in symbols or lines[i-1][j+1] in symbols):
                window.append(int(lines[i][j]))
                j += 1
            
            elif lines[i][j] in numbers and lines[i][j+1] in numbers and \
                (lines[i][j+2] in symbols or lines[i][j-1] in symbols \
                or lines[i-1][j-1] in symbols or lines[i-1][j] in symbols or lines[i-1][j+1] in symbols):
                window.append(int(lines[i][j])*10 + int(lines[i][j+1]))
                j += 2

            elif lines[i][j] in numbers and lines[i][j+1] in numbers and lines[i][j+2] in numbers and \
                (lines[i][j+3] in symbols or lines[i][j-1] in symbols \
                or lines[i-1][j-1] in symbols or lines[i-1][j] in symbols or lines[i-1][j+1] in symbols):
                window.append(int(lines[i][j])*100 + int(lines[i][j+1])*10 + int(lines[i][j+2]))
                j += 3

            else:
                j += 1

    # print('GRAMMI: ', i)        
    i += 1

print(sum(window))