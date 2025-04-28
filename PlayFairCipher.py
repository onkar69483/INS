def matrix(key):
    key=''.join(dict.fromkeys(key.upper().replace("J","I")))
    abc="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    full=''.join(dict.fromkeys(key+abc))
    return [list(full[i:i+5])for i in range(0,25,5)]
def pos(grid,ch):
    for i in range(5):
        for j in range(5):
            if grid[i][j]==ch:
                return i,j
    return None
def pairs(text):
    text=text.upper().replace("J","I").replace(" ","")
    res,i=[],0
    while(i<len(text)):
        a=text[i]
        b=text[i+1] if i+1<len(text) else 'X'
        if a==b:
            res.append((a,'X'))
            i=i+1
        else:
            res.append((a,b))
            i=i+2
    return res
def rule(a,b,g,s):
    r1,c1=pos(g,a)
    r2,c2=pos(g,b)
    if r1==r2: return g[r1][(c1 +s)%5]+g[r2][(c2+s)%5]
    if c1==c2: return g[(r1+s)%5][c1]+g[(r2+s)%5][c2]
    return g[r1][c2]+g[r2][c1]
def encrypt(text,key):
    g=matrix(key)
    return ''.join(rule(a,b,g,1) for a,b in pairs(text))
def decrypt(text,key):
    g=matrix(key)
    return ''.join(rule(a,b,g,-1) for a,b in pairs(text))
e = encrypt("HELLO", "MONARCHY")
d = decrypt(e, "MONARCHY")
print("Encrypted:", e)
print("Decrypted:", d.replace("X",""))