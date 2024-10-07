def verifica_letra_a(texto):
    # Converte o texto para minúsculas e conta o número de ocorrências de 'a'
    contagem_a = texto.lower().count('a')
    
    if contagem_a > 0:
        return f"A letra 'a' aparece {contagem_a} vez(es) na string."
    else:
        return "A letra 'a' não está presente na string."


# Entrada do usuário
string_informada = input("Informe uma string: ")

# Chamada da função e exibição do resultado
resultado = verifica_letra_a(string_informada)
print(resultado)
