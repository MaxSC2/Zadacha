"""Пациент — наследник Person; владеет медицинской картой (композиция).

UML: Человек -> Пациент — обобщение; Пациент — Приём — ассоциация.
"""
from .appointment import Appointment
from .medical_card import MedicalCard
from .person import Person


class Patient(Person):
    """Пациент: полис ОМС и собственная медицинская карта."""

    def __init__(self, full_name, birth_date, phone, insurance_no):
        super().__init__(full_name, birth_date, phone)
        self._insurance_no = insurance_no          # полис ОМС (UML: −)
        self._card = None                          # композиция: карта пациента

    @property
    def insurance_no(self):
        return self._insurance_no

    @property
    def card(self):
        """Медицинская карта пациента (может быть не заведена)."""
        return self._card

    def issue_card(self, card):
        """Завести медицинскую карту (у пациента она одна)."""
        if self._card is not None:
            raise ValueError("У пациента уже есть медицинская карта")
        self._card = card

    def make_appointment(self, doctor, when):
        """Записаться на приём к врачу (ассоциация: возвращает объект Приёма)."""
        return Appointment(when, self, doctor)

    def cancel_appointment(self, appointment, reason):
        """Отменить свою запись на приём."""
        appointment.cancel(reason)

    def get_history(self):
        """История обращений из медицинской карты."""
        if self._card is None:
            return []
        return self._card.get_history()
