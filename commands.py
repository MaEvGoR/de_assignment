import math
import numpy as np

main_y = 2
main_x = 1
main_upper_x = 10
main_N = 10


def f(x, y):
    try:
        return (2 * (x ** 3)) + ((2 * y) / x)
    except:
        return ZeroDivisionError


def y(x, c1):
    return math.pow(x, 2) * (math.pow(x, 2) + c1)


def calculate_c1(y0, x0):
    try:
        return (y0 - math.pow(x0, 4)) / (math.pow(x0, 2))
    except:
        return ZeroDivisionError


def calculate(x0, y0, X, N):
    xs = [main_x]
    ys = [main_y]
    error_y = [0]
    total_error = [0]
    wrong_xs = []

    main_c1 = calculate_c1(y0, x0)
    step = 0.1

    for current_x in np.arange(x0, X, step):
        try:
            current_y = y(current_x, main_c1)
        except ZeroDivisionError:
            wrong_xs.append(current_x)
        else:
            xs.append(current_x)
            ys.append(current_y)
            error_y.append(0)
            total_error.append(0)

    return {'xs': xs, 'ys': ys, 'wx': wrong_xs, 'error': error_y, 'total_error':total_error}


def calculate_euler(x0, y0, X, N):
    deltax = (X - x0) / (N - 1)
    step = (X - x0) / N

    ys = [y0]
    xs = [x0]
    wrong_xs = []
    error_y = [0]
    total_error = [0]
    c1 = calculate_c1(y0, x0)

    for i in range(1, N + 1):
        try:
            ys.append(deltax * f(xs[i - 1], ys[i - 1]) + ys[i - 1])
            xs.append(xs[i - 1] + step)
            error_y.append(y(xs[i], c1) - ys[i])
            total_error.append(total_error[i - 1] + error_y[i - 1])
        except:
            break

    return {'xs': xs, 'ys': ys, 'wx': wrong_xs, 'error': error_y, 'total_error':total_error}


def calculate_imp_euler(x0, y0, X, N):
    step = (X - x0) / N

    ys = [y0]
    xs = [x0]
    wrong_xs = []
    error_y = [0]
    total_error = [0]
    c1 = calculate_c1(y0, x0)

    for i in range(1, N + 1):
        try:
            ys.append(ys[i - 1] + step * (
                    f(xs[i - 1], ys[i - 1]) + f(xs[i - 1] + step, ys[i - 1] + step * f(xs[i - 1], ys[i - 1]))) / 2)
            xs.append(xs[i - 1] + step)
            error_y.append(y(xs[i], c1) - ys[i])
            total_error.append(total_error[i - 1] + error_y[i - 1])
        except:
            break

    return {'xs': xs, 'ys': ys, 'wx': wrong_xs, 'error': error_y, 'total_error':total_error}


def calculate_runge(x0, y0, X, N):
    step = (X - x0) / N

    ys = [y0]
    xs = [x0]
    wrong_xs = []
    error_y = [0]
    total_error = [0]
    c1 = calculate_c1(y0, x0)

    for i in range(1, N + 1):
        try:
            k1 = f(xs[i - 1], ys[i - 1])
            k2 = f(xs[i - 1] + step / 2, ys[i - 1] + step * k1 / 2)
            k3 = f(xs[i - 1] + step / 2, ys[i - 1] + step * k2 / 2)
            k4 = f(xs[i - 1] + step, ys[i - 1] + step * k3)
            ys.append(ys[i - 1] + step * (k1 + 2 * k2 + 2 * k3 + k4) / 6)
            xs.append(xs[i - 1] + step)
            error_y.append(y(xs[i], c1) - ys[i])
            total_error.append(total_error[i - 1] + error_y[i - 1])
        except:
            break

    return {'xs': xs, 'ys': ys, 'wx': wrong_xs, "error": error_y, 'total_error':total_error}
