"""Больница и Отделение.

UML: Больница — Отделение — композиция (закрашенный ромб): отделение
создаётся только методом больницы и не существует вне её.
Отделение — МедицинскийПерсонал — агрегация (пустой ромб): сотрудники
закрепляются, но создаются вне отделения и переживают его расформирование.
"""
from .staff import Doctor


class Department:
    """Отделение: название, расположение и закреплённый персонал."""

    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._staff = []                 # агрегация: объекты приходят извне

    @property
    def name(self):
        return self._name

    def attach_staff(self, person):
        """Закрепить сотрудника за отделением (не создаёт его!)."""
        self._staff.append(person)

    def schedule(self):
        """Расписание: единый формат через полиморфный get_info()."""
        return [s.get_info() for s in self._staff]

    @property
    def staff(self):
        """Кортеж сотрудников (защита списка от изменения извне)."""
        return tuple(self._staff)


class Hospital:
    """Больница: название, адрес и принадлежащие ей отделения."""

    def __init__(self, name, address):
        self._name = name
        self._address = address
        self._departments = []           # композиция: отделение рождается здесь

    @property
    def name(self):
        return self._name

    def add_department(self, name, location):
        """Добавить отделение — объект создаётся внутри больницы (композиция)."""
        dept = Department(name, location)
        self._departments.append(dept)
        return dept

    def find_doctors(self, specialty):
        """Найти врачей заданной специальности по всем отделениям."""
        specialty = specialty.lower()
        found = []
        for dept in self._departments:
            for person in dept.staff:
                if isinstance(person, Doctor) and person.specialty.lower() == specialty:
                    found.append(person)
        return found

    def get_statistics(self):
        """Сводка: отделения и сотрудники по категориям."""
        staff = [p for d in self._departments for p in d.staff]
        doctors = sum(1 for p in staff if isinstance(p, Doctor))
        return {
            "Отделений": len(self._departments),
            "Сотрудников": len(staff),
            "Врачей": doctors,
            "Медсестёр": len(staff) - doctors,
        }
