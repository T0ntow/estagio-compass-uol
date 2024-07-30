def calcular_valor_maximo(operadores, operandos) -> float: # Definir as operações em um dicionário
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }
    
    # Combinar operadores e operandos usando zip
    combinados = zip(operadores, operandos)
    
    # Aplicar as operações aos operandos
    resultados = map(lambda op_pair: operacoes[op_pair[0]](op_pair[1][0], op_pair[1][1]), combinados)
    
    # Encontrar e retornar o maior valor
    return max(resultados)

# Testando a função
operadores = ['+','-','*','/','+']
operandos  = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

print(calcular_valor_maximo(operadores, operandos))  # Deve retornar 12
