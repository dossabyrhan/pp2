import string
from collections import Counter

# 1. Подсчёт гласных букв
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# 2. Удаление знаков препинания
def remove_punctuation(text):
    return "".join(char for char in text if char not in string.punctuation)

# 3. Подсчёт количества слов
def count_words(text):
    return len(text.split())

# 4. Подсчёт заглавных букв
def count_uppercase(text):
    return sum(1 for char in text if char.isupper())

# 5. Проверка на палиндром
def is_palindrome(text):
    cleaned_text = "".join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

# 6. Замена пробелов на "_"
def replace_spaces(text):
    return text.replace(" ", "_")

# 7. Самое длинное слово
def longest_word(text):
    words = text.split()
    return max(words, key=len) if words else ""

# 8. Удаление цифр из строки
def remove_digits(text):
    return "".join(char for char in text if not char.isdigit())

# 9. Подсчёт частоты букв
def count_letters(text):
    return dict(Counter(char for char in text if char.isalpha()))

# Тестовые примеры
test_text = "Hello, world! This is a test. 12345"

results = {
    "Гласные буквы": count_vowels(test_text),
    "Текст без знаков препинания": remove_punctuation(test_text),
    "Количество слов": count_words(test_text),
    "Количество заглавных букв": count_uppercase(test_text),
    "Является ли палиндромом": is_palindrome(test_text),
    "Пробелы заменены": replace_spaces(test_text),
    "Самое длинное слово": longest_word(test_text),
    "Текст без цифр": remove_digits(test_text),
    "Частота букв": count_letters(test_text),
}

import pandas as pd
df = pd.DataFrame(list(results.items()), columns=["Задача", "Результат"])
import ace_tools as tools
tools.display_dataframe_to_user(name="Результаты задач", dataframe=df)
