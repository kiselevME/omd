import pytest
from morse import decode


@pytest.mark.parametrize(
        'test_input, expected',
        [
            ('... --- ...', 'SOS'),
            ('.---- ..--- ...-- ....- ..... -.... --... ---.. ----. -----'
             ' -.--. -.--.- -..-. .-.-.-  ', '1234567890()/.')

        ]
    )
def test_decode(test_input, expected):
    assert decode(test_input) == expected


@pytest.mark.parametrize('test_input', '[')
def test_decode_raises(test_input):
    with pytest.raises(KeyError):
        decode(test_input)
