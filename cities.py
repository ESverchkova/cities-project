cities = open("russian_cities.txt", "r", encoding="utf-8").read().split(", ")
cities = [city.strip() for city in cities if city.strip()]