import ply.lex as lex

# Lista de tokens (incluindo palavras-chave)
tokens = [
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
    'Less', 'great', 'equal', 'NEqual', 'GoE', 'LoE', 
    'Ecou', 'Dcou', 'collum', 'semiCollum', 'comma', 'atri','atri2','acess', 'ID', 'NUMBER'
] + [
    'BEGIN', 'END', 'WHILE', 'IF', 'ELSE', 'VAR', 'OF', 'WRITE', 'READ',
    'DO', 'THEN', 'TO', 'FOR', 'CONST', 'TYPE', 'INTEGER', 'REAL', 
    'CHAR', 'BOOLEAN', 'ARRAY', 'RECORD', 'AND', 'OR', 'TRUE', 'FALSE'
]

# Palavras-chave (mapeando para os tokens correspondentes)
keywords = {
    'begin': 'BEGIN',
    'end': 'END',
    'while': 'WHILE',
    'if': 'IF',
    'else': 'ELSE',
    'var': 'VAR',
    'of': 'OF',
    'write': 'WRITE',
    'read': 'READ',
    'do': 'DO',
    'then': 'THEN',
    'to': 'TO',
    'for': 'FOR',
    'const': 'CONST',
    'type': 'TYPE',
    'integer': 'INTEGER',
    'real': 'REAL',
    'char': 'CHAR',
    'boolean': 'BOOLEAN',
    'array': 'ARRAY',
    'record': 'RECORD',
    'and': 'AND',
    'or': 'OR',
    'true': 'TRUE',
    'false': 'FALSE'
}

# Expressões regulares para os tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\^'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_Less    = r'<'
t_great   = r'>'
t_equal   = r'=='
t_NEqual  = r'\!='
t_GoE     = r'>='
t_LoE     = r'<='
t_Ecou    = r'\['
t_Dcou    = r'\]'
t_collum  = r'\:'
t_semiCollum = r';'
t_comma   = r'\,'
t_atri    = r'\:\='
t_atri2   = r'\='
t_acess  =r'\.'

# Expressão regular para números (inteiros e reais)
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Expressão regular para identificadores e palavras-chave
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Verifica se é uma palavra-chave
    t.type = keywords.get(t.value, 'ID')  # Se não for uma palavra-chave, é um identificador
    return t

# Regra para ignorar espaços e tabulações
t_ignore = ' \t'

# Regra para lidar com quebras de linha (necessário para contar linhas)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regra para lidar com erros
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)
# Criar a instância do lexer
lexer = lex.lex()
# Função para tokenizar uma string de entrada
def tolkenizando(script):
    lexer.input(script)  # Alimentar o lexer com o script
    listaTolkens =[]
    # Iterar sobre os tokens gerados
    while True:
        tok = lexer.token()  # Obter o próximo token
        if not tok:
            break  # Quando nenhum token é encontrado, encerra.
        print(tok)
        listaTolkens.append(tok)
    return listaTolkens