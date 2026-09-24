"""Демонстрация объектной модели «Больница» (ООП, Модуль 1).

Запуск:  python main.py

Сценарий показывает все связи диаграммы классов:
композицию, агрегацию, ассоциации, обобщение и полиморфизм.
"""
from datetime import date, datetime

from hospital_model import Doctor, Hospital, MedicalCard, Nurse, Patient


def header(title):
    print()
    print("=" * 68)
    print(title)
    print("=" * 68)


def main():
    # ── 1. Больница и отделения ──────────────────────────────────────────
    header("1. Больница и отделения — КОМПОЗИЦИЯ (больница владеет отделениями)")
    hospital = Hospital("Городская больница №1", "г. Петропавловск, ул. Мира, 5")
    therapy = hospital.add_department("Терапевтическое", "Корпус А, 2 этаж")
    surgery = hospital.add_department("Хирургическое", "Корпус Б, 1 этаж")
    print(f"Создана больница: {hospital.name}")
    print(f"  отделение 1: {therapy.name} ({therapy._location})")
    print(f"  отделение 2: {surgery.name} ({surgery._location})")

    # ── 2. Персонал ──────────────────────────────────────────────────────
    header("2. Персонал — АГРЕГАЦИЯ (сотрудники созданы вне отделения)")
    doctor = Doctor("Иванов А.С.", date(1980, 5, 12), "+7 700 111-22-33",
                    "В-101", 15, "терапевт", "высшая")
    surgeon = Doctor("Петров В.К.", date(1975, 11, 2), "+7 700 222-33-44",
                     "В-102", 20, "хирург", "высшая")
    nurse = Nurse("Смирнова Е.П.", date(1990, 9, 3), "+7 700 444-55-66",
                  "М-205", 7, "терапия", "дневная")

    therapy.attach_staff(doctor)      # агрегация: объекты приходят извне
    therapy.attach_staff(nurse)
    surgery.attach_staff(surgeon)

    for dept in (therapy, surgery):
        print(f"Расписание «{dept.name}»:")
        for line in dept.schedule():  # полиморфизм get_info()
            print(f"  - {line}")

    # ── 3. Пациент и медицинская карта ───────────────────────────────────
    header("3. Пациент и медкарта — КОМПОЗИЦИЯ (карта принадлежит пациенту)")
    patient = Patient("Бахтагареев М.Р.", date(2005, 4, 21),
                      "+7 700 777-88-99", "123456789012")
    patient.issue_card(MedicalCard("К-000123", date.today()))
    print(f"Пациент: {patient.get_contacts()}, возраст: {patient.get_age()}")
    print(f"Полис ОМС: {patient.insurance_no}, карта №: {patient.card.number}")

    # ── 4. Запись и проведение приёма ────────────────────────────────────
    header("4. Приём — АССОЦИАЦИЯ (пациент + врач, результат — в карту)")
    appt = patient.make_appointment(doctor, datetime(2026, 9, 20, 10, 30))
    print(f"Записан на приём: {appt.describe()}")
    nurse_line = nurse.prepare_room(therapy)
    print(nurse_line)
    doctor.conduct_appointment(appt, "ОРВИ", "Постельный режим, обильное питьё")
    print(f"Приём проведён: {appt.describe()}")

    # ── 5. Перенос и отмена приёма ───────────────────────────────────────
    header("5. Перенос и отмена — статус меняют методы самого приёма")
    appt2 = patient.make_appointment(surgeon, datetime(2026, 9, 24, 14, 0))
    appt2.reschedule(datetime(2026, 9, 26, 9, 30))
    print(f"Перенесён:  {appt2.describe()}")
    appt3 = patient.make_appointment(doctor, datetime(2026, 10, 1, 11, 0))
    patient.cancel_appointment(appt3, "выздоровел")
    print(f"Отменён:    {appt3.describe()}")

    # ── 6. История обращений ─────────────────────────────────────────────
    header("6. История обращений пациента (из медицинской карты)")
    for record in patient.get_history():
        print(f"  * {record}")

    # ── 7. Поиск врачей и статистика ─────────────────────────────────────
    header("7. Поиск врачей и статистика больницы")
    print("Терапевты больницы:")
    for doc in hospital.find_doctors("терапевт"):
        print(f"  - {doc.get_info()}")
    print("Статистика:")
    for key, value in hospital.get_statistics().items():
        print(f"  {key}: {value}")

    # ── 8. Полиморфизм через общий тип ───────────────────────────────────
    header("8. Полиморфизм: единый вызов get_info() для разных классов")
    for person in (doctor, surgeon, nurse):
        print(f"  {person.get_info()}")
    print()
    print("Демонстрация завершена успешно.")


if __name__ == "__main__":
    main()
