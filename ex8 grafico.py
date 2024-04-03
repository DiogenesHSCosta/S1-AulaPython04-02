import matplotlib.pyplot as plt

def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

n = 19 # Número de termos da sequência de Fibonacci a serem gerados
fib_seq = fibonacci(n)

plt.plot(fib_seq, marker='o')
plt.title('Sequência de Fibonacci')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.show()
