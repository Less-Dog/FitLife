# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30      # Убираем числа в константы
WATER_FROM_L_TO_ML = 1000


def get_user_age():
    """Запрашивает возраст пользователя"""
    while True:
        try:
            user_age = int(input('Отлично! Сколько Вам лет?'))
            if user_age <= 0 or user_age > 130:     # Ограничение по возрасту
                raise ValueError
            return user_age
        except ValueError:
            print('Введите положительное целое число (Возраст от 1 до 130)')


def get_user_weight():
    """Запрашивает вес пользователя"""
    while True:
        try:
            user_weight = float(input('Напишите Ваш вес в (кг.)'))
            if user_weight <= 0 or user_weight > 350:  # разумный max вес
                raise ValueError
            return user_weight
        except ValueError:
            print('Введите положительное целое число от 0 до 300')


def get_user_height():
    """Запрашивает рост пользователя"""
    while True:
        try:
            user_height = float(input('Ваш рост в метрах? (например: 1.62)'))
            if user_height <= 0 or user_height > 2.7:    # Рост макс - 2.7 м.
                raise ValueError
            return user_height
        except ValueError:
            print('Пожалуйста, введите число от 0 до 2.7 (Пример: 1.62)')


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

    user_age = get_user_age()
    user_weight = get_user_weight()
    user_height = get_user_height()

    bmi = user_bmi(user_weight, user_height)
    water = water_needed(user_weight)
    print(f'Добро пожаловать, {user_name}!')
    print(f'Ваш возраст: {user_age} лет')
    print(f'Ваш индекс массы тела составляет: {bmi}')
    print(f'Ваша норма воды на день: {water} литров.')
    print('=' * 40)
    print('Расчет окончен. Будьте здоровы!')
