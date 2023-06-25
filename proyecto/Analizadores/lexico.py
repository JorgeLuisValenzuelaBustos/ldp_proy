import ply.lex as lex

# List of tokens.
tokens = [
    # Inicio del aporte P@B por Paul Bustos M.
    'SEMICOLON',
    'COLON',
    'LBRACE',
    'RBRACE',
    'BRACES',
    'COMMA',
    'DOT',
    'GREATER_THAN',
    # 'DIAMOND_OPERATOR',
    'EQUAL',
    'PLUS',
    'MINUS',
    'TIMES',
    # 'PLUS_EQUAL',
    # 'MINUS_EQUAL',
    'APOSTROPHE',
    'LPARENTHESE',
    'RPARENTHESE',
    'SLASH',
    'BACKSLASH',
    'ID',
    # 'DIGIT',
    'NONDIGIT',
    'NUMBER',
    # Fin aporte P@B
    # Inicio del aporte de Jorge Luis Valenzuela Bustos.
    'DOBLEIGUAL',
    'MENOR',
    'MENORIGUAL',
    "CADENA",
    "FLOTANTE",
    "ENTERO",
    "LBRACKET",
    "RBRACKET",
    # Fin aporte
]

reserved = {
    # Inicio del aporte P@B de Paul Bustos M.
    'import': 'IMPORT',
    'set': 'SET',
    'static': 'STATIC',
    'typedef': 'TYPEDEF',
    'int': 'INT',
    'double': 'DOUBLE',
    'num': 'NUM',
    'String': 'STRING',
    'bool': 'BOOL',
    'true': 'TRUE',
    'false': 'FALSE',
    'dynamic': 'DYNAMIC',
    'new': 'NEW',
    'const': 'CONST',
    # Fin aporte P@B
    # Inicio del aporte de Jorge Luis Valenzuela Bustos.
    'null': 'NULL',
    'return': 'RETURN',
    'this': 'THIS',
    'var': 'VAR',
    'while': 'WHILE',
    'List': 'LISTA',
    'Set': 'CONJUNTO',
    'Map': 'MAPA',
    'stdin': 'STDIN',
    'add': 'ADD',
    'from': 'FROM',
    'remove': 'REMOVE',
    'update': 'UPDATE',
    # Fin aporte
    # Inicio del aporte de Douglas Javier Sabando Macías
    'continue': 'CONTINUE',
    'else': 'ELSE',
    'break': 'BREAK',
    'class': 'CLASS',
    'final': 'FINAL',
    'for': 'FOR',
    'if': 'IF',
    'print': 'PRINT',
    'readLineSync': 'READLINESYNC',
    'export': 'EXPORT',
    'function': 'FUNCTION',
    'get': 'GET',
    # Fin aporte
}

tokens += list(reserved.values())


# Aporte P@B por Paul Bustos M.
# t_DIGIT = r'([0-9])'
t_NONDIGIT = r'([_A-Za-z])'
t_SEMICOLON = r';'
t_COLON = r':'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_DOT = r'\.'
t_GREATER_THAN = r'>'
t_EQUAL = r'='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_SLASH = r'/'
t_APOSTROPHE = r'\''
t_LPARENTHESE = r'\('
t_RPARENTHESE = r'\)'
t_BACKSLASH = r'\\'
# Fin P@B
# Inicio del aporte de Jorge Luis Valenzuela Bustos.
t_DOBLEIGUAL = r'\={2}'
t_MENOR = r'\<'
t_MENORIGUAL = r'\<\='
t_CADENA = r'"[a-zA-z0-9\s]+"'
t_RBRACKET = r'\]'
t_LBRACKET = r'\['
# Fin aporte

    # Aporte P@B por Paul Bustos M.
    # def t_PLUS_EQUAL(self, t):
    #     r'(var | dynamic | num | int | double)? ([_A-Za-z]([_A-Za-z]?[0-9]?)*) += +?\d+\; | -?\d+\.\d+'
    #     return t
    #
    # def t_MINUS_EQUAL(self, t):
    #     r'(var | dynamic | num | int | double)? ([_A-Za-z]([_A-Za-z]?[0-9]?)*) -= +?\d+\; | -?\d+\.\d+'
    #     return t

def t_FLOTANTE(t):
    r'(-?[1-9]\d*\.\d+)|0.0'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'(-?[1-9]\d*)|0'
    t.value = int(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_BRACES(t):
    r'([_A-Za-z]([_A-Za-z]?[0-9]?)*) \{ ([_A-Za-z]([_A-Za-z]?[0-9]?)*) \}'
    return t

# def t_DIAMOND_OPERATOR(self, t):
#     r'(List< ([A-Za-z]+)? > | Map< ([A-Za-z]+ , [_A-Za-z]+)? >) (\( ([_A-Za-z]+ (, [_A-Za-z]+)*)? \))?'
#     return t

def t_ID(t):
    r'[a-zA-Z_][A-Za-z0-9_]*'
    # Inicio del aporte de Jorge Luis Valenzuela Bustos.
    t.type = reserved.get(t.value, 'ID')
    # Fin aporte
    return t

# Fin P@B

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

def getTokens(lexer):

    while True:
    
        tok = lexer.token()
    
        if not tok:
            break
    
        print(tok)

'''
linea = " "
while linea != "":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
print("Ejecución terminada")
'''