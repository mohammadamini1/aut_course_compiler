#!/usr/bin/python3

from ply import lex

class Lexer:
    reserved = {
        'program': 'PROGRAM',
        'var': 'VAR',
        'int': 'INTEGER',
        'real': 'REAL',
        'begin': 'BEGIN',
        'end': 'END',
        'if': 'IF',
        'then': 'THEN',
        'else': 'ELSE',
        'while': 'WHILE',
        'do': 'DO',
        'print': 'PRINT',
        'switch': 'SWITCH',
        'of': 'OF',
        'done': 'DONE',
        'default': 'DEFAULT',
        'mod': 'MOD',
        'and': 'AND',
        'or': 'OR',
        'not': 'NOT',
    }

    tokens = [
        'DOUBLEDOT',
        'SEMICOLON',
        'COMMA',
        'ASSIGN',
        'LCB',
        'RCB',
        'SUM',
        'SUB',
        'MUL',
        'DIV',
        'L',
        'E',
        'G',
        'NE',
        'LE',
        'GE',
        'INTEGER_CONSTANT',
        'REAL_CONSTANT',
        'IDENTIFIER',

        # '',

    ] + list(reserved.values())


    t_DOUBLEDOT = r'\:'
    t_SEMICOLON = r'\;'
    t_COMMA = r'\,'
    t_ASSIGN = r'\:\='
    t_LCB = r'\('
    t_RCB = r'\)'
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_L = r'\<'
    t_E = r'\='
    t_G = r'\>'
    t_NE = r'\<\>'
    t_LE = r'\<\='
    t_GE = r'\>\='
    def t_REAL_CONSTANT(self, t):
        r'[-]?(\d+\.\d+)'
        t.value = float(t.value)    
        return t
    def t_INTEGER_CONSTANT(self, t):
        r'[-]?(\d+)'
        t.value = int(t.value)    
        return t

    t_ignore  = '\n \t'
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        raise Exception('Error at', t.value[0], t.lineno, t.lexpos)


    def t_IDENTIFIER(self, t):
        r'[a-zA-Z][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'IDENTIFIER')
        return t


    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer


