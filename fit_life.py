# Проект FitLife - MVP версия 1.0
print('Добро пожаловать в FitLife!')
user_name = input('Давайте познакомимся! Как Вас зовут?').title()
user_age = int(input('Отлично! Сколько Вам полных лет?'))
user_weight = float(input('Напишите Ваш вес в (кг.):'))
user_height = float(input('Ваш рост в метрах? (Например: 1.62):'))


def user_bmi():
    """Рассчитываем индекс массы тела"""
    bmi = user_weight / (user_height ** 2)
    return round(bmi, 1)


WATER_PER_KG = 30      # Убираем числа в константы
WATER_FROM_L_TO_ML = 1000


def water_needed():
    """Рассчитываем суточную норму воды"""
    water_ml = user_weight * WATER_PER_KG
    water_l = water_ml / WATER_FROM_L_TO_ML    # Переводим миллилитры в литры
    return round(water_l, 1)


print(f'Добро пожаловать, {user_name}!')
print(f'Ваш возраст: {user_age} лет')
print(f'Ваш индекс массы тела составляет: {user_bmi()}')
print(f'Ваша норма воды на день: {water_needed()}')
print('=' * 40)
print('Расчет окончен. Будьте здоровы!')
