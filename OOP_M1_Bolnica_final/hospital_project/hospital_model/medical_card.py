"""Медицинская карта — документ пациента.

UML: Пациент — МедицинскаяКарта — композиция (закрашенный ромб):
карта заводится при регистрации и принадлежит только этому пациенту.
"""


class MedicalCard:
    """Карта: номер, дата заведения и записи о приёмах."""

    def __init__(self, number, issue_date):
        self._number = number            # учётный номер карты
        self._issue_date = issue_date    # дата регистрации пациента
        self._records = []               # записи о проведённых приёмах

    @property
    def number(self):
        return self._number

    def add_record(self, appointment):
        """Добавить запись о приёме (вызывается методом Appointment.complete)."""
        self._records.append(appointment)

    def get_history(self):
        """История обращений в читаемом виде."""
        return [record.describe() for record in self._records]
