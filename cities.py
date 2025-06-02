import random

cities_file = open("russian_cities.txt", "r", encoding="utf-8")
cities = cities_file.read().split(", ")
cities = [city.strip() for city in cities if city.strip()]


def play_cities():
    used_cities = set()
    available_cities = [city.lower() for city in cities]
    last_letter = None
    
    print("Давайте играть в города! Вы начинаете.")
    print("Правила: называйте город на последнюю букву предыдущего города (кроме ъ, ы, ь).")
    print("Чтобы выйти, введите 'стоп'.")
    
    while True:
        user_city = input("Ваш город: ").strip().lower()

        if user_city == "стоп":
            print("Игра окончена. Спасибо за игру!")
            break

        if user_city in used_cities:
            print("Этот город уже был назван. Вы проиграли!")
            break

        if user_city.title() not in cities:
            print("Такого города нет в списке. Вы проиграли!")
            break

        if last_letter is not None and user_city[0] != last_letter:
            print(f"Город должен начинаться на букву '{last_letter}'. Вы проиграли!")
            break
            
        used_cities.add(user_city)
        available_cities.remove(user_city)

        last_char = user_city[-1]
        for char in reversed(user_city):
            if char not in ('ъ', 'ы', 'ь'):
                last_char = char
                break
        last_letter = last_char

        matching_cities = [city for city in available_cities if city[0] == last_letter]
        if not matching_cities:
            print("Я не знаю подходящего города. Вы победили!")
            break
        computer_city = random.choice(matching_cities)
        
        print(f"Мой город: {computer_city.title()}")
        used_cities.add(computer_city)
        available_cities.remove(computer_city)

        last_char = computer_city[-1]
        for char in reversed(computer_city):
            if char not in ('ъ', 'ы', 'ь'):
                last_char = char
                break
        last_letter = last_char

cities_file.close()

play_cities()