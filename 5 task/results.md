1. `python -m unittest -v tests.py`
test_what_is_year_now_1 (tests.TestWhatIsYear.test_what_is_year_now_1) ... ok
test_what_is_year_now_2 (tests.TestWhatIsYear.test_what_is_year_now_2) ... ok
test_what_is_year_now_raise_1 (tests.TestWhatIsYear.test_what_is_year_now_raise_1) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK

2. Создаем файл .coveragerc и прописываем там 
```
[report]

exclude_lines =
    if __name__ == .__main__.:
```

3. `py.test --cov-report html tests.py --cov=./`
============================================================================================= test session starts ==============================================================================================
platform darwin -- Python 3.11.5, pytest-7.4.3, pluggy-1.3.0
rootdir: /Users/max/omd/5 task
plugins: cov-4.1.0
collected 3 items                                                                                                                                                                                              

tests.py ...                                                                                                                                                                                             [100%]

---------- coverage: platform darwin, python 3.11.5-final-0 ----------
Coverage HTML written to dir htmlcov


============================================================================================== 3 passed in 0.06s ===============================================================================================

4. Получаем файл ./htmlcov/what_is_year_now_py.html
Покрытие 100% достигнуто