with open ('day3_input.txt') as f:
    lines = f.readlines()
    f.close()

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['@', '%', '=', '-', '*', '&', '/', '+', '#', '$']
window = []

i=0
for i in range(len(lines)):
    
    j=0
    w_s = None
    w_e = None

    while j < len(lines[i]):
        if i=0: # FORST ROW
            if lines[i][j].isnumeric():
                w_s = j
                w_e = j
                if lines[i][j+1].isnumeric():
                    w_e = j+1
                    if lines[i][j+2].isnumeric():
                        w_e = j+2
        elif i < len(lines)-1: # MID ROWS
            pass
        else: # LAST ROW
            pass