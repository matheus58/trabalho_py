def verifica_parentheses(expressao):
    pilha = []
    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if len(pilha) == 0 or pilha[-1] != '(':
                return False
            pilha.pop()
    return len(pilha) == 0

# Testando a função
expressao1 = "(())"
expressao2 = "()()(()())"
expressao3 = "())"
expressao4 = "(()))"

print(verifica_parentheses(expressao1))  # Saída: True
print(verifica_parentheses(expressao2))  # Saída: True
print(verifica_parentheses(expressao3))  # Saída: False
print(verifica_parentheses(expressao4))  # Saída: False