"""Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление. Функцию hex используйте
для проверки своего результата."""

num = int(input("Введите целое число: "))
hex_str = hex(num)[2:]
print("Шестнадцатеричное представление: " + hex_str)

print(hex(num))