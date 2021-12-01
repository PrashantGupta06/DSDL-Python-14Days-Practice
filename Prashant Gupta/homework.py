list = [18,20,8,16,4,10,12,3]
list.sort()
num = list[4]
count = 0

while num!=0:
    if num%2==0:
        num/=2
        count+=1
    elif num%2!=0:
        num-=1    
        count+=1
print(count)