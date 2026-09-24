"""Человек — базовый класс для пациента и медицинского персонала.

UML: обобщение (пустой треугольник). Общие атрибуты всех участников
процесса вынесены в этот класс, чтобы не дублировать их в наследниках.
"""
from datetime import date


class Person:
    """Общий родитель пациента и персонала: ФИО, дата рождения, телефон."""

    def __init__(self, full_name, birth_date, phone):
        self._full_name = full_name      # ФИО (защищённый член, UML: #)
        self._birth_date = birth_date    # дата рождения
        self._phone = phone              # контактный телефон

    @property
    def full_name(self):
        """Только чтение: ФИО не должно меняться извне."""
        return self._full_name

    def get_age(self):
        """Возраст в полных годах по дате рождения."""
        today = date.today()
        age = today.year - self._birth_date.year
        if (today.month, today.day) < (self._birth_date.month, self._birth_date.day):
            age -= 1
        return age

    def get_contacts(self):
        """Контактная информация человека в едином формате."""
        return f"{self._full_name}, тел. {self._phone}"
