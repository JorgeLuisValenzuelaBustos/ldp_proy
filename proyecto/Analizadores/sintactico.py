import ply.yacc as yacc
from Analizadores.lexico import tokens


# Aporte de Douglas Sabando Macías (1/2)
def p_dart(p):
    '''dart : sentencias
	'''


# | metodofunction
# Fin del aporte (1/2)


# Inicio del aporte de Jorge Luis Valenzuela Bustos

def p_sentencias(p):
    '''sentencias : imprimir
                    | expresion
					| obtenerEntrada
                    | estructurasControl
					| declaracion
					| metodosEstructuras
					| assign_operator_equal
    '''
    p[0] = p[1]


def p_expresion(p):
    '''expresion : comparacion
					| LPARENTHESE expresion RPARENTHESE
                    | booleano
                    | ID
	'''


def p_comparacion(p):
    '''comparacion : comparacionIgualdad
                    | comparacionMenorque
                    | comparacionMenorIgualque
    '''


def p_comparacionIgualdad(p):
    '''comparacionIgualdad : numeroOrId DOBLEIGUAL numeroOrId
							| ID DOBLEIGUAL numeroOrId
							| flotanteOrId DOBLEIGUAL flotanteOrId
							| ID DOBLEIGUAL flotanteOrId
							| booleanoOrId DOBLEIGUAL booleanoOrId
							| ID DOBLEIGUAL booleanoOrId
							| expresion DOBLEIGUAL expresion
                            | CADENA DOBLEIGUAL cadenaOrId
                            | cadenaOrId DOBLEIGUAL CADENA
	'''


def p_comparacionMenorque(p):
    '''comparacionMenorque : numeroOrId MENOR numeroOrId
							| ID MENOR numeroOrId
							| flotanteOrId MENOR flotanteOrId
							| ID MENOR flotanteOrId
							| expresion MENOR expresion
	'''


def p_comparacionMenorIgualque(p):
    '''comparacionMenorIgualque : numeroOrId MENORIGUAL numeroOrId
							| ID MENORIGUAL numeroOrId
							| flotanteOrId MENORIGUAL flotanteOrId
							| ID MENORIGUAL flotanteOrId
							| expresion MENORIGUAL expresion
	'''


def p_obtenerEntrada(p):
    '''obtenerEntrada : STDIN DOT READLINESYNC LPARENTHESE RPARENTHESE'''


def p_imprimir(p):
    '''imprimir : PRINT LPARENTHESE valor RPARENTHESE
				| PRINT LPARENTHESE obtenerElementoLista RPARENTHESE
	'''
    p[0] = p[3]


def p_obtenerElementoLista(p):
    'obtenerElementoLista : ID DOT GET LPARENTHESE numeroOrId RPARENTHESE'


def p_valor(p):
    '''valor :  ENTERO
    			| FLOTANTE
				| CADENA
                | ID
                | booleano
    '''

    p[0] = p[1]


def p_identificador(p):
    '''identificador : INT
					 | DOUBLE
					 | STRING
					 | BOOL
					 | DYNAMIC
	'''


def p_booleano(p):
    '''booleano :  TRUE
                | FALSE
           '''


def p_estructurasControl(p):
    '''estructurasControl : ifSimple
						  | ifElse
						  | while
	'''


def p_ifSimple(p):
    'ifSimple : IF LPARENTHESE expresion RPARENTHESE LBRACE sentenciasAnidadas RBRACE'


def p_ifElse(p):
    '''ifElse : ifSimple ELSE LBRACE sentenciasAnidadas RBRACE
				| ifSimple ELSE ifElse'''


def p_while(p):
    'while : WHILE LPARENTHESE expresion RPARENTHESE LBRACE sentenciasAnidadas RBRACE'


def p_sentenciasAnidadas(p):
    '''sentenciasAnidadas : sentencias
						| sentencias sentenciasAnidadas
	'''


def p_declaracion(p):
    '''declaracion : crearLista
				   | crearConjunto
				   | crearMapa
    '''


def p_crearLista(p):
    '''crearLista : LISTA ID EQUAL LBRACKET RBRACKET
				  |	LISTA ID EQUAL LBRACKET valLista RBRACKET
				  |	LISTA MENOR	identificador GREATER_THAN	ID EQUAL LBRACKET RBRACKET
				  |	LISTA MENOR	identificador GREATER_THAN	ID EQUAL LBRACKET valLista RBRACKET
	'''


def p_metodosEstructuras(p):
    '''metodosEstructuras : metodosLista
						  | metodosConjunto
						  | metodosMapa
	'''


def p_metodosLista(p):
    '''metodosLista : agregarElementoLista
					| removerElementoLista
	'''


def p_agregarElementoLista(p):
    'agregarElementoLista : ID DOT ADD LPARENTHESE valor RPARENTHESE'


def p_removerElementoLista(p):
    'removerElementoLista : ID DOT REMOVE LPARENTHESE valor RPARENTHESE'


def p_valLista(p):
    '''valLista : valor
				| valLista COMMA valor
	'''


def p_crearConjunto(p):
    '''crearConjunto : CONJUNTO ID
					  | CONJUNTO ID EQUAL CONJUNTO DOT FROM LPARENTHESE LBRACE valLista RBRACE RPARENTHESE
	'''


