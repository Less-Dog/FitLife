# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30      # Убираем числа в константы
WATER_FROM_L_TO_ML = 1000


def user_bmi(weight, height):
    """Рассчитываем индекс массы тела"""
    return round(weight / (height ** 2), 1)


def water_needed(weight):
    """Рассчитываем суточную норму воды"""
    water_ml = weight * WATER_PER_KG
    water_l = water_ml / WATER_FROM_L_TO_ML    # Переводим миллилитры в литры
    return round(water_l, 1)


if __name__ == "__main__":
    print('Добро пожаловать в FitLife!')
    user_name = input('Давайте познакомимся! Как Вас зовут?').title()
    user_age = int(input('Отлично! Сколько Вам полных лет?'))
    user_weight = float(input('Напишите Ваш вес в (кг.):'))
    user_height = float(input('Ваш рост в метрах? (Например: 1.62):'))

    bmi = user_bmi(user_weight, user_height)
    water = water_needed(user_weight)
    print(f'Добро пожаловать, {user_name}!')
    print(f'Ваш возраст: {user_age} лет')
    print(f'Ваш индекс массы тела составляет: {bmi}')
    print(f'Ваша норма воды на день: {water}')
    print('=' * 40)
    print('Расчет окончен. Будьте здоровы!')
