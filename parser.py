#!/usr/bin/python3

from ply import yacc
from lexer import Lexer

class Parser:
    tokens = Lexer().tokens

    def __init__(self):
        pass

    def p_program(self, p):
        'program : PROGRAM IDENTIFIER declarations compound_statement'
        print('program : PROGRAM IDENTIFIER declarations compound_statement')

    def p_declarations(self, p):
        '''
        declarations : VAR declaration_list
                        | empty
        '''
        print('declarations : VAR declaration_list | empty')

    def p_declaration_list(self, p):
        '''declaration_list : identifier_list DOUBLEDOT type
                            | declaration_list SEMICOLON identifier_list DOUBLEDOT type
        '''
        print('declaration_list : identifier_list DOUBLEDOT type | declaration_list SEMICOLON identifier_list DOUBLEDOT type')

    def p_identifier_list(self, p):
        '''identifier_list : IDENTIFIER
                            | identifier_list COMMA IDENTIFIER
        '''
        print('identifier_list : IDENTIFIER | identifier_list COMMA IDENTIFIER')

    def p_type(self, p):
        '''type : INTEGER
                    | REAL'''
        print('type : INTEGER | REAL')

    def p_compound_statement(self, p):
        'compound_statement : BEGIN statement_list END'
        print('compound_statement : BEGIN statement_list END')

    def p_statement_list(self, p):
        '''statement_list : statement
                            | statement_list SEMICOLON statement
        '''
        print('statement_list : statement | statement_list SEMICOLON statement')

    def p_statement(self, p):
        '''statement : IDENTIFIER ASSIGN exp
                        | IF exp THEN statement ELSE statement
                        | IF exp THEN statement
                        | WHILE exp DO statement
                        | compound_statement
                        | PRINT LCB exp RCB
                        | SWITCH exp OF cases default_case DONE
        '''
        print('statement : IDENTIFIER ASSIGN exp | IF exp THEN statement ELSE statement | IF exp THEN statement | WHILE exp DO statement | compound_statement | PRINT LCB exp RCB | SWITCH exp OF cases default_case DONE')

    def p_default_case(self, p):
        '''default_case : DEFAULT statement SEMICOLON
                        | empty
        '''
        print('default_case : DEFAULT statement SEMICOLON | empty')

    def p_cases(self, p):
        '''cases : constant_list DOUBLEDOT statement SEMICOLON cases
                        | empty
        '''
        print('cases : constant_list DOUBLEDOT statement SEMICOLON cases | empty')

    def p_constant_list(self, p):
        '''constant_list : constant
                        | constant_list COMMA constant
        '''
        print('constant_list : constant | constant_list COMMA constant')

    def p_constant(self, p):
        '''constant : REAL_CONSTANT
                        | INTEGER_CONSTANT
        '''
        print('constant : REAL_CONSTANT | INTEGER_CONSTANT')

    def p_exp(self, p):
        '''
        exp : INTEGER_CONSTANT
            | REAL_CONSTANT
            | IDENTIFIER
            | exp SUM exp 
            | exp SUB exp
            | exp MUL exp
            | exp DIV exp
            | SUB exp
            | exp MOD exp
            | exp L exp
            | exp E exp
            | exp G exp
            | exp NE exp
            | exp LE exp
            | exp GE exp
            | exp AND exp
            | exp OR exp
            | NOT exp
            | LCB exp RCB
        '''
        print('exp: ',p[1])

    def p_empty(self, p):
        'empty : '
        print('empty : ')


    precedence = (
        ('left', 'OR', 'AND'),
        ('left', 'NOT'),
        ('nonassoc', 'L', 'LE', 'E', 'NE', 'G', 'GE'),

        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV', 'MOD'),

        # ('left', 'ELSE'),
        # ('right', 'IF', 'ELSE'),

        ('left', 'LCB', 'RCB'),
        ('right', 'ASSIGN'),

    )





    def p_error(self, p):
        if p:
            print('Syntax error at token', p)
            # parser.errok()
        else:
            print('Syntax error at EOF')

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser


