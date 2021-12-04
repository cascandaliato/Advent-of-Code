import os
import shutil
import sys

from colorama import init, Fore, Style
init()

from pyutils import download, puzzle_input

year = sys.argv[1]
day = str(sys.argv[2]).zfill(2)

day_folder = os.path.join(year, day)
if not os.path.exists(day_folder):
    os.makedirs(day_folder)
    shutil.copy(os.path.join('template', '__init__.py'), os.path.join(day_folder, '__init__.py'))
    open(os.path.join(day_folder, 'test.txt'), 'a').close()

os.chdir(os.path.abspath(os.sep.join([year, day])))
download(*sys.argv[1:])

solution = getattr(__import__('.'.join([year, day])), day)

parse = solution.parse if hasattr(solution, 'parse') else lambda x: x


def run(part):
    solver_name = f'solve{part}'
    if hasattr(solution, solver_name):
        print()
        print(f'Part {part}')
        solver = getattr(solution, solver_name)
        if hasattr(solver, 'expectations'):
            max_testname = max(len(testname)
                               for testname in solver.expectations.keys())
            for filename, expectation in sorted(solver.expectations.items()):
                result = solver(parse(puzzle_input(f'{filename}.txt')))
                if result == expectation:
                    print(
                        f'  {filename:<{max_testname+2}}{Fore.GREEN}PASS{Style.RESET_ALL}')
                else:
                    print(
                        f'  {filename:<{max_testname+2}}{Fore.RED}FAIL{Style.RESET_ALL}  (expected {expectation}, got {result})')
                    raise AssertionError()
        print(f'  solution = {solver(parse(puzzle_input()))}')


try:
    print(f'AoC.{Fore.LIGHTGREEN_EX}{year}{Style.RESET_ALL}.{Fore.LIGHTYELLOW_EX}{day}{Style.RESET_ALL}')
    run(1)
    run(2)
except AssertionError:
    pass
