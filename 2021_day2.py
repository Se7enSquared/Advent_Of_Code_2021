# 2021 Day 2
# Puzzle at: https://adventofcode.com/2021/day/2

'''
    Part 1:
    Given a course for your submarine, Calculate the horizontal position 
    and depth you would have after following the planned course. 
    What do you get if you multiply your final horizontal position by your 
    final depth?
    
    Part 2:
    In addition to horizontal position and depth, you'll also need to track 
    a third value, aim, which also starts at 0. The commands also mean 
    something entirely different than you first thought:
    
    - down X increases your aim by X units.
    - up X decreases your aim by X units.
    
    - forward X does two things:
        *It increases your horizontal position by X units.
        *It increases your depth by your aim multiplied by X.
'''
#---------------------------------------------------------------------------
# AOC framework & test setup
from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=2)

def print_test_results(day, part, expected, function_call):
    answer = function_call()
    if answer == expected:
        print('Day ' + str(day) + '.'+ str(part) + ' Result = **Pass**: answer "' + str(answer) + '" returned from ' + function_call.__name__)
    else:
        print('Day ' + str(day) + '.'+ str(part) + ' Result = **Fail** (expected "' + str(expected) + '): answer "' + str(answer) + '" returned from ' + function_call.__name__)

    
#---------------------------------------------------------------------------

# Begin solution #######################
planned_course = puzzle.input_data.split('\n')

def move_forward(forward_pos, amount):
    return forward_pos + amount

def move_up_down(depth_pos, amount):
    return depth_pos + amount

def move_forward_with_aim(forward_pos, depth_pos, aim_pos, amount):
    forward_pos += amount
    if aim_pos > 0:
        depth_pos += amount * aim_pos
    return forward_pos, depth_pos

def plot_course():
    longitudinal_pos = 0
    latitudinal_pos = 0

    for instruction in planned_course:
        direction, amount = instruction.split(' ')[0], int(instruction.split(' ')[1])
        
        if direction == 'forward':
            longitudinal_pos = move_forward(longitudinal_pos, amount)
            
        else:
            if direction == 'up':
                amount = -amount
            latitudinal_pos = move_up_down(latitudinal_pos, amount)
    return (longitudinal_pos * latitudinal_pos)        
    
def plot_course_with_aim():
    longitudinal_pos = 0
    latitudinal_pos = 0
    aim_pos = 0

    for instruction in planned_course:
        direction, amount = instruction.split(' ')[0], int(instruction.split(' ')[1])
        
        if direction == 'forward':
            longitudinal_pos, latitudinal_pos = move_forward_with_aim(longitudinal_pos, latitudinal_pos, aim_pos, amount)
            
        else:
            if direction == 'up':
                amount = -amount
            aim_pos += amount
    return (longitudinal_pos * latitudinal_pos)    

if __name__ == '__main__':
    print('T E S T  R E S U L T S')
    print('-----------------------------------------')
    print_test_results(1, 1, 1507611, plot_course)
    print_test_results(1, 2, 1880593125, plot_course_with_aim)
    