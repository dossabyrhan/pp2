def reverse_string(text):
    reversed_text = []
    for char in text:
        reversed_text.insert(0, char)  # Добавляем символ в начало списка
    return "".join(reversed_text)

# Пример использования
print(reverse_string("Python"))  # Выведет: "nohtyP"
