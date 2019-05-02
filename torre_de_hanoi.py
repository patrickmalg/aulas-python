def mover(o, d):
    print(o, "→", d)
def hanoi(n, o, d, a):
    if n > 0:
        hanoi(n-1, o, a, d)
        mover(o, d)
        hanoi(n-1, a, d, o)
hanoi(4, "A", "C", "B")