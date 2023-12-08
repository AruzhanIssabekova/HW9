import re

# 2

# N=list(map(int,input().split()))
# sch=0
# snch=0
# for i in range (len(N)):
#     if N[i]>=0:
#         sch=sch+N[i]
#     else:
#         snch=snch+N[i]
# if abs(snch)>abs(sch):
#     print(abs(snch)-abs(sch))
# elif abs(snch)<abs(sch):
#     print(-((abs(sch)-abs(snch))))
# else:
#     print(0)

# 1.1

# def ma(m):
#     s=[]
#     for i in range(m):
#         f=input()
#         s.append(f)
#         c=max(s,key=len)
#         d=len(c)
#         e=[]
#         for j in range(m):
#             k=len(s[j])
#             g=d-k
#             l=g*'*'+s[j]
#             print(l)
# m=int(input())
# h=ma(m)
# print(h)

# 1.2

# def ma(s):
#     c=max(s,key=len)
#     n=len(s)
#     d=len(c)
#     e=[]
#     for i in range (n):
#         k=len(s[i])
#         g=d-k
#         l=g*'*'+d[i]
#         e.append(l)
#     for q in e:
#         print(q)
# s=list(map(int,input().split()))
# h=ma(s)
# print(h)

# 3

# string=input()
# pattern = r'[\w0-9]+\.'
# r=re.findall(pattern, string)
# print(r)

# 4

# string=input()
# r = re.findall(r'[aeiouyAEIOUY]\w+', string)
# print(r)

# 5

string=input()
pattern = r'[fol]+'
r=re.split(pattern, string)
print(r)
