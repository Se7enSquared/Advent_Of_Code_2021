from day1 import find_depth_increase_count, sliding_depth_increase_count
from day2 import plot_course, plot_course_with_aim


def print_test_results(day, part, expected, function_call):
    answer = function_call()
    if answer == expected:
        print(
            f'Day {str(day)}.{str(part)}'
            + ' Result = **Pass**: answer "'
            + str(answer)
            + '" returned from '
            + function_call.__name__
        )

    else:
        print(
            f'Day {str(day)}.{str(part)}'
            + ' Result = **Fail** (expected "'
            + str(expected)
            + '): answer "'
            + str(answer)
            + '" returned from '
            + function_call.__name__
        )

if __name__ == '__main__':
    print('T E S T  R E S U L T S')
    print('-----------------------------------------')
    print('----D A Y  1----')
    print_test_results(1, 1, 1466, find_depth_increase_count)
    print_test_results(1, 2,  1491,sliding_depth_increase_count)
    print('----D A Y  2----')
    print_test_results(2, 1, 1507611, plot_course)
    print_test_results(2, 2, 1880593125, plot_course_with_aim)
