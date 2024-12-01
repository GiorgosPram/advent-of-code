with open ('day2_input.txt') as f:
    lines = f.readlines()
    f.close()


# 12 red cubes, 13 green cubes, and 14 blue cubes
result = 0

for line in lines:
    # print(line)
    # game_id = int(line.split(': ')[0].split(' ')[1])
    
    game_list = line.split(': ')[1].split(';')
    num_of_games = len(game_list)
    max_reds = 0
    max_greens = 0
    max_blues = 0

    for game in game_list:
        if 'red' in game:
            reds = game.split(' red')[0]
            reds = reds[len(reds)-2:]
            if reds[0] == ' ':
                reds = reds[1:]
            reds = int(reds)
            if reds > max_reds:
                max_reds = reds
        else:
            reds = 0

        if 'green' in game:
            greens = game.split(' green')[0]
            greens = greens[len(greens)-2:]
            if greens[0] == ' ':
                greens = greens[1:]
            greens = int(greens)
            if greens > max_greens:
                max_greens = greens
        else:
            greens = 0

        if 'blue' in game:
            blues = game.split(' blue')[0]
            blues = game.split(' blue')[0]
            blues = blues[len(blues)-2:]
            if blues[0] == ' ':
                blues = blues[1:]
            blues = int(blues)
            if blues > max_blues:
                max_blues = blues
        else:
            blues = 0

    result += max_reds * max_greens * max_blues


print(result)