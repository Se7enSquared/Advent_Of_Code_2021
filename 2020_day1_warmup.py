# 2020 Day 1 to warm up for the 2021 puzzles coming tomorrow :)
# Puzzle at: https://adventofcode.com/2020/day/1
'''
    Part 1:
    Before you leave, the Elves in accounting just need you to fix your 
    expense report (your puzzle input); apparently, something isn't 
    quite adding up. Specifically, they need you to find the two entries
    that sum to 2020 and then multiply those two numbers together.
    
    Part 2:
    In your expense report, what is the product of the THREE entries that 
    sum to 2020?
'''
#---------------------------------------------------------------------------
# AOC framework setup
from aocd.models import Puzzle
puzzle = Puzzle(year=2020, day=1)
#---------------------------------------------------------------------------

# Begin solution #######################
from itertools import combinations

expense_report = puzzle.input_data.split('\n')
TARGET_SUM = 2020

def get_product(permutations):
    
    combos = list(combinations(expense_report, permutations))
    product = 1

    for combo in combos:
        combo_sum = sum(int(number) for number in combo)

        if combo_sum == TARGET_SUM:
            for number in combo:
                product *= int(number)

    return product

if __name__ == '__main__':
    answer_day1pt1 = 157059
    answer_day1pt2 = 165080960

    pt1_answer = get_product(2)
    pt2_answer = get_product(3)

    test_day1pt1 = 'Pass' if pt1_answer == answer_day1pt1 else 'Fail'
    test_day1pt2 = 'Pass' if pt2_answer == answer_day1pt2 else 'Fail'
    print('T E S T  R E S U L T S')
    print('-----------------------------------------')
    print(f'Day 1 Part 1: {test_day1pt1} with answer: {str(pt1_answer)}')
    print(f'Day 1 Part 2: {test_day1pt2} with answer: {str(pt2_answer)}')
