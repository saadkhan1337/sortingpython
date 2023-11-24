##a=input("enter your list:")
##a=[67,2,34,5,76,86,-1,24,67,85]
##print("orginal sort:",a)
##a.sort()
##print("Asscending sort:",a)
##a.sort(reverse=True)
##print("Decending sort:",a)
##i=i+1
a=[0,45,25,60,90,-1,31,27,9,2,85,110]
n=len(a)
i=0
j=0
while(j<n):
        s=a[j]
        p= j
        i= j+1 
        while(i<n):
             if(a[i]>s):
                   s=a[i]
                   p=i
             i=i+1
        t=a[j]
        a[j]=a[p]
        a[p]=t
        j=j+1

print(a)
##
##    
