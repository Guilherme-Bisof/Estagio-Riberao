import time

# Função para simular o estado das lâmpadas baseado nos interruptores
def identificar_lampadas():
    # Inicializa os estados dos interruptores (False = desligado, True = ligado)
    interruptor_1 = False
    interruptor_2 = False
    interruptor_3 = False
    
    # Inicializa os estados das lâmpadas (False = apagada, True = acesa)
    lampada_1 = False
    lampada_2 = False
    lampada_3 = False
    
    # Simulando o uso da estratégia:

    # 1. Ligue o Interruptor 1 e deixe por alguns minutos (simulado com sleep)
    interruptor_1 = True
    print("Ligando o Interruptor 1 por algum tempo...")
    time.sleep(2)  # Simula o tempo necessário para esquentar a lâmpada
    lampada_1 = True  # Lampada 1 aquece e depois será desligada
    
    # 2. Desligue o Interruptor 1 e ligue o Interruptor 2
    interruptor_1 = False
    interruptor_2 = True
    print("Desligando o Interruptor 1 e ligando o Interruptor 2.")
    lampada_1 = False  # Lampada 1 fica apagada, mas estará quente
    lampada_2 = True  # Lampada 2 ficará acesa

    # 3. Deixe o Interruptor 3 desligado o tempo todo
    # Lampada 3 ficará apagada e fria

    # 4. Agora simulamos a "ida" à sala e verificamos o estado das lâmpadas

    # Criando as condições da sala das lâmpadas
    estado_lampada_1 = "quente" if not lampada_1 else "acesa"
    estado_lampada_2 = "acesa" if lampada_2 else "apagada"
    estado_lampada_3 = "fria"

    # 5. Identificar qual interruptor controla qual lâmpada
    if estado_lampada_1 == "quente":
        print("A Lâmpada 1 está quente, então é controlada pelo Interruptor 1.")
    if estado_lampada_2 == "acesa":
        print("A Lâmpada 2 está acesa, então é controlada pelo Interruptor 2.")
    if estado_lampada_3 == "fria":
        print("A Lâmpada 3 está fria, então é controlada pelo Interruptor 3.")

# Chamada da função para identificar qual interruptor controla cada lâmpada
identificar_lampadas()
