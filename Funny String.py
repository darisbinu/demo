q = int(input().strip())
for testcase in range(q):
    s = list(input())
    r = list(reversed(s))
    f=0
    for i in range (0,len(s)-1):
        if(abs(ord(s[i])-ord(s[i+1])) == abs(ord(r[i])-ord(r[i+1]))):
            f=f+1
    if(f==(len(s)-1)):
        print("Funny")
    else:
        print("Not Funny")
        
