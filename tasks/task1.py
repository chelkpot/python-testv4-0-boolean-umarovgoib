# tasks/task1.py

def solve():
    # Читаем одну строку и разбиваем на три числа
    a, b, c = map(int, input().split())
    print(a == b == c)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()