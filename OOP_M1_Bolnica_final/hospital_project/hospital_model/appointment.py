"""Приём — центральный класс-событие предметной области.

UML: ассоциация (серая линия) с Пациентом, Врачом и МедицинскойКартой.
Приём хранит ссылки на участников, но не владеет ни одним из них:
все они существуют до и после приёма.
"""
from datetime import datetime


class Appointment:
    """Приём: дата/время, статус, диагноз и назначения."""

    def __init__(self, when, patient, doctor):
        self._when = when                 # плановый момент приёма
        self._patient = patient           # ассоциация: пациент
        self._doctor = doctor             # ассоциация: врач
        self._status = "запланирован"     # запланирован / завершён / отменён
        self._diagnosis = None            # результат приёма
        self._prescription = None         # назначения

    def reschedule(self, new_when):
        """Перенести приём на новое время (отменённый переносить нельзя)."""
        if self._status == "отменён":
            raise ValueError("Нельзя перенести отменённый приём")
        self._when = new_when

    def complete(self, diagnosis, prescription=None):
        """Завершить приём; запись автоматически попадает в карту пациента."""
        if self._status != "запланирован":
            raise ValueError("Завершить можно только запланированный приём")
        self._status = "завершён"
        self._diagnosis = diagnosis
        self._prescription = prescription
        if self._patient.card is not None:            # запись в медкарту
            self._patient.card.add_record(self)

    def cancel(self, reason):
        """Отменить приём с указанием причины."""
        if self._status == "завершён":
            raise ValueError("Нельзя отменить завершённый приём")
        self._status = f"отменён ({reason})"

    def describe(self):
        """Строка-описание приёма для карт и истории."""
        text = f"{self._when:%d.%m.%Y %H:%M} — {self._doctor.get_info()} — {self._status}"
        if self._diagnosis:
            text += f" — диагноз: {self._diagnosis}"
            if self._prescription:
                text += f" — назначения: {self._prescription}"
        return text
