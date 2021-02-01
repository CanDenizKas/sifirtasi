import numpy as np
arr = [int(item) for item in input("Sayilari giriniz ").split()]
zeros = [i for i in arr if i == 0]
arr = [i for i in arr if i != 0]
zeros.extend(arr)
print(zeros)
