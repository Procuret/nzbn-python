"""
New Zealand Business Number
Test Suite Module
author: hugh@procuret.com
© Procuret Operating Pty Ltd
"""
import sys
from nzbn.tests import cases

STOP_AFTER_ONE = False
START = 0

if '--start' in sys.argv[1:] or '-s' in sys.argv[1:]:
    index = 0
    for key in sys.argv[1:]:
        if key == '--start' or key == '-s':
            START = int(sys.argv[1:][index + 1])
            break
        index += 1
        continue

if '--only-one' in sys.argv[1:] or '-o' in sys.argv[1:]:
    STOP_AFTER_ONE = True

LAST = False
if '--last' in sys.argv[1:]:
    LAST = True


TESTS = [
    cases.RetrieveEntity,
    cases.SearchByName,
    cases.ParseRegisteredAddress
]


def run_tests(start=START) -> None:
    """Execute NZBN Python unit tests"""
    print('Executing NZBN Python Test Suite')
    i = 0
    if LAST is True:
        start = len(TESTS)
    for test in TESTS:
        i += 1
        if i < start:
            continue
        number = str(i)
        while len(number) < 3:
            number = '0' + number
        number = '[' + number + '] '
        executed_test = test()
        executed_test.run()
        print(number + executed_test.report())
        if executed_test.did_fail:
            break
        if STOP_AFTER_ONE is True:
            break
    print('NZBN Python Test sequence complete.')
    return
