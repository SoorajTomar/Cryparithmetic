import itertools
def solve(a,b,c):
    letters=[]
    for i in a+b+c:
        if i not in letters:
            letters.append(i)
    letters = tuple(letters)
    print(letters)
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        x=0 
        y=0 
        z=0
        sol = dict(zip(letters, perm))
        if sol[a[0]] == 0 or sol[c[0]] == 0 or sol[b[0]]==0:
            continue
        for i in range(len(a)):
            x+=pow(10,len(a)-i-1)*sol[a[i]]
        for i in range(len(b)):
            y+=pow(10,len(b)-i-1)*sol[b[i]]
        for i in range(len(c)):
            z+=pow(10,len(c)-i-1)*sol[c[i]]
        if x+y==z:
          print(a,b,c)
          return x,y,z
print(solve(input(),input(),input()))
