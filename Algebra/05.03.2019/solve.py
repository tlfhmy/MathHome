DM = []
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            for l in range(0,3):
                DM.append((i,j,k,l))
#print(len(DM),DM)

Ans = []

#       i1^2  + i2*j1 = 1 (mod 3)
#       i1*j1 + j2*j1 = 0 (mod 3)
#       i1*i2 + i2*j2 = 0 (mod 3)
#       i2*j1 + j2^2  = 1 (mod 3)
#   There I use instead: i[0] ~ i1; i[1]~j1; i[2]~i2; i[3]~j2


for i in DM:
    if (i[0]**2 + i[2]*i[1]) % 3 == 1 and\
    (i[0]*i[1] + i[3]*i[1]) % 3 == 0 and\
    (i[0]*i[2] + i[2]*i[3]) % 3 == 0 and\
    (i[2]*i[1] + i[3]**2) % 3 == 1:
        Ans.append(i)

print(Ans)