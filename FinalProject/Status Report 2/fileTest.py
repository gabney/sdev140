import os
c = os.getcwd()
print(c)
f = open(f"{c}/"+'testfile.txt','w') 
f.write("Hello World") 
f.close()