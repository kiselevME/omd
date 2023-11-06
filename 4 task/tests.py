import pytest
from one_hot_encoder import fit_transform


@pytest.mark.parametrize(
        'input, expected_result',
        [
            (['123', '345', '123'],
             [('123', [0, 1]), ('345', [1, 0]), ('123', [0, 1])]),
            ([123, 345, 123],
             [(123, [0, 1]), (345, [1, 0]), (123, [0, 1])]),
            ('abc',
             [('abc', [1])]),
            ('',
             [('', [1])])
        ]
)
def test_one_hot_transform(input, expected_result):
    assert fit_transform(input) == expected_result


@pytest.mark.parametrize(
        'input',
        [
            None,
            [[1, 2], [3, 4]]
        ]
)
def test_one_hot_raise_type_error(input):
    with pytest.raises(TypeError):
        fit_transform(input)
