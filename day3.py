# 2021 Day 3
# Puzzle at: https://adventofcode.com/2021/day/3
'''
    Part 1:
    for each bit of a list of binary numbers, find the most
    common bit (0 or 1) at each bit position and then convert
    to decimal to get the gamma_rate. For the epsilon rate,
    get the least common bit (0 or 1). Then multiply the 
    gamma and epsilon decimals together
    
    Part 2:
    X
'''
#---------------------------------------------------------------------------
# AOC framework setup
from aocd.models import Puzzle
from requests.api import get
puzzle = Puzzle(year=2021, day=3)

#---------------------------------------------------------------------------
# Begin solution #######################
from collections import Counter
diagnostic_report = puzzle.input_data.split('\n')

    
def get_rates():

    gamma_rate = ''
    epsilon_rate = ''
    
    for i in range(12):     
        counter = {}   
        for j in range(len(diagnostic_report)):
            current_number = diagnostic_report[j][i]
            counter[current_number] = counter.get(current_number, 0) + 1

        counter = Counter(counter)
        
        gamma_rate += str(counter.most_common()[0][0])
        epsilon_rate += str(counter.most_common()[1][0])
        
    
    return (int(gamma_rate, 2) * int(epsilon_rate, 2))
        
        
if __name__ == '__main__':
    print(diagnostic_report)
    print(get_rates())