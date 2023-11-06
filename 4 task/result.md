# python -m pytest -v tests.py
============================================================================================= test session starts ==============================================================================================
platform darwin -- Python 3.11.5, pytest-7.4.3, pluggy-1.3.0 -- /opt/homebrew/Caskroom/miniconda/base/envs/base_env/bin/python
cachedir: .pytest_cache
rootdir: /Users/max/omd/4 task
collected 6 items                                                                                                                                                                                              

tests.py::test_one_hot_transform[input0-expected_result0] PASSED                                                                                                                                         [ 16%]
tests.py::test_one_hot_transform[input1-expected_result1] PASSED                                                                                                                                         [ 33%]
tests.py::test_one_hot_transform[abc-expected_result2] PASSED                                                                                                                                            [ 50%]
tests.py::test_one_hot_transform[-expected_result3] PASSED                                                                                                                                               [ 66%]
tests.py::test_one_hot_raise_type_error[None] PASSED                                                                                                                                                     [ 83%]
tests.py::test_one_hot_raise_type_error[input1] PASSED                                                                                                                                                   [100%]

============================================================================================== 6 passed in 0.01s ===============================================================================================