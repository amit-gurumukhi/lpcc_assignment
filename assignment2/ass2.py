code = open("input.txt","r")
mnt = open("mnt.txt","a+")
mdt = open("mdt.txt","a+")
fpvpp = open("fpvpp","a+")
mnt.write("Macro_Name \t Start-End \n")

mntable = []
mdtable = []

mntp = 0
mdtp = 0
flag = False

lines  = code.readlines()

for l in lines:
    x = l.split();
    
    if(len(x)>0):
        
        if x[0]=="MACRO" :
            flag = True;
            mntp = mntp +1
            mntable.append(x[1])
            mntable.append(mdtp)
            
            if len(x) > 2:
                # parameters exist
                l = mntp*3
                fpvpp.write(mntable[l-3]+"\n")
                for i in range(2,len(x)):
                    fpvpp.write(x[i] + " " + str(i-1)+ "\n")
                fpvpp.write("\n")
                    
        elif x[0]=="MEND":
            flag =  False
            mntable.append(mdtp-1)
            l = mntp*3
            mnt.write(mntable[l-3]+ " " + str(mntable[l-2])+ " " + str(mntable[l-1]) + "\n")
        
        elif flag == True:
            for i in x:
                mdt.write(str(i) +" ")
            mdt.write(" "+ str(mdtp) + "\n")
            mdtp = mdtp +1
                    
                
            
