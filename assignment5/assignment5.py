#Ambarish Kshirsagar C_26

#precedence list
precedence = [['/','1'],['*','1'],['+','2'],['-','2']]

def precedenceof(s):
    for x in precedence:
        if x[0]==s:
            return x[1]

#Main program 
opc = 0;

str = input("Please enter a simple expression")
l = len(str)
processed = [False]*l
operator = []

#creating a list with location of operators
for i in range(0,l):
    x = str[i]
    for j in range(0,4):
        if x==precedence[j][0]:
            temp =[]
            temp.append(precedence[j][1])
            temp.append(x)
            temp.append(i)
            operator.append(temp)
            break
        
#sorting the list of operators according to precedence
operator.sort()

for i in range(0,len(operator)):
    opt1=""
    opt2=""
    j = operator[i][2] # location
    if processed[j-1]==True:
        if operator[i-1][0]==operator[i][0]:
            opt1+= "t"
            opt1+=f"{i}"
        else:
            for x in range(0,len(operator)):
                if j-2 == operator[x][2]:
                    opt1+= "t"
                    z = x+1
                    opt1+=f"{z}"
    else:
        opt1 += str[j-1]
    
    if processed[j+1]==True:
        for x in range(0,len(operator)):
            if j+2 == operator[x][2]:
                opt2+= "t"
                z = x+1
                opt2+=f"{z}"
                
    else:
        opt2 += str[j+1]
    
    processed[j+1] = True
    processed[j-1] = True
    processed[j]   = True
    
    print(f"t{i+1} = {opt1} {operator[i][1]} {opt2}")
        
                
