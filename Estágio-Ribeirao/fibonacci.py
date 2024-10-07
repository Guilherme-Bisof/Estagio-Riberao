def pertence_fibonacci(numero):
    # Inicializando os primeiros valores da sequência de Fibonacci
    fibonacci_seq = [0, 1]
    
    # Gerar a sequência até que o último número seja maior ou igual ao número informado
    while fibonacci_seq[-1] < numero:
        proximo_valor = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(proximo_valor)
    
    # Verifica se o número informado está na sequência
    if numero in fibonacci_seq:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} NÃO pertence à sequência de Fibonacci."


# Entrada do usuário
numero_informado = int(input("Informe um número: "))

# Chamada da função e exibição do resultado
resultado = pertence_fibonacci(numero_informado)
print(resultado)
