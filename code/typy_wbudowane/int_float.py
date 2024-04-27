import math
import random

float_digits = []
int_digits = []

for _ in range(0, 6):
    float_digits.append(random.uniform(-20, 20))

for _ in range(0, 3):
    int_digits.append(random.randint(1, 10))

print("Liczby float:", float_digits)
print("Liczby int:", int_digits)

float_digits[0] = round(float_digits[0])
float_digits[1] = math.ceil(float_digits[1])
float_digits[2] = math.floor(float_digits[2])

print("Liczby float (3 pierwsze po zaokrągleniu):", float_digits)

for index_int, index_float in enumerate(range(3,6)):
    float_digits[index_float] = math.pow(float_digits[index_float], int_digits[index_int])

print("Liczby float (po całym przetworzeniu):", float_digits)
