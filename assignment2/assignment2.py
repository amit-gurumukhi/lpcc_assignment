#code for pass of macro processor (generate mnt and mdt)
mdtp =0
mntp =0
mnt ={}
mntl =[]
mdt ={}
file1 = open("input1.txt",'r')
file2 = open("mdt.txt",'a+')
file3 = open("mnt.txt",'a+')

file3.write("MACRO_NAME \t START END \n\n")

lines = file1.readlines()
for line in lines :
  x = line.split()
 
  if(len(x)>0):
  
   if(x[0]=='MACRO'):
     mntp= mntp+1
     mnt[x[1]] =[mdtp+1]
     mntl.append(x[1])
   elif (x[0]=='MEND'):
    mnt[mntl[mntp-1]].append(mdtp)
    file2.write("\n")
    file3.write(mntl[mntp-1]+"\t\t\t\t"+str(mnt[mntl[mntp-1]])+" \n")
   else :
     mdtp=mdtp+1
     for i in x:
       file2.write(i+" ")
     file2.write("\t\t"+str(mdtp)+" \n")

print(mnt)
print(mntl)
