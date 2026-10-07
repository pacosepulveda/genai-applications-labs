import torch

# Parte A — cálculo manual
x = 2.0
y = 7.0
w = 1.0
b = 0.5
lr = 0.05

y_hat = w * x + b
loss = (y_hat - y) ** 2

# dL/dy_hat = 2 * (y_hat-y)
dL_dy_hat = 2 * (y_hat - y)
dL_dw = dL_dy_hat * x
dL_db = dL_dy_hat

w_new = w - lr * dL_dw
b_new = b - lr * dL_db

print("predicción:", y_hat)
print("loss:", loss)
print("gradientes manuales:", dL_dw, dL_db)
print("nuevos parámetros:", w_new, b_new)

# Parte B — autograd
x_t = torch.tensor(2.0)
y_t = torch.tensor(7.0)
w_t = torch.tensor(1.0, requires_grad=True)
b_t = torch.tensor(0.5, requires_grad=True)

y_hat_t = w_t * x_t + b_t
loss_t = (y_hat_t - y_t) ** 2
loss_t.backward()

print("gradientes autograd:", w_t.grad.item(), b_t.grad.item())

assert abs(w_t.grad.item() - dL_dw) < 1e-6
assert abs(b_t.grad.item() - dL_db) < 1e-6

# Ampliación — varias iteraciones
w_t = torch.tensor(1.0, requires_grad=True)
b_t = torch.tensor(0.5, requires_grad=True)
history = []

for step in range(8):
    y_hat_t = w_t * x_t + b_t
    loss_t = (y_hat_t - y_t) ** 2
    loss_t.backward()

    history.append({
        "step": step,
        "w": w_t.item(),
        "b": b_t.item(),
        "prediction": y_hat_t.item(),
        "loss": loss_t.item(),
    })

    with torch.no_grad():
        w_t -= lr * w_t.grad
        b_t -= lr * b_t.grad

    w_t.grad.zero_()
    b_t.grad.zero_()

print(history)
