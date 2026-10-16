# Проект FitLife - MVP версия 1.0

#  Знакомства с пользователем.
print('Здравствуйте, как вас зовут?')
user_name = input('Введите ваше имя: ').title()
print('Добро пожаловать,', user_name)

#  Запрос от пользователя.
print('Введите ваш возраст, вес,рост.')
user_age = int(input('Ваш возраст: '))
user_weight = float(input('Ваш вес (в кг): '))
user_growth = float(input('Ваш рост (в метрах(1.67)): '))

#  разчитаем ИМТ.
bmi = user_weight / (user_growth ** 2)
rounding_bmi = round(bmi, 1)

#  Расчитаем норму воды в миллилитрах.
water_ml = user_weight * 30
water_l = water_ml / 1000

#  Выводим результат для пользователя.
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {rounding_bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print()
print('Расчет окончен. Будьте здоровы!')