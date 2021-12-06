# 2021 Day 1
# Puzzle at: https://adventofcode.com/2021/day/1
'''
    Part 1:
    Given a sonar sweep report showing depths recorded in front of the 
    submarine, count the number of times a depth measurement increases 
    from the previous measurement.
    
    Part 2:
    Do the same but by comparing a sliding window of 3 measurements
'''
#---------------------------------------------------------------------------
# AOC framework & test setup
from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=1)

def print_test_results(day, part, expected, function_call):
    answer = function_call()
    if answer == expected:
        print('Day ' + str(day) + '.'+ str(part) + ' Result = **Pass**: answer "' + str(answer) + '" returned from ' + function_call.__name__)
    else:
        print('Day ' + str(day) + '.'+ str(part) + ' Result = **Fail** (expected "' + str(expected) + '): answer "' + str(answer) + '" returned from ' + function_call.__name__)

    
#---------------------------------------------------------------------------

# Begin solution #######################
sonar_sweep_report = puzzle.input_data.split('\n')

def find_depth_increase_count():
    
    depth_increase_count = 0
    
    for i in range(1, len(sonar_sweep_report)):
        current_depth = int(sonar_sweep_report[i])
        previous_depth = int(sonar_sweep_report[i-1])
        
        if current_depth > previous_depth:
            depth_increase_count += 1
    return depth_increase_count

def sliding_depth_increase_count():
    
    depth_increase_count = 0
    
    for i in range(1, len(sonar_sweep_report)):
        try:
            current_depth = int(sonar_sweep_report[i]) + int(sonar_sweep_report[i+1]) + int(sonar_sweep_report[i+2])
            previous_depth = int(sonar_sweep_report[i-1]) + int(sonar_sweep_report[i]) + int(sonar_sweep_report[i+1])
        except:
            continue
        if current_depth > previous_depth:
            depth_increase_count += 1
    return depth_increase_count

