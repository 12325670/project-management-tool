x = int(input("x: "))
y = int(input("y: "))
if(y<=20):
  for i in range(1,y+1):
    print(x,"*",i,"=",x*1)

else:
    for i in range (1,21):
        print(x,"*",i,"=",x*1)
    print("row is limited to 20") 
    
