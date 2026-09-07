import math
import matplotlib.pyplot as plt


def bisection(f, a, b, decimals):
    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a

    if fb == 0:
        return b

    if fa * fb > 0:
        return None

    # Use a little more precision than the answer needs
    tolerance = 10 ** (-(decimals + 3))

    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        fc = f(c)

        if fc == 0:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2


# Problem 1
f1a = lambda x: x**3 - 9
f1b = lambda x: 3*x**3 + x**2 - x - 5
f1c = lambda x: math.cos(x)**2 + 6 - x

# Problem 2
f2a = lambda x: x**5 + x - 1
f2b = lambda x: math.sin(x) - 6*x - 5
f2c = lambda x: math.log(x) + x**2 - 3


# Problem 3
def f3a(x):
    return 2*x**3 - 6*x - 1


def f3b(x):
    return math.exp(x - 2) + x**3 - x


def f3c(x):
    return 1 + 5*x - 6*x**3 - math.exp(2*x)


def make_x_values(start, end, amount=600):
    gap = (end - start) / (amount - 1)
    return [start + i * gap for i in range(amount)]


def show_graph(title, f, start, end, roots):
    x_values = make_x_values(start, end)
    y_values = [f(x) for x in x_values]

    plt.figure()
    plt.plot(x_values, y_values)
    plt.axhline(0)
    plt.scatter(roots, [0] * len(roots))

    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    # Problems 1 and 2
    p1a = bisection(f1a, 2, 3, 6)
    p1b = bisection(f1b, 1, 2, 6)
    p1c = bisection(f1c, 6, 7, 6)

    p2a = bisection(f2a, 0, 1, 8)
    p2b = bisection(f2b, -1, 0, 8)
    p2c = bisection(f2c, 1, 2, 8)

    # Problem 3
    p3a_1 = bisection(f3a, -2, -1, 6)
    p3a_2 = bisection(f3a, -1, 0, 6)
    p3a_3 = bisection(f3a, 1, 2, 6)

    p3b_1 = bisection(f3b, -1.5, -0.5, 6)
    p3b_2 = bisection(f3b, -0.5, 0.5, 6)
    p3b_3 = bisection(f3b, 0.5, 1.5, 6)

    p3c_1 = bisection(f3c, -1.5, -0.5, 6)
    p3c_2 = bisection(f3c, -0.5, 0.5, 6)
    p3c_3 = bisection(f3c, 0.25, 1.25, 6)

    print("\nBISECTION METHOD - FINAL ANSWERS")
    print("=" * 42)

    print("\nProblem 1")
    print(f"1(a) x^3 = 9                 : {p1a:.6f}")
    print(f"1(b) 3x^3 + x^2 = x + 5     : {p1b:.6f}")
    print(f"1(c) cos^2(x) + 6 = x        : {p1c:.6f}")

    print("\nProblem 2")
    print(f"2(a) x^5 + x = 1             : {p2a:.8f}")
    print(f"2(b) sin(x) = 6x + 5         : {p2b:.8f}")
    print(f"2(c) ln(x) + x^2 = 3         : {p2c:.8f}")

    print("\nProblem 3")
    print("3(a) 2x^3 - 6x - 1 = 0")
    print("      intervals: [-2,-1], [-1,0], [1,2]")
    print(f"      roots: {p3a_1:.6f}, {p3a_2:.6f}, {p3a_3:.6f}")

    print("\n3(b) e^(x-2) + x^3 - x = 0")
    print("      intervals: [-1.5,-0.5], [-0.5,0.5], [0.5,1.5]")
    print(f"      roots: {p3b_1:.6f}, {p3b_2:.6f}, {p3b_3:.6f}")

    print("\n3(c) 1 + 5x - 6x^3 - e^(2x) = 0")
    print("      intervals: [-1.5,-0.5], [-0.5,0.5], [0.25,1.25]")
    print(f"      roots: {p3c_1:.6f}, {p3c_2:.6f}, {p3c_3:.6f}")

    print("\nClose each graph window to view the next graph.")

    show_graph(
        "Problem 3(a): 2x^3 - 6x - 1",
        f3a,
        -2.5,
        2.5,
        [p3a_1, p3a_2, p3a_3]
    )

    show_graph(
        "Problem 3(b): e^(x-2) + x^3 - x",
        f3b,
        -1.8,
        1.5,
        [p3b_1, p3b_2, p3b_3]
    )

    show_graph(
        "Problem 3(c): 1 + 5x - 6x^3 - e^(2x)",
        f3c,
        -1.5,
        1.2,
        [p3c_1, p3c_2, p3c_3]
    )


if __name__ == "__main__":
    main()