%{
#include <stdio.h>
#include "y.tab.h"
%}

%%

[\t ]+ 

printf | 
scanf |
strlen |
strcpy |
free |
mallac |
realloc | 
memcpy |
memset |
fwrite |
fread |
getchar |
isgraph |
isspace |
tolower |
toupper |
isalpha |
isdigit |
islower |
isuppper {return fun; }

\n { return(0); }

%%
