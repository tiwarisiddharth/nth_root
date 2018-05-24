def nthRootMe(m,n):
    def pwr(p,q):
        r=1;
        for i in range(0,q):
            r*=p
        return r
    def repe(x):
        a=m/pwr(x,n-1)
        b=(a+(x*(n-1)))/n
        if (x==((x+b)/2)):
            print(x)
        else:
            repe((x+b)/2)
    repe(1)
#function called
#cube root of 999 is calculated here.
nthRootMe(999,3)
