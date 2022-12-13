
%%
[\t ]+ /* ignore whitespace */ ; 
is?|am|are|were|was|be|being|been|do|does|did|will|would|should|can|could|has|have|had|go {printf("%s: is a verb\n",yytext);}

very|simply|gently|quietly|calmly|angrily { printf("%s: is an adverb\n", yytext);}
 
to|from|behind|above|below|between {printf("%s: is a preposition\n", yytext); } 

if|then|and|but|or { printf("%s: is aconjunction\n", yytext); }

their|my|your|his|her|its { printf("%s:is a adjective\n", yytext); }

(I|i)|(Y|y)ou|(H|h)e|(S|s)he|(W|w)e|(T|t)hey { printf("%s: is a pronoun\n",yytext); }

[a-zA-Z]+ { printf("%s: don't recognize, might be a noun\n", yytext);}
.|\n ECHO;/* normal default anyway */
%%
int yywrap(){return 1;}
int main() {
 yylex();
} 