#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Avançada
Realiza operações matemáticas com precedência e parênteses
Suporta expressões como: 9+2*3, (5+3)*2, 10/2+3*4, etc.
"""

import re
from typing import Optional, Union, Dict, Callable

# Constantes para melhor manutenibilidade
OPERACOES_BASICAS: Dict[str, tuple] = {
    "1": ("adição", "+", lambda a, b: a + b),
    "2": ("subtração", "-", lambda a, b: a - b),
    "3": ("multiplicação", "*", lambda a, b: a * b),
    "4": ("divisão", "/", lambda a, b: a / b if b != 0 else _raise_divisao_zero())
}

RESPOSTAS_POSITIVAS = {'s', 'sim', 'y', 'yes'}
PADRAO_EXPRESSAO = re.compile(r'^[0-9+\-*/().\s]+$')
PADRAO_OPERADORES = re.compile(r'[+\-*/]')
PADRAO_ESPACOS = re.compile(r'\s+')
CARACTERES_PERMITIDOS = set('0123456789+-*/().')

def _raise_divisao_zero() -> None:
    """Helper para divisão por zero"""
    raise ValueError("Erro: Divisão por zero não é permitida!")

def adicionar(a: float, b: float) -> float:
    """Soma dois números"""
    return a + b

def subtrair(a: float, b: float) -> float:
    """Subtrai dois números"""
    return a - b

def multiplicar(a: float, b: float) -> float:
    """Multiplica dois números"""
    return a * b

def dividir(a: float, b: float) -> float:
    """Divide dois números"""
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida!")
    return a / b

def obter_expressao() -> Optional[str]:
    """Obtém uma expressão matemática válida do usuário"""
    while True:
        try:
            expressao = input("Digite a expressão matemática: ").strip()
            if not expressao:
                print("Erro: Por favor, digite uma expressão!")
                continue
            
            if validar_expressao(expressao):
                return expressao
            print("Erro: Expressão inválida! Use apenas números, operadores (+, -, *, /) e parênteses.")
                
        except KeyboardInterrupt:
            print("\nOperação cancelada.")
            return None

def validar_expressao(expressao: str) -> bool:
    """Valida se a expressão contém apenas caracteres permitidos"""
    if not PADRAO_EXPRESSAO.match(expressao):
        return False
    
    if not PADRAO_OPERADORES.search(expressao):
        return False
    
    # Verificar parênteses balanceados de forma mais eficiente
    contador = 0
    for char in expressao:
        if char == '(':
            contador += 1
        elif char == ')':
            contador -= 1
            if contador < 0:
                return False
    
    return contador == 0

def processar_expressao(expressao: str) -> Union[int, float]:
    """Processa uma expressão matemática de forma segura"""
    try:
        # Limpar e normalizar a expressão
        expressao_limpa = PADRAO_ESPACOS.sub('', expressao).replace('×', '*').replace('÷', '/')
        
        # Verificação de segurança mais eficiente
        if not all(c in CARACTERES_PERMITIDOS for c in expressao_limpa):
            raise ValueError("Expressão contém caracteres inválidos")
        
        # Usar eval de forma controlada
        resultado = eval(expressao_limpa, {"__builtins__": {}}, {})
        return resultado
        
    except ZeroDivisionError:
        raise ValueError("Erro: Divisão por zero não é permitida!")
    except SyntaxError:
        raise ValueError("Erro: Sintaxe da expressão inválida!")
    except Exception as e:
        raise ValueError(f"Erro ao processar expressão: {str(e)}")

def exibir_menu() -> None:
    """Exibe o menu principal"""
    menu = [
        "="*50,
        "           CALCULADORA AVANÇADA",
        "="*50,
        "1. Calcular expressão matemática",
        "2. Operações básicas (modo antigo)",
        "3. Sair",
        "="*50,
        "Exemplos de expressões:",
        "• 9+2*3",
        "• (5+3)*2", 
        "• 10/2+3*4",
        "• (10+5)/(3*2)",
        "="*50
    ]
    print("\n".join(menu))

def exibir_menu_antigo() -> None:
    """Exibe o menu de operações básicas"""
    menu = [
        "="*40,
        "        OPERAÇÕES BÁSICAS",
        "="*40,
        "1. Adição (+)",
        "2. Subtração (-)",
        "3. Multiplicação (*)",
        "4. Divisão (/)",
        "5. Voltar ao menu principal",
        "="*40
    ]
    print("\n".join(menu))

def obter_numero(mensagem: str) -> float:
    """Obtém um número válido do usuário"""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Por favor, digite um número válido!")

def formatar_resultado(resultado: Union[int, float]) -> Union[int, float]:
    """Formata o resultado removendo decimais desnecessários"""
    return int(resultado) if resultado == int(resultado) else resultado

def perguntar_continuar(mensagem: str) -> bool:
    """Pergunta se o usuário quer continuar"""
    resposta = input(f"\n{mensagem} (s/n): ").strip().lower()
    return resposta in RESPOSTAS_POSITIVAS

def modo_expressao() -> None:
    """Modo de cálculo por expressão matemática"""
    while True:
        try:
            expressao = obter_expressao()
            if expressao is None:
                return
            
            resultado = processar_expressao(expressao)
            resultado_formatado = formatar_resultado(resultado)
            
            print(f"\nResultado: {expressao} = {resultado_formatado}")
            
            if not perguntar_continuar("Deseja calcular outra expressão?"):
                break
                
        except ValueError as e:
            print(f"\n{e}")
            if not perguntar_continuar("Deseja tentar novamente?"):
                break
        except KeyboardInterrupt:
            print("\nOperação cancelada.")
            break

def modo_operacoes_basicas() -> None:
    """Modo de operações básicas (modo antigo)"""
    while True:
        exibir_menu_antigo()
        
        try:
            opcao = input("Escolha uma opção (1-5): ").strip()
            
            if opcao == "5":
                break
            elif opcao in OPERACOES_BASICAS:
                operacao, simbolo, funcao = OPERACOES_BASICAS[opcao]
                
                # Obter os números
                num1 = obter_numero("Digite o primeiro número: ")
                num2 = obter_numero("Digite o segundo número: ")
                
                try:
                    resultado = funcao(num1, num2)
                    resultado_formatado = formatar_resultado(resultado)
                    
                    print(f"\nResultado da {operacao}:")
                    print(f"{num1} {simbolo} {num2} = {resultado_formatado}")
                    
                    if not perguntar_continuar("Deseja fazer outra operação?"):
                        break
                        
                except ValueError as e:
                    print(f"\n{e}")
                    continue
            else:
                print("Erro: Opção inválida! Escolha entre 1 e 5.")
                
        except KeyboardInterrupt:
            print("\nOperação cancelada.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")

def main() -> None:
    """Função principal da calculadora"""
    print("Bem-vindo à Calculadora Avançada!")
    
    modos = {
        "1": modo_expressao,
        "2": modo_operacoes_basicas
    }
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("Escolha uma opção (1-3): ").strip()
            
            if opcao == "3":
                print("Obrigado por usar a calculadora! Até logo!")
                break
            elif opcao in modos:
                modos[opcao]()
            else:
                print("Erro: Opção inválida! Escolha entre 1 e 3.")
                
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
