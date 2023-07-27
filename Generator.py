quadruples = []

def backpatch(l: list, i: int):
    for line_number in l:
        quadruples[line_number - 1] = ("goto", i)


def nextinstr():
    return len(quadruples) + 1


def p_marker(t):
    'marker : '
    t[0] = nextinstr()

class E:
    def __init__(self, t, f):
        self.truelist = t
        self.falselist = f


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


    def p_exp_const_int(self, p):
        '''
        exp : INTEGER_CONSTANT
        '''
        p[0] = p[1]


    def p_exp_const_real(self, p):
        '''
        exp : REAL_CONSTANT
        '''
        p[0] = p[1]

    def p_exp_identifier(self, p):
        '''
        exp : IDENTIFIER
        '''
        p[0] = p[1]

    def p_exp_sum(self, p):
        '''
        exp : exp exp SUM exp
        '''
        p[0] = E([],[])
        # p[0].addr = global_temp.newTemp()
        quadruples.append((p[0].addr + '=' + str(p[1].addr) + '+' + str(p[3].addr),))

    def p_exp_sub(self, p):
        '''
        exp : exp exp SUB exp
        '''
        p[0] = E([], [])
        # p[0].addr = global_temp.newTemp()
        quadruples.append((p[0].addr + '=' + str(p[1].addr) + '-' + str(p[3].addr),))

    def p_exp_mul(self, p):
        '''
        exp : exp exp MUL exp
        '''
        p[0] = E([], [])
        # p[0].addr = global_temp.newTemp()
        quadruples.append((p[0].addr + '=' + str(p[1].addr) + '*' + str(p[3].addr),))

    def p_exp_div(self, p):
        '''
        exp : exp exp DIV exp
        '''
        p[0] = E([], [])
        # p[0].addr = global_temp.newTemp()
        quadruples.append((p[0].addr + '=' + str(p[1].addr) + '/' + str(p[3].addr),))

    def p_exp_unot(self, p):
        '''
        exp : SUB exp %prec UNOT
        '''
        p[0] = E(p[2].falselist, p[2].truelist)


    def p_exp_mod(self, p):
        '''
        exp : exp MOD exp
        '''


    def p_exp_less_than(self, p):
        '''
        exp : exp L exp
        '''


    def p_exp_equal(self, p):
        '''
        exp : exp E exp
        '''

    def p_exp_grater_than(self, p):
        '''
        exp : exp G exp
        '''


    def p_exp_not_equal(self, p):
        '''
        exp : exp NE exp
        '''

    def p_exp_less_equal(self, p):
        '''
        exp : exp LE exp
        '''

    def p_exp_greater_equal(self, p):
        '''
        exp : exp GE exp
        '''

    def p_exp_and(self, p):
        '''
        exp : exp AND marker exp
        '''
        backpatch(p[1].truelist, p[3])
        truelist = p[4].truelist
        falselist = p[4].falselist + p[1].falselist
        p[0] = E(truelist, falselist)

    def p_exp_or(self, p):
        '''
        exp : exp OR marker exp
        '''
        backpatch(p[1].falselist, p[3])
        truelist = p[1].truelist + p[4].truelist
        falselist = p[4].falselist
        p[0] = E(truelist, falselist)

    def p_exp_not(self, p):
        '''
        exp : NOT exp
        '''
        p[0] = E(p[2].falselist, p[2].truelist)

    def p_exp_group(self, p):
        'exp : LCB exp RCB'
        p[0] = p[2]


    def p_empty(self, p):
        'empty : '
        print('empty : ')



    # while True:
    #     try:
    #         s = input('calc > ')  # Use raw_input on Python 2
    #     except EOFError:
    #         break
    #     r = parser.parse(s)
    #     print(quadruples)
    #     print(r.truelist, r.falselist)
    #     quadruples.clear()

    