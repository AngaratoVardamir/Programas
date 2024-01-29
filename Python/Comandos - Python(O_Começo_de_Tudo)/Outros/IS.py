Coisa = str(input('Escreva uma Coisa: '))
print(Coisa.isalnum())#True:a,A,1  False:SPACE,#  
print(Coisa.isalpha())#True:a,A  False:1,SPACE,#  
print(Coisa.isascii())#True:a,A,1,SPACE,#  False:  
print(Coisa.isdecimal())#True:1  False:a,A,SPACE,#  
print(Coisa.isdigit())#True:1  False:a,A,SPACE,# 
print(Coisa.isidentifier())#True:a,A  False:1,SPACE,#  
print(Coisa.islower())#True:a,  False:A,1,SPACE,#  
print(Coisa.isnumeric())#True:1  False:a,A,SPACE,#  
print(Coisa.isprintable())#True:a,A,1,SPACE,#  False:  
print(Coisa.isspace())#True:  False:a,A,1,SPACE,#  
print(Coisa.istitle())#True:A  False:a,1,SPACE,# 
print(Coisa.isupper())#True:A  False:a,1,SPACE,#