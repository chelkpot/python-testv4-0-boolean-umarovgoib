def solve():
    a, b, c = map(int, input().split())
    x = a*a
    y = b*b  
    z = c*c
    print(x == y + z or y == x + z or z == x + y)

if __name__ == "__main__":
    solve()