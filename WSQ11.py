def invert(inf):
 inf=str(inf)
 inf=inf[::-1]
 inf=int(inf)
 return(inf)


rangeofnumbers=[]
lychrel=[]

inf=int(input("Write the inferior number"))
sup=int(input("Write the superior number"))

for i in range(sup-inf+1):
 rangeofnumbers.append(inf)
 inf=inf+1

palindromes=0
nolychrel=0
candidates=0

for i in rangeofnumbers:
 inverted=invert(i)
 if i==inverted:
  palindromes=palindromes+1
 else:
  iteration1=inverted+i
  iteration2=invert(iteration1)
  for i1 in range(30):
   if iteration1==iteration2:
    nolychrel=nolychrel+1
    break
   else:
    iteration1=iteration1+iteration2
    iteration2=invert(iteration1)
    if (i1==29):
     candidates=candidates+1
     lychrel.append(i)

print("There are",palindromes,"palindromes")
print("There are",nolychrel,"thate are not lychrel")
print("There are",candidates," candidates for lychrel")

if candidates!=0:
 print("Los numeros lychrel son:", lychrel)
