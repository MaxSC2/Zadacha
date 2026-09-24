"""Медицинский персонал: абстрактный родитель + Врач и Медсестра.

UML: обобщение (MedicalStaff -> Person, Doctor/Nurse -> MedicalStaff).
Полиморфизм: каждый наследник возвращает свою строку в get_info().
"""
from .person import Person


class MedicalStaff(Person):
    """Общий родитель врача и медсестры: табельный номер и стаж."""

    def __init__(self, full_name, birth_date, phone, staff_no, exp):
        super().__init__(full_name, birth_date, phone)
        self._staff_no = staff_no        # табельный номер (UML: #)
        self._experience = exp           # стаж работы в годах

    def get_info(self):
        """Абстрактный метод — переопределяется в наследниках."""
        raise NotImplementedError("Метод get_info() должен быть переопределён")


class Doctor(MedicalStaff):
    """Врач: специальность и категория; проводит приёмы (ассоциация с Приёмом)."""

    def __init__(self, full_name, birth_date, phone, staff_no, exp,
                 specialty, category="без категории"):
        super().__init__(full_name, birth_date, phone, staff_no, exp)
        self._specialty = specialty      # профиль врачебной деятельности
        self._category = category        # квалификационная категория
        self._appointments = []          # проведённые приёмы

    @property
    def specialty(self):
        return self._specialty

    def get_info(self):                              # полиморфизм
        return f"Врач {self._full_name} ({self._specialty})"

    def conduct_appointment(self, appointment, diagnosis, prescription=None):
        """Провести приём: поставить диагноз и выписать назначения."""
        appointment.complete(diagnosis, prescription)
        self._appointments.append(appointment)

    @property
    def appointments(self):
        """Кортеж проведённых приёмов (защита списка от изменения извне)."""
        return tuple(self._appointments)


class Nurse(MedicalStaff):
    """Медсестра: профиль работы и смена; помощник врача."""

    def __init__(self, full_name, birth_date, phone, staff_no, exp, profile, shift="дневная"):
        super().__init__(full_name, birth_date, phone, staff_no, exp)
        self._profile = profile          # направление работы
        self._shift = shift              # график дежурств

    def get_info(self):                              # полиморфизм
        return f"Медсестра {self._full_name} ({self._profile}, {self._shift} смена)"

    def prepare_room(self, department):
        """Подготовить кабинет отделения к приёму."""
        return f"{self._full_name} готовит кабинет ({department.name})"

    def escort_patient(self, patient):
        """Сопроводить пациента к кабинету."""
        return f"{self._full_name} сопровождает пациента {patient.full_name}"
