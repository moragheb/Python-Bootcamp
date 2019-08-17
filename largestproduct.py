def max13product(num):
    import numpy 
    prod=1
    max=0
    res = list(map(int, num)) 
    for index in enumerate(res) :
        #nums=list(res[index:index+13])
        for j in range(index,index+13):
            prod+=res[j]
        #prod=numpy.product(nums)
        if prod>max:
                max=prod
    return prod 
          
    
        
    return max
with open("bigassnum.txt","r+") as newf:
    lines= newf.readlines()
    linesprd=[]
    number=""
    for line in lines:
        number+=(line.replace("\n",""))

        

    print(max13product(number))