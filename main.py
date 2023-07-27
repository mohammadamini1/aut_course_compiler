#!/usr/bin/python3



text_input = '''
program test
var x, y, z : int;
a, b : real

begin
x := 1 + 2;
y := x * 3;
z := y / 2;
a := 1.5 + 2.5;
b := a * 3.5;
print(x);
print(y);
print(z);
print(a);
print(b);

if x < y then
    if z >= y then
        print(a)
else
    print(b)




;

while x < 10 do
    x := x + 1;
    print(x);

switch x of
    1, 5 : print(x);
    6, 10 : print(y);
    default print(z);
done


end

'''


from lexer import Lexer
from parser import Parser

lexer = Lexer().build()
# file = open("test.txt")
# text_input = file.read()
# file.close()
lexer.input(text_input)

# output_file = open('output.txt', 'w')
# while True:
#     tok = lexer.token()
#     if not tok: break
#     print(tok)
#     output_file.write(str(tok) + '\n')
# output_file.close()
# print('\noutput saved in output.txt')

parser = Parser()
parser.build().parse(text_input, lexer, False)



