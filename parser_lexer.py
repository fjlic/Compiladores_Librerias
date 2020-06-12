# -*- encondig: utf-8 -*-

import ply.lex as lex
import argparse
import sys

columna = 0
# list of tokens
tokens = (

	# Reserverd words
	'KEY_ELSE',
	'KEY_IF',
	'INT',
	'FLOAT',
	'CHAR',
	'RETURN',
	'VOID',
	'MAIN',
	'KEY_WHILE',
	'KEY_FOR',
	
	# Symbols
	'PLUS',
	'MINUS',
	'TIMES',
	'DIVIDE',
	'MENOR_QUE',
	'MENOR_QUE_IGUAL',
	'MAYOR_QUE',
	'MAYOR_QUE_IGUAL',
	'IGUAL',
	'DIGUAL',
	'DISTINT',
	'PUNTOCOMA',
	'COMMA',
	'LPAREN',
	'RPAREN',
	'LBRACKET',
	'RBRACKET',
	'LBLOCK',
	'RBLOCK',

	# Others	
	'IDENTIFIER',
	'IDENTIFIER_1', 
	'NUMBER',

	#libs
	'LIB',
	'DEFINE',

	#Literarl
	'LITERAL',
	'LITERAL_2',

	#WhiteSpace
	'WHITESPACE',
	'WHITESPACE_T',
	'WHITESPACE_N',
	
)

# Regular expressions rules for a simple tokens
def t_PLUS(t):
	r'\+'
	global columna
	columna += 1
	return t

def t_MINUS(t):
	r'-'
	global columna
	columna += 1
	return t

def t_TIMES(t):
	r'\*'
	global columna
	columna += 1
	return t

def t_DIVIDE(t):
	r'/'
	global columna
	columna += 1
	return t

def t_IGUAL(t):
	r'='
	global columna
	columna += 1
	return t

def t_MENOR_QUE(t):
	r'<'
	global columna
	columna += 1
	return t

def t_MAYOR_QUE(t):
	r'>'
	global columna
	columna += 1
	return t

def t_PUNTOCOMA(t):
	r';'
	global columna
	columna += 1
	return t

def t_COMMA(t):
	r','
	global columna
	columna += 1
	return t

def t_LPAREN(t):
	r'\('
	global columna
	columna += 1
	return t

def t_RPAREN(t):
	r'\)'
	global columna
	columna += 1
	return t

def t_LBRACKET(t):
	r'\['
	global columna
	columna += 1
	return t

def t_RBRACKET(t):
	r'\]'
	global columna
	columna += 1
	return t

def t_LBLOCK(t):
	r'{'
	global columna
	columna += 1
	return t

def t_RBLOCK(t):
	r'}'
	global columna
	columna += 1
	return t

def t_LIB(t):
	r'\#include'
	global columna
	columna += 1
	return t

def t_DEFINE(t):
	r'\#define'
	global columna
	columna += 1
	return t

def t_VOID(t):
	r'void'
	global columna
	columna += 1
	return t

def t_MAIN(t):
	r'main'
	global columna
	columna += 1
	return t

def t_INT(t):
	r'int'
	global columna
	columna += 1
	return t
	
def t_FLOAT(t):
	r'float'
	global columna
	columna += 1
	return t
	
def t_CHAR(t):
	r'char'
	global columna
	columna += 1
	return t
	
def t_KEY_IF(t):
	r'if'
	global columna
	columna += 1
	return t
	
def t_KEY_ELSE(t):
	r'else'
	global columna
	columna += 1
	return t
	
def t_RETURN(t):
	r'return'
	global columna
	columna += 1
	return t
		
def t_KEY_WHILE(t):
	r'while'
	global columna
	columna += 1
	return t
	
def t_KEY_FOR(t):
	r'for'
	global columna
	columna += 1
	return t
		
def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	global columna
	columna += 1
	return t
	
def t_IDENTIFIER_1(t):
	r'\w+(\.\w)*'
	global columna
	columna += 1
	return t
	
def t_IDENTIFIER(t):
	r'\w+(_\d\w)*'
	global columna
	columna += 1
	return t
	
def t_LITERAL(t):
	r'\"(.)*?\"'
	t.lexer.lineno += t.value.count('\n')
	global columna
	columna += 1
	return t
	
def t_LITERAL_2(t):
	r'\'(.)*?\''
	t.lexer.lineno += t.value.count('\n')
	global columna
	columna += 1
	return t
	 
def t_MENOR_QUE_IGUAL(t):
	r'<='
	global columna
	columna += 1
	return t
	
def t_MAYOR_QUE_IGUAL(t):
	r'>='
	global columna
	columna += 1
	return t
	
def t_DIGUAL(t):
	r'=='
	global columna
	columna += 1
	return t
	
def t_DISTINT(t):
	r'!='
	global columna
	columna += 1
	return t
	
def t_WHITESPACE(t):
	r'\ '
#	t.lexer.lineno += len(t.value)
	global columna
	columna += 1
	return t
	
def t_WHITESPACE_N(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	global columna
	columna += 1
	return t
	
def t_WHITESPACE_T(t):
	r'\t+'
#	t.lexer.lineno += len(t.value)
	global columna
	columna += 1
	return t
	
#t_ignore = ' \t'

def t_comments(t):
	r'/\*(.|\n)*?\*/'
	t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
	r'//(.)*?\n'
	t.lexer.lineno += 1

def t_error(t):
	print "Lex UNKNOWN: " + str(t.value[0])
	t.lexer.skip(1)

def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		#print(tok)
		if 	tok.value=="\n":
			string=str("\\n")
		else:
			string=str(tok.value)
		print "Lex (" + str(tok.type) + ", " + str(string) + "," + str(tok.lineno) + "," + str(columna) +"," + str(tok.lexpos) + ")"
		

lexer = lex.lex()

# Test 
if __name__ == '__main__':
	#parser = argparse.ArgumentParser(description='%(prog)s is an array the arguments')
	#parser.add_argument('files', option_strings=[], nargs='*', help='Test Help')
	#args = parser.parse_args()
	#    if len(args.files) > 0: 
	#	    for arg in args.files:
	#		    fil = open(arg, 'r')
	#		    data = fil.read()
	#		    print "Nombre del Archivo: " + arg + "\n"
	#		    print data
	#		    lexer.input(data)
	#		    test(data, lexer)
    #
	#    else:
	#	    print " Necesito el nombre el programa en lenguaje C para analizarlo \n Gracias ...."

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'Matriz_File.c'
    
	print "Nombre del Archivo: " + fin + "\n"
	print "Contenido del archivo: "
	f = open(fin, 'r')
	lineas = f.readlines()
	print lineas
	for linea in lineas:
		print linea
		lexer.input(linea)
		test(linea, lexer)
		columna=0
		print "---------------------------------------------------------------------------------"
	
	#print data
	#lexer.input(data)
	#test(data, lexer)
	#parser.parse(data, tracking=True)
    # Build lexer and try on
	#lexer.input(data)
	#test(data, lexer)