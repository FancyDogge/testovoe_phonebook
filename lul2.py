numbers = input()
A, B, C, D = map(int, numbers.split())
mb_need = B - D
expenses = A if mb_need >= 0 else A + abs(mb_need) * C
print(expenses)