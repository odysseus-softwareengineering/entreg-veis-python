n = int(input())

for _ in range(n):
    texto = input()
    
    # 1ª passada: desloca letras 3 posições para a direita
    resultado = ""
    
    for c in texto:
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            resultado += chr(ord(c) + 3)
        else:
            resultado += c
    
    # 2ª passada: inverte a linha
    resultado = resultado[::-1]
    
    # 3ª passada: desloca metade dos caracteres 1 posição para a esquerda
    metade = len(resultado) // 2
    
    resultado_final = ""
    
    for i, c in enumerate(resultado):
        if i >= metade:
            resultado_final += chr(ord(c) - 1)
        else:
            resultado_final += c
    
    print(resultado_final)