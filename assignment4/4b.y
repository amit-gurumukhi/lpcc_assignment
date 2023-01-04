%{
#include <stdio.h>
#include <ctype.h>
#define YYSTYLE char*
int count = 0;
int yylex();
int yylex(void);
extern YYSTYLE yytext;
%}

%token fun

%%

S: fun { printf("Built-in function found - %s",yytext); count++;} |
;

%%

int main(){
	printf("\nEnter the string containing built-in function:\n\n");
	yyparse();
	printf("\n");
	if(count==0){
		printf("No function found\n");
	}
	return 0;
}

int yywrap(){
	return 1;
}

int yyerror(char *msg){
	fprintf(stderr,"%s\n",msg);
	return 0;
}



