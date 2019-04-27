import math
import datetime


def f(x, y):
    func = 2*x*(x-1) - (x + y)*(x + y + - 1)
    return func


def solve(y):
    """Решает уравнение относительно х при переборе у. Возвращает только положительные корни, т.к. квадратный корень из
    дискриминанта всегда больше по модулю, чем b"""
    a = 1
    b = -1 - 2*y
    c = y - y**2

    D = b*b - 4*a*c

    if D > 0:
        x1 = (-b + math.sqrt(D))/(2*a)
        #x2 = (-b - math.sqrt(D))/(2*a)
        # if (x1 > 0) and (x2 > 0):
        #     return x1, x2
        # elif (x1 > 0) and (x2 < 0):
        #     return x1
        # elif (x2 > 0) and (x1 < 0):
        #     return x2
        return x1
    if D == 0:
        x = (-b)/(2*a)
        return x
    if D < 0:
        return False


def is_int(x):
    """Проверяет, все ли элементы списка целые числа"""
    flag = 0
    for i in x:
        if not i.is_integer():
            flag = 1
    if flag > 0:
        return False
    else:
        return True


start = datetime.datetime.now()

y = 1
k = 0

arr_y = []
arr_x = []

dev = []

while k < 9:
    print("\r", end="")
    print(str(len(arr_y) + 1)+". ", "y = ", y, end="")
    t = solve(y)

    if t.is_integer():
        arr_y.append(y)
        arr_x.append(t)
        if len(arr_y) > 1:
            dev.append(arr_y[-1]/arr_y[-2])
            append_to = [t, dev[-1]]
        else:
            append_to = [t]
        k = k + 1
        print(append_to)
    y += 1

summ = 0


while summ < 10**12:
    before = arr_y[-1]*dev[-1]
    y1 = math.floor(before)
    print("\r", end="")
    print(str(len(arr_y) + 1)+". ", "before = ", before, "y = ", y1, "(округление по низу) ", end="")

    t = solve(y1)

    if t.is_integer():
        arr_y.append(y1)
        arr_x.append(t)
        dev.append(arr_y[-1]/arr_y[-2])
        append_to = [t, dev[-1]]
        print(append_to)
    else:
        y2 = math.ceil((arr_y[-1]*dev[-1]))
        print("\n  ", "y = ", y2, "(округление по верху) ", end="")
        t = solve(y2)

        if t.is_integer():
            arr_y.append(y2)
            arr_x.append(t)
            dev.append(arr_y[-1] / arr_y[-2])
            append_to = [t, dev[-1]]
            print(append_to)
    summ = arr_y[-1] + arr_x[-1]

stop = datetime.datetime.now()
ellapsed_time = stop - start
print("Вычисления закончены и заняли", ellapsed_time.seconds, "секунд.")
print("summ > 10*12 при х =", arr_x[-1], "y =", arr_y[-1], "sum =", summ)

