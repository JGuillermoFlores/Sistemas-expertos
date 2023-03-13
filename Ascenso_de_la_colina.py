import numpy as np

def hill_climbing(f, x0, step_size, max_iterations):
    x = x0
    for i in range(max_iterations):
        fx = f(x)
        dx = step_size * np.random.randn(*x.shape)
        x_new = x + dx
        fx_new = f(x_new)
        if fx_new < fx:
            x = x_new
            fx = fx_new
        else:
            dx = -dx
            x_new = x + dx
            fx_new = f(x_new)
            if fx_new < fx:
                x = x_new
                fx = fx_new
            else:
                return x
    return x

# Ejemplo de uso
def f(x):
    return np.sum(x ** 2)

x0 = np.array([1.0, -2.0, 3.0])
step_size = 0.1
max_iterations = 100

x_opt = hill_climbing(f, x0, step_size, max_iterations)

print("El mínimo local encontrado es:", x_opt)
print("El valor mínimo encontrado es:", f(x_opt))
