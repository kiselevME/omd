`python -m doctest -o FAIL_FAST morse.py -v`
Trying:
    decode('... --- ...')
Expecting:
    'SOS'
ok
Trying:
    decode('... .--. .- -.-. .   - . ... -')
Expecting:
    'SPACETEST'
ok
Trying:
    encode('SOS')
Expecting:
    '... --- ...'
ok
Trying:
    encode('SPACE TEST') # doctest: +NORMALIZE_WHITESPACE
Expecting:
    '... .--. .- -.-. .   - . ...        -'
ok
Trying:
    encode('@') #
Expecting:
    Traceback (most recent call last):
        ...
    KeyError: '@'
ok
1 items had no tests:
    morse
2 items passed all tests:
   2 tests in morse.decode
   3 tests in morse.encode
5 tests in 3 items.
5 passed and 0 failed.
Test passed.
