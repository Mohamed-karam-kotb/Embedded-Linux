def count_four(li):
    element=4
    x=[i for i in li if i==element] 
    print("the element",element,"occurs",len(x),"times")
    
li_ex=[2,3,5,4,6,4,7,4]
count_four(li_ex)
