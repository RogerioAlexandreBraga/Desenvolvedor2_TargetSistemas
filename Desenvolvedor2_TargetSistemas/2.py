def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    
    return b == num or num == 0

# Solicitar um número do usuário
num = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))

# Verificar e exibir o resultado
if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
