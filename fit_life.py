# Импортируем модуль datetime.
import datetime as dt


# Константы.
WATER_INTAKE_PER_KG = 30
MILLILITERS_IN_LITER = 1000
BMI_ROUND_DIGITS = 1
DATETIME_FORMAT = "%d.%m.%Y %H:%M:%S"


# Знакомство с пользователем.
print("Здравствуйте, как вас зовут?")
user_name = input("Введите ваше имя: ").title()

print("Добро пожаловать,", user_name)

# Запрос данных пользователя.
print("Введите ваш возраст, вес и рост.")

user_age = int(input("Ваш возраст: "))
user_weight = float(
    input("Ваш вес (в кг): ").replace(",", ".")
)
user_height = float(
    input("Ваш рост (в метрах, например 1.67): ").replace(",", ".")
)

# Рассчитываем ИМТ.
bmi = user_weight / (user_height ** 2)
rounded_bmi = round(bmi, BMI_ROUND_DIGITS)

# Рассчитываем норму воды в миллилитрах.
water_ml = user_weight * WATER_INTAKE_PER_KG
water_l = water_ml / MILLILITERS_IN_LITER

# Выводим результат для пользователя.
print(f"Отчет для пользователя: {user_name} ({user_age} лет)")
print(f"Твой индекс массы тела: {rounded_bmi}")
print(f"Рекомендуемая норма воды: {water_l} л в день")

print()
print("Расчет окончен.")

# Выводим текущую дату и время.
current_datetime = dt.datetime.now()
print(
    f"Дата и время расчета: "
    f"{current_datetime:{DATETIME_FORMAT}}"
)

print()
print("Будьте здоровы!")
