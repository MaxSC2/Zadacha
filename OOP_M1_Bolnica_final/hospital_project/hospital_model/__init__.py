"""Объектная модель учёта пациентов и медицинских приёмов в больнице.

Модуль 1 по объектно-ориентированному программированию.
Группа ИСУ-24-1: Бахтагареев М.Р., Добош Н.

Состав модели (9 классов):
    Person, Patient, MedicalStaff, Doctor, Nurse,
    Hospital, Department, MedicalCard, Appointment

Типы связей на диаграмме классов:
    обобщение   — Person -> Patient/MedicalStaff, MedicalStaff -> Doctor/Nurse
    композиция  — Hospital -> Department, Patient -> MedicalCard
    агрегация   — Department -> MedicalStaff
    ассоциация  — Patient — Appointment, Doctor — Appointment,
                  Appointment -> MedicalCard (запись о приёме)
"""
from .appointment import Appointment
from .hospital import Department, Hospital
from .medical_card import MedicalCard
from .patient import Patient
from .person import Person
from .staff import Doctor, MedicalStaff, Nurse

__all__ = [
    "Person", "Patient", "MedicalStaff", "Doctor", "Nurse",
    "Hospital", "Department", "MedicalCard", "Appointment",
]
