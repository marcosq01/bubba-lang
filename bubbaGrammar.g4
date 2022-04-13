grammar bubbaGrammar;

//Parser rules
//////////////////////////////////7

program: PROG ID COLON paux paux2 paux3 main;
paux: classr paux | ;
paux2: varsr | ;
paux3: methods paux3 | ;

main: MAIN LPARENTHESIS RPARENTHESIS LBRACE body RBRACE;

whiler: WHILE LPARENTHESIS expression RPARENTHESIS LBRACE whileaux RBRACE;
whileaux: statement whileaux2;
whileaux2: whileaux | ;

forr: FOR foraux TO foraux foraux2 LBRACE foraux3 RBRACE;
foraux: V_INT | ID;
foraux2: STEP foraux | ;
foraux3: statement foraux4;
foraux4: foraux3 | ;

statement: assign | call | cond| forr| whiler| output| inputr;

lid: ID lidaux SEMICOLON;
lidaux: laux laux2;
laux: COMMA ID laux| ;
laux2: LBRACKET V_INT maux RBRACKET laux | ;
maux: COMMA V_INT | ;

cond: IF LPARENTHESIS expression RPARENTHESIS LBRACE condaux RBRACE condaux3;
condaux: statement condaux2;
condaux2: condaux| ;
condaux3: ELSE LBRACE condaux RBRACE;

assign: assignaux EQUAL expression;
assignaux : ID DOT ID | ID ;

factor: faux faux2;
faux: ADD | MINUS | ;
faux2: var_cte| call|LPARENTHESIS expression RPARENTHESIS| ID faux3;
faux3:LBRACKET expression faux4 RBRACKET | DOT ID| ;
faux4: COMMA expression | ;

term: factor termaux;
termaux: STAR term | SLASH term | ;

exp: term expaux;
expaux: ADD exp| MINUS exp| ;

aexp: exp aexpaux;
aexpaux:aexps exp | ;
aexps: GREATER | LESS | EQEQUAL| NOTEQUAL | GREATEREQ| LESSEQ;

bexp: aexp bexpaux;
bexpaux: AND bexp| ;

expression: bexp expressionaux;
expressionaux: OR expression| ;

func: FUNC type_simple ID LPARENTHESIS funcaux RPARENTHESIS LBRACE body RETURN expression SEMICOLON RBRACE;
funcaux: args | ;

classr:
    CLASS ID class_a LBRACKET varsr class_b RBRACKET SEMICOLON;

class_a:
    EXTENDS ID
    | ;

class_b:
    methods
    | ;

output:
    PRINT LPARENTHESIS expression output_a RPARENTHESIS SEMICOLON;

output_a:
    COMMA expression output_a
    | ;

inputr:
    INPUT LPARENTHESIS ID input_a RPARENTHESIS SEMICOLON;

input_a:
    COMMA ID input_a
    | ;

body:
    body_a statement body_b;

body_a:
    varsr
    | ;

body_b: 
    statement body_b
    | ;

varsr:
    VARS vars_a COLON lid vars_b;
vars_a:
    ID
    | type_simple;
vars_b:
    varsr
    | ;

args:
    type_simple COLON ID args_a;

args_a: 
    COMMA args
    | ;

type_simple:
    INT
    | FLOAT
    | STRING;

call:                                                                            
    ID call_a LPARENTHESIS call_b RPARENTHESIS;                               
                                                                                 
call_a:                                                                          
    DOT ID                                                                       
    | ;                                                                         
                                                                                 
call_b:                                                                          
    params                                                                       
    | ; 

params:
    expression params_a;

params_a:
    COMMA params
    | ;

var_cte:
    V_INT
    | V_FLOAT
    | V_STRING;

void:
    FUNC VOID ID LPARENTHESIS void_a RPARENTHESIS LBRACE body RBRACE;

void_a:
    args
    | ;

methods:
    void methods
    | func methods;
  


//Tokens
PROG: 'prog';
MAIN: 'main';
FLOAT: 'float';
INT: 'int';
STRING: 'string';
PRINT: 'print';
VARS: 'vars';
IF: 'if';
ELSE:'else';
DOT : '.';
COMMA: ',';
LPARENTHESIS:'(';
RPARENTHESIS:')';
LBRACE:'{';
RBRACE:'}';
LBRACKET:'[';
RBRACKET:']';
SEMICOLON:';';
ADD:'+';
MINUS:'-';
STAR:'*';
SLASH: '/';
GREATER:'>';
GREATEREQ:'>=';
LESS:'<';
LESSEQ:'<=';
EQUAL:'=';
COLON: ':';
QUOTE: '"';
AND:'&&';
OR: '||';
NOT:'!';
EQEQUAL: '=='; 
NOTEQUAL: '!=';
WHILE: 'while';
FOR: 'for';
STEP:'step';
RETURN: 'return';
CLASS: 'class';
EXTENDS : 'extends';
FUNC: 'func';
VOID:'void';
INPUT:'input';
TO:'to';

fragment DIGIT: [0-9];
fragment LETTER: [A-Za-z];

V_STRING: QUOTE [^QUOTE]*  QUOTE;
ID: (LETTER DIGIT*)+;
V_INT: DIGIT+;
V_FLOAT: DIGIT+ DOT DIGIT+;

WS: [ \t\r\n] + -> skip;

///


