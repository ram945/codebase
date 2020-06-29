import sys
sys.stdout=open('code1/output.txt','w')
sys.stdin=open('code1/input.txt','r')


tc=int(input())
for _ in range(tc):
    s,m=map(int,input().split())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    org_sum=0
    new_sum=0
    for j in range(s):
        org_sum=org_sum+(A[j]*B[j])
    new_sum=org_sum
    for j in range(s):
        curr_prod=A[j]*B[j]
        sel_prod=min((A[j]+2*m)*B[j],(A[j]-2*m)*B[j])
        temp_sum=org_sum-curr_prod+sel_prod
        if temp_sum<new_sum:
            new_sum=temp_sum
    print(new_sum)



     

