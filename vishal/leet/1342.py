#Run in terminal: python "vishal/leet/1342.py"
def numberOfSteps(num):
        step=0
        while(num!=0):
            if(num&1==0):
                num=num//2
                step+=1
            else:
                num-=1
                step+=1
        return step
num=int(input("Enter a number: "))
print(numberOfSteps(num))