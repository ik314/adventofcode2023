#!/usr/bin/env python3

cube_check = {'red': 12,
              'green': 13,
              'blue': 14}

puzzle_file = open("../test/02.txt")


def part1(puzzle_file):
    running_total = 0
    for line in puzzle_file:
        possible = True
        line = line.strip('\n')
        arr = line.split(": ")
        print(arr)
        results = arr[1].split("; ")
        cubes_dict = {'red': 0, 'blue': 0, 'green': 0}
        for r in results:
            cubes_arr = r.split(", ")
            for color in cubes_arr:
                num_per_color = color.split(" ")
                color = num_per_color[1]
                if (int(num_per_color[0]) > cube_check[color]):
                    possible = False

        if (possible):
            game_id = int(arr[0].replace("Game ", ""))
            running_total += game_id

    return running_total



def part2(puzzle_file):
    running_total = 0
    for line in puzzle_file:
        line = line.strip('\n')
        cubes_dict = {'red': 0, 'green': 0, 'blue': 0}

        arr = line.split(": ")
        print(arr)
        results = arr[1].split("; ")
        for r in results:
            cubes_arr = r.split(", ")
            for color in cubes_arr:
                num_per_color = color.split(" ")
                color = num_per_color[1]
                if (int(num_per_color[0]) > cubes_dict[color]):
                    cubes_dict[color] = int(num_per_color[0])

        power = cubes_dict['red'] * cubes_dict['green'] * cubes_dict['blue']
        print("Power of Minimum Set for {}: {} ({} x {} x {})".format(arr[0],
                                                                      power,
                                                                      cubes_dict['red'],
                                                                      cubes_dict['green'],
                                                                      cubes_dict['blue']))
        running_total += power


    return running_total

# part1(puzzle_file)
part2(puzzle_file)
