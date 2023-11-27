from hw_1 import Advert
import json
import pytest


@pytest.mark.parametrize(
    "input, expected_result",
    [
        (
            """{
        "title": "python",
        "price": 0,
        "location": {
        "address": "город Москва, Лесная, 7",
        "metro_stations": ["Белорусская"]
        }
    }""",
            ["python", 0, "город Москва, Лесная, 7", ["Белорусская"]],
        )
    ],
)
def test_1_1(input, expected_result):
    dic_input = json.loads(input)
    lesson = Advert(dic_input)

    # обращаемся к атрибутам lesson
    assert lesson.title == expected_result[0]
    assert lesson.price == expected_result[1]
    assert lesson.location.address == expected_result[2]
    assert lesson.location.metro_stations == expected_result[3]


@pytest.mark.parametrize(
    "input, expected_result",
    [
        (
            """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs"
    }""",
            ["Вельш-корги", 1000, "dogs"],
        )
    ],
)
def test_1_2(input, expected_result):
    dic_input = json.loads(input)
    dog_ad = Advert(dic_input)
    # обращаемся к атрибутам dog_ad
    assert dog_ad.title == expected_result[0]
    assert dog_ad.price == expected_result[1]
    assert dog_ad.class_ == expected_result[2]


@pytest.mark.parametrize(
    "input",
    [
        (
            """{
        "title": "python",
        "price": -1
    }"""
        )
    ],
)
def test_1_3(input):
    lesson = json.loads(input)
    with pytest.raises(ValueError, match="price должна быть >= 0"):
        Advert(lesson)


@pytest.mark.parametrize(
    "input",
    [
        (
            """{
        "title": "python",
        "price": 1
    }"""
        )
    ],
)
def test_1_4(input):
    lesson = json.loads(input)
    lesson_ad = Advert(lesson)
    with pytest.raises(ValueError, match="price должна быть >= 0"):
        lesson_ad.price = -3


@pytest.mark.parametrize(
    ("input", "expected_result"),
    [
        (
            """{
        "title": "python"
    }""",
            0.0,
        )
    ],
)
def test_1_5(input, expected_result):
    lesson = json.loads(input)
    lesson_ad = Advert(lesson)
    assert lesson_ad.price == expected_result


@pytest.mark.parametrize(
    "input",
    [
        (
            """{
        "price": 1
    }"""
        )
    ],
)
def test_1_6(input):
    lesson = json.loads(input)
    with pytest.raises(ValueError, match="Атрибут title не найден"):
        Advert(lesson)


@pytest.mark.parametrize(
    ("input", "expected_result"),
    [
        (
            """{
        "title": "iPhone X",
        "price": 100
    }""",
            "iPhone X | 100 ₽",
        )
    ],
)
def test_2_1(input, expected_result):
    iphone = json.loads(input)
    iphone_ad = Advert(iphone)
    assert f"{iphone_ad}" == expected_result
