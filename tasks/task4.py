# tasks/task4.py

def solve():
    a, b, c = map(int, input().split())
    result = (a + b > c) and (a + c > b) and (b + c > a)
    print(result)

if __name__ == "__main__":
    solve()