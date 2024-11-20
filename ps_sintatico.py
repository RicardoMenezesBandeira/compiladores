import ps_lex as lex
import ps_read as read
from ply import yacc

# Definir tokens (os tokens devem estar definidos previamente)
tokens = [
    'ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
    'AND', 'OR', 'NOT', 'EQ', 'NEQ', 'LT', 'GT', 'LTE', 'GTE','comma','semiCollum',
]

# Funções de produção para a gramática
def p_exp(p):
    '''EXP : PARAMETRO EXP_L1
           | LPAREN PARAMETRO EXP_L2 RPAREN '''
    print(f"Expressão: {p[1]}")
def p_parametro(p):
    '''PARAMETRO : ID'''
    
def p_empty(p):
    '''empty : semiCollum 
             | RPAREN '''
def p_exp_l1(p):
    '''EXP_L1 : EXP OP_LOGICO EXP
              | empty'''
    if len(p) > 2:
        print(f"Operação lógica: {p[1]} {p[2]} {p[3]}")

def p_exp_l2(p):
    '''EXP_L2 : EXP OP_MAT EXP
              | empty'''
    if len(p) > 2:
        print(f"Operação matemática: {p[1]} {p[2]} {p[3]}")

def p_param_logico(p):
    '''PARAM_LOGICO : EXP_LOGICO
                    | OP_LOGICO EXP
                    | PARAM_LOGICO comma EXP_LOGICO'''
    print(f"Parâmetro lógico: {p[1]}")

def p_exp_logico(p):
    '''EXP_LOGICO : OP_LOGICO EXP
                  | empty'''
    if len(p) > 1:
        print(f"Operação lógica: {p[1]} {p[2]}")

def p_op_mat(p):
    '''OP_MAT : PLUS
              | MINUS
              | TIMES
              | DIVIDE'''
    p[0] = p[1]

def p_op_logico(p):
    '''OP_LOGICO : AND
                 | OR
                 | NOT'''
    p[0] = p[1]

def p_op_comp(p):
    '''OP_COMP : EQ
               | NEQ
               | LT
               | GT
               | LTE
               | GTE'''
    p[0] = p[1]

# Erro de sintaxe
def p_error(p):
    print(f"Erro de sintaxe: {p}")

# Construir o parser
parser = yacc.yacc()

if __name__=='__main__':
    script = read.abre('./exemplo1.sp')
    L_tolken = lex.tolkenizando(script)
    if not lex.lexical_errors:
        result = parser.parse(script)
    
