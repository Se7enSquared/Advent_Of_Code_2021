# 2021 Day X
# Puzzle at: X
'''
    Part 1:
    X
    
    Part 2:
    X
'''
#---------------------------------------------------------------------------
# AOC framework & test setup
from aocd.models import Puzzle
puzzle = Puzzle(year=2021, day=X)

def print_test_results(day, part, expected, function_call):
    answer = function_call()
    if answer == expected:
        print('Day ' + str(day) + '.'+ str(part) + ' Result = **Pass**: answer "' + str(answer) + '" returned from ' + function_call.__name__)
    else:
        print('Day ' + str(day) + '.'+ str(part) + ' Result = **Fail** (expected "' + str(expected) + '): answer "' + str(answer) + '" returned from ' + function_call.__name__)

    
#---------------------------------------------------------------------------

# Begin solution #######################
X = puzzle.input_data.split('\n')



if __name__ == '__main__':
    print('T E S T  R E S U L T S')
    print('-----------------------------------------')
    print_test_results(1, 1, EXPECTEDRESULT, FUNCTIONTORUN)
    print_test_results(1, 2, EXPECTEDRESULT, FUNCTIONTORUN)
    