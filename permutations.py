


def permute(A,l, list_of_all_perms):
    r=len(A)
    if l==r-1:
      list_of_all_perms.append(A.copy())
      
    for i in range(l,r): # SET EACH ELEMENT TO BE AT FIRST POSITION IN THIS LEVEL 
      A[l],A[i]=A[i],A[l]
      permute(A,l+1,list_of_all_perms)
      A[l],A[i]=A[i],A[l]

def permuteUnique(A,l, list_of_all_perms):
    r=len(A)
    if l==r-1:
      list_of_all_perms.append(A.copy())
    duplicate_check=set()
    for i in range(l,r): # SET EACH ELEMENT TO BE AT FIRST POSITION IN THIS LEVEL 
      if A[i] not in duplicate_check:
        print(l)
        duplicate_check.add(A[i])          
        A[l],A[i]=A[i],A[l]
        permuteUnique(A,l+1,list_of_all_perms)
        A[l],A[i]=A[i],A[l]

def permuteShort(A,l,r_limit, list_of_all_perms):
    if l==r_limit:
      list_of_all_perms.append(A[:r_limit].copy())
    for i in range(l,len(A)): # SET EACH ELEMENT TO BE AT FIRST POSITION IN THIS LEVEL 
      A[l],A[i]=A[i],A[l]
      permuteShort(A,l+1,r_limit,list_of_all_perms)
      A[l],A[i]=A[i],A[l]

A=[4,4,4,4]
A=[1,2,3,4]
all_perms=[]

permuteShort(A,0,3,all_perms)
# permuteUnique(A,0,all_perms)
print(all_perms)