def p_metodosConjunto(p):
    '''metodosConjunto : asignacionConjunto
						| agregarElementoConjunto
						| removerElementoConjunto
	'''


def p_asignacionConjunto(p):
    '''asignacionConjunto : ID EQUAL CONJUNTO DOT FROM LPARENTHESE LBRACE valLista RBRACE RPARENTHESE'''


def p_agregarElementoConjunto(p):
    '''agregarElementoConjunto : ID DOT ADD LPARENTHESE valor RPARENTHESE'''


def p_removerElementoConjunto(p):
    'removerElementoConjunto : ID DOT REMOVE LPARENTHESE valor RPARENTHESE'


def p_crearMapa(p):
    '''crearMapa : MAPA MENOR identificador COMMA identificador GREATER_THAN ID EQUAL LBRACKET RBRACKET
				 | MAPA MENOR identificador COMMA identificador GREATER_THAN ID EQUAL LBRACKET valorMapa RBRACKET
	'''


def p_valorMapa(p):
    '''valorMapa : valor COLON valor
				 | valorMapa COMMA valor COLON valor
	'''


def p_metodosMapa(p):
    '''metodosMapa : removerElementoMapa
				   | actualizarElementoMapa
	'''


def p_removerElementoMapa(p):
    '''removerElementoMapa : ID DOT REMOVE LPARENTHESE valor RPARENTHESE'''


def p_actualizarElementoMapa(p):
    '''actualizarElementoMapa : ID DOT UPDATE LPARENTHESE valor COMMA valor RPARENTHESE'''


def p_numeroOrId(p):
    '''numeroOrId : ENTERO
					| ID
	'''


def p_flotanteOrId(p):
    '''flotanteOrId : FLOTANTE
						| ID
	'''


def p_booleanoOrId(p):
    '''booleanoOrId : booleano
					| ID
	'''


def p_cadenaOrId(p):
    '''cadenaOrId : CADENA
                  | ID
    '''


# Fin del aporte
# Inicio del aporte P@B de Paul Bustos M.

def p_assign_operator_equal(p):
    '''assign_operator_equal : numdt ID PLUS EQUAL ID SEMICOLON
    						 | numdt ID MINUS EQUAL ID SEMICOLON
    '''


# def p_id_operator_equal(p):
#     'id_operator_equal : ID operator_equal ID SEMICOLON'
#
# def p_operator_equal(p):
#     '''operator : PLUS EQUAL
#                 | MINUS EQUAL
#     '''

# def p_num(p):
#     'num : numdt ID EQUAL number SEMICOLON'
#
# def p_number(p):
#     '''number : NUMBER
#              |  NUMBER DOT NUMBER '''
#
# def p_datatype(p):
#     '''datatype : numdt
#                 | STRING
#                 | BOOL
#                 | DYNAMIC
#                 | CONST
#                 | LISTA
#                 | CONJUNTO
#                 | MAPA
#                 | FINAL
#                 | VAR
#     '''

def p_numdt(p):
    '''numdt : INT
             | DOUBLE
             | NUM
    '''


# Fin aporte P@B

# Aporte de Douglas Sabando Macías (2/2)
def p_metodoFunction(p):
    '''metodoFunction : identificador ID LPARENTHESE parametros RPARENTHESE LBRACE sentenciasAnidadas RBRACE
	'''


def p_parametros(p):
    '''parametros : identificador ID
			| parametros COMMA identificador ID
	'''


def p_import(p):
    '''import : IMPORT ID
			| IMPORT ID DOT ID
	'''


def p_valFunction(p):
    '''valFunction : ID
			| valor
			| valFunction COMMA ID
			| valFunction COMMA valor
	'''


def p_llamarFunction(p):
    '''llamarFunction : ID LPARENTHESE valFunction RPARENTHESE
	'''


# Fin del aporte (2/2)


# Samples

# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     p[0] = p[1] + p[3]
#
#
# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]
#
#
# def p_expression_term(p):
#     'expression : term'
#     p[0] = p[1]
#
#
# def p_term_times(p):
#     'term : term TIMES factor'
#     p[0] = p[1] * p[3]
#
#
# def p_term_div(p):
#     'term : term SLASH factor'
#     p[0] = p[1] / p[3]
#
#
# def p_term_factor(p):
#     'term : factor'
#     p[0] = p[1]
#
#
# def p_factor_num(p):
#     'factor : NUMBER'
#     p[0] = p[1]
#
#
# def p_factor_expr(p):
#     'factor : LPARENTHESE expression RPARENTHESE'
#     p[0] = p[2]

# ***

# Error rule for syntax errors
def p_error(p):
    errorFormat = ("Error sintáctico sentencia errónea Linea: {0}, columna: {1}"
                   .format(p.lineno, p.lexpos))

    print(errorFormat)


algoritmo = '''
while("test" == test){
    print(9)
};
if("test" == test){
    print(9)
};
if("test" == test){
    print(9)
} else if("test" == test){
    print(9)
} else{
	print(9)
};
print(9);
List<String> test = [];
Set hola = Set.from({"hola"});
Set hola;
hola = Set.from({"hola"});
hola.remove(9);
Map<String,String> test = [];
test.update("hola", "hola");
stdin.readLineSync()
'''.split(";")

parser = yacc.yacc()

for x in range(len(algoritmo)):
    result = parser.parse(algoritmo[x])
    print(result)
