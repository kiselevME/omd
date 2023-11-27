from keyword import iskeyword
import json


class ColorizeMixin:
    @staticmethod
    def change_color(text: str, repr_color_code: int) -> str:
        """Изменяет цвет текса

        Args:
            text (_type_): Текст
            repr_color_code (_type_): Индекс цвета, в который перекрашиваем
                текст

        Returns:
            str: Текст заданного цвета
        """

        return f"\033[1;{repr_color_code};40m {text}\033[0;37;40m"

    def __str__(self):
        text = f"{self.title} | {self.price} ₽"
        if hasattr(self, "repr_color_code"):
            return self.change_color(text, self.repr_color_code)
        else:
            return text


class BaseAdvert:
    """
    Базовый класс, который принимает на вход словарь и выдает инстанс
    класса, к атрибутам которого можно обращаться через точку
    """

    def __init__(self, dic: dict) -> None:
        """
            Принимает на вход словарь, возвращает инстанс класса,
            к атрибутам которого можно обращаться через точку
        Args:
            dic (dict): Словарь, полученный из json
        """

        for k, v in dic.items():
            k = f"{k}_" if iskeyword(k) else k
            if k == "price":
                k = "_price"
            setattr(self, k, BaseAdvert(v) if isinstance(v, dict) else v)

    def _valid_params(self):
        if not hasattr(self, "title"):
            raise ValueError("Атрибут title не найден")

        if not hasattr(self, "_price"):
            self._price = 0.0
        elif self._price < 0:
            raise ValueError("price должна быть >= 0")

    @property
    def price(self) -> float:
        """Возвращает цену

        Returns:
            float: Цена (price)
        """
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("price должна быть >= 0")
        self._price = value

    def __str__(self):
        return f"{self.title} | {self.price} ₽"


class Advert(ColorizeMixin, BaseAdvert):
    """Основной класс (который требуется реализовать в рамках задачи)

    Args:
        BaseAdvert (_type_): Базовый класс
        ColorizeMixin (_type_): Миксина для вывода текста
    """

    def __init__(self, dic: dict) -> None:
        """
            Принимает на вход словарь, возвращает инстанс класса,
            к атрибутам которого можно обращаться через точку
        Args:
            dic (dict): Словарь, полученный из json
        """

        super().__init__(dic)
        self._valid_params()


if __name__ == "__main__":
    corgi_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "repr_color_code": 33
    }"""
    corgi = json.loads(corgi_str)
    corgi_ad = Advert(corgi)
    print(corgi_ad)
