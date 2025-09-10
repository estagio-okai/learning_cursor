# Documentação - Calculadora Simples

## Visão Geral
A `calculadora_simples.py` é uma calculadora avançada em Python que realiza operações matemáticas com precedência e parênteses. O programa oferece dois modos de operação: cálculo por expressão matemática e operações básicas individuais.

## Funcionalidades Principais

### 1. Cálculo por Expressão Matemática
- Suporta expressões complexas com precedência de operadores
- Permite uso de parênteses para agrupamento
- Exemplos suportados:
  - `9+2*3`
  - `(5+3)*2`
  - `10/2+3*4`
  - `(10+5)/(3*2)`

### 2. Operações Básicas
- Adição (+)
- Subtração (-)
- Multiplicação (*)
- Divisão (/)
- Validação de divisão por zero

## Estrutura do Código

### Constantes e Configurações
```python
OPERACOES_BASICAS: Dict[str, tuple]  # Mapeamento de operações básicas
RESPOSTAS_POSITIVAS = {'s', 'sim', 'y', 'yes'}  # Respostas positivas aceitas
PADRAO_EXPRESSAO = re.compile(r'^[0-9+\-*/().\s]+$')  # Regex para validação
```

### Funções Principais

#### `adicionar(a: float, b: float) -> float`
Soma dois números.

#### `subtrair(a: float, b: float) -> float`
Subtrai dois números.

#### `multiplicar(a: float, b: float) -> float`
Multiplica dois números.

#### `dividir(a: float, b: float) -> float`
Divide dois números com validação de divisão por zero.

#### `obter_expressao() -> Optional[str]`
Obtém uma expressão matemática válida do usuário com validação.

#### `validar_expressao(expressao: str) -> bool`
Valida se a expressão contém apenas caracteres permitidos e parênteses balanceados.

#### `processar_expressao(expressao: str) -> Union[int, float]`
Processa uma expressão matemática de forma segura usando `eval` controlado.

#### `exibir_menu() -> None`
Exibe o menu principal da calculadora.

#### `exibir_menu_antigo() -> None`
Exibe o menu de operações básicas.

#### `obter_numero(mensagem: str) -> float`
Obtém um número válido do usuário com tratamento de erro.

#### `formatar_resultado(resultado: Union[int, float]) -> Union[int, float]`
Formata o resultado removendo decimais desnecessários.

#### `perguntar_continuar(mensagem: str) -> bool`
Pergunta se o usuário quer continuar a operação.

#### `modo_expressao() -> None`
Gerencia o modo de cálculo por expressão matemática.

#### `modo_operacoes_basicas() -> None`
Gerencia o modo de operações básicas individuais.

#### `main() -> None`
Função principal que coordena o funcionamento da calculadora.

## Características de Segurança

### Validação de Entrada
- Verificação de caracteres permitidos
- Validação de parênteses balanceados
- Tratamento de divisão por zero
- Uso controlado de `eval` com namespace restrito

### Tratamento de Erros
- Captura de `KeyboardInterrupt` para cancelamento
- Tratamento de `ValueError` para entradas inválidas
- Tratamento de `ZeroDivisionError` para divisão por zero
- Tratamento de `SyntaxError` para expressões malformadas

## Uso

### Execução
```bash
python3 calculadora_simples.py
```

### Fluxo de Uso
1. O programa exibe o menu principal
2. Usuário escolhe entre:
   - Calcular expressão matemática
   - Operações básicas (modo antigo)
   - Sair
3. Após cada operação, pergunta se deseja continuar
4. Suporte a cancelamento com Ctrl+C

## Dependências
- Python 3.x
- Módulos padrão: `re`, `typing`

## Exemplos de Uso

### Expressões Matemáticas
```
Digite a expressão matemática: 9+2*3
Resultado: 9+2*3 = 15

Digite a expressão matemática: (5+3)*2
Resultado: (5+3)*2 = 16
```

### Operações Básicas
```
Escolha uma opção (1-5): 1
Digite o primeiro número: 10
Digite o segundo número: 5
Resultado da adição:
10.0 + 5.0 = 15
```

## Notas Técnicas
- O código utiliza type hints para melhor legibilidade
- Implementa princípios de clean code com funções pequenas e bem definidas
- Usa regex para validação eficiente de expressões
- Tratamento robusto de exceções em todos os pontos de entrada do usuário
