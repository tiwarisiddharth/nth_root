def nthRootMe(m,n):
    
    #to calculate p**q
    def pwr(p,q):
        r=1;
        for i in range(0,q):
            r*=p
        return r
    #this repe function takes a guess and improves it and keeps improving it until the if condition is met.
    def repe(x):
        a=m/pwr(x,n-1)
        b=(a+(x*(n-1)))/n
        
        # this if specifies when the new guess generated will have no change then the that will be the answer.
        # to adjust precision
        # use this 'abs(((x+b)/2)-x) < p' as a condition inside if and replace 'p' with the amount of precision you need
        # smaller the value of 'p' larger the precision.
        
        if (x==((x+b)/2)):
            print(x)
        else:
            repe((x+b)/2)
    repe(1)
#function called
#cube root of 999 is calculated here.
nthRootMe(999,3)
