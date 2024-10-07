def proximo_elemento():
    # a) 1, 3, 5, 7, ___
    seq_a = [1, 3, 5, 7]
    seq_a.append(seq_a[-1] + 2)  # Incremento de 2
    print(f"a) {seq_a}")

    # b) 2, 4, 8, 16, 32, 64, ____
    seq_b = [2, 4, 8, 16, 32, 64]
    seq_b.append(seq_b[-1] * 2)  # Multiplica por 2
    print(f"b) {seq_b}")

    # c) 0, 1, 4, 9, 16, 25, 36, ____
    seq_c = [0, 1, 4, 9, 16, 25, 36]
    seq_c.append(len(seq_c) ** 2)  # Quadrado perfeito
    print(f"c) {seq_c}")

    # d) 4, 16, 36, 64, ____
    seq_d = [4, 16, 36, 64]
    next_term = (len(seq_d) * 2 + 2) ** 2  # Quadrado de números pares
    seq_d.append(next_term)
    print(f"d) {seq_d}")

    # e) 1, 1, 2, 3, 5, 8, ____
    seq_e = [1, 1, 2, 3, 5, 8]
    seq_e.append(seq_e[-1] + seq_e[-2])  # Sequência de Fibonacci
    print(f"e) {seq_e}")

    # f) 2, 10, 12, 16, 17, 18, 19, ____
    seq_f = [2, 10, 12, 16, 17, 18, 19]
    seq_f.append(seq_f[-1] + 1)  # Incremento de 1
    print(f"f) {seq_f}")

# Chamada da função para exibir as sequências completas
proximo_elemento()
