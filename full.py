# caesar
def encrypt(key):
    plaintext = input("\nEnter plain text: ").lower()
    cipher = ""
    for char in plaintext:
        if char.isalpha():
            cipher += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            cipher += char
    print("\nEncrypted cipher text is:", cipher)
def decrypt(key):
    cipher = input("\nEnter cipher text: ").lower()
    plaintext = ""
    for char in cipher:
        if char.isalpha():
            plaintext += chr((ord(char) - ord('a') - key + 26) % 26 + ord('a'))
        else:
            plaintext += char
    print("\nDecrypted plain text is:", plaintext)
key = int(input("Enter key: "))
encrypt(key)
decrypt(key)


#playfair
key = input("Enter Key: ")
key = key.lower()
key_mat = [[], [], [], [], []]
present = []

row=0
col=0
for i in range (len(key)):
  ch = key[i]
  if ch == 'j':
    ch = 'i'
  if ch not in present:
    present.append(ch)
    key_mat[row].append(ch)
    col = col + 1
    if col == 5:
      col = 0
      row = row + 1

for i in range(ord('a'), ord('z')+1):
  ch = chr(i)
  if ch == 'j':
    continue
  if ch not in present:
    present.append(ch)
    key_mat[row].append(ch)
    col = col + 1
    if col == 5:
      col = 0
      row = row + 1
print(key_mat)
pt = input("Enter Plain Text: ")
pt = pt.lower()
helper = []
i=0
while i < len(pt):
  if pt[i] != pt[i+1]:
    helper.append([pt[i], pt[i+1]])
    i = i+2
  else:
    helper.append([pt[i], 'x'])
    i = i+1
  if i == len(pt)-1:
    helper.append([pt[i], 'x'])
    break
print(helper)
i=0
while i < len(helper):
  row1 = -1
  col1 = -1
  row2 = -1
  col2 = -1

  for j in range(5):
    for k in range(5):
      if helper[i][0] == key_mat[j][k]:
        row1 = j
        col1 = k
      if helper[i][1] == key_mat[j][k]:
        row2 = j
        col2 = k
  if row1 != row2 and col1 != col2:
    helper[i][0] = key_mat[row1][col2]
    helper[i][1] = key_mat[row2][col1]
  elif row1 == row2:
    helper[i][0] = key_mat[row1][(col1+1)%5]
    helper[i][1] = key_mat[row2][(col2+1)%5]
  else:
    helper[i][0] = key_mat[(row1+1)%5][col1]
    helper[i][1] = key_mat[(row2+1)%5][col2]
  i = i+1
print(helper)
ct = ""
for l in helper:
  ct = ct + l[0] + l[1]
print(ct)



# polyalpha
alpha = list('abcdefghijklmnopqrstuvwxyz')

pt = input("Enter PT: ")
key = input("Enter key: ")
ct = ""
k=0
for i in range(len(pt)):
  ct += chr((ord(pt[i]) - ord('a')) + (ord(key[k]) - ord('a')) %26 + ord('a'))
  k = (k+1) % len(key)

dt = ""
k=0
for i in range(len(ct)):
  dt += chr((ord(ct[i]) - ord('a')) - (ord(key[k]) - ord('a')) %26 + ord('a'))
  k = (k+1) % len(key)

print(ct)
print(dt)



# railfence
pt = "himanshu"
key = 3

key_mat = []
for i in range(key):
  key_mat.append([])
  for j in range(len(pt)):
    key_mat[i].append("*")

row = 0
col = 0
dirDown = False

for i in range(len(pt)):
  if row == 0:
    dirDown = True
  elif row == key-1:
    dirDown = False
  key_mat[row][col] = pt[i]
  if dirDown == True:
    row += 1
  else:
    row -= 1
  col += 1

print(key_mat)

cipher= ''
for i in range(key):
  for j in range(len(pt)):
    if key_mat[i][j] != "*":
      cipher += key_mat[i][j]

print(cipher)




# hill cipher
import numpy as np

pt = input("Enter PT: ")
key_mat = np.array([[5, 8], [17, 3]])
key = 2

plain_nums = [ord(char) - ord('a') for char in pt]

if len(pt) % 2 != 0:
  plain_nums.append(23)

cipher_nums = []
for i in range(0, len(pt), key):
  block = plain_nums[i: i+key]
  print(block)
  enc = np.dot(key_mat, block) % 26
  cipher_nums.extend(enc)
ct = ""
for num in cipher_nums:
  ct = ct + chr(num + ord('a'))
print(ct)
det = int(np.round(np.linalg.det(key_mat))) % 26
det_inv = pow(det, -1, 26)

adjugate = np.array([[key_mat[1][1], -key_mat[0][1]], [-key_mat[1][0], key_mat[0][0]]])
key_inv = (det_inv * adjugate) % 26

dec_nums = []
for i in range(0, len(ct), key):
  block = cipher_nums[i: i+key]
  dec = np.dot(key_inv, block) % 26
  dec_nums.extend(dec)
dt = ""
for num in dec_nums:
  dt = dt + chr(num + ord('a'))
print(dt)




# columnar
pt = 'himanshu'
key =2

mat =[[]]
mat[0].extend(['']*key)
row =0
col = 0

for i in range(len(pt)):
  mat[row][col] = pt[i]
  col += 1
  if col == key:
    col = 0
    row += 1
    mat.append([])
    mat[row].extend(['']*key)
print(mat)

cipher =''
for i in range(key):
  for j in range(len(mat)):
    cipher += mat[j][i]

print(cipher)




# rsa
import math

p = 11
q = 13

n = p*q
tot = (p-1)*(q-1)
e = -1
for i in range(2,tot):
  if math.gcd(i,tot) == 1:
    e=i
    break

d = pow(e,-1,tot)
pt = 97
ct = (pt**e) % n
print(ct)
dt = (ct**d) % n
print(dt)




#deffie hellman
p = int(input("Enter prime: "))
g = int(input("Enter generator: "))

sec_a = int(input("Enter secret a: "))
sec_b = int(input("Enter secret b: "))
A = (g**sec_a) % p
B = (g**sec_b) % p
symkey_A = (B**sec_a) % p
symkey_B = (A**sec_b) % p

print("Symmetric Key A: ", symkey_A)
print("Symmetric Key B: ", symkey_B)



# crt
a = [2,3,2]
m = [3,5,7]
M= 1
for mod in m:
  M *= mod
result = sum(ai * (M//mi) * pow(M//mi,-1,mi) for ai,mi in zip(a,m)) % M
print(result)



# el gamal
import random
p = int(input("Enter Prime: "))
g = int(input("Enter Generator: "))
pri = int(input("Enter private key: "))
pub = pow(g, pri, p)

m = int(input("Enter Message: "))
k = int(random.random()*(p-2))
C1 = pow(g, k, p)
C2 = m*pow(pub, k, p)
print([C1, C2])

# Decryption
s = pow(C1, pri, p)
dt = C2*pow(s, -1, p) % p
print(dt)





# hashing
def complexHash(key, size=1000000):
  hash_val = 1
  for char in key:
    hash_val = (hash_val * ord(char)) % size

  return hash_val

class HashChaining:
  def __init__(self, size=1000000):
    self.size = size
    self.table = [[] for _ in range(size)]

  def insert(self, key):
    index = complexHash(key, self.size)
    self.table[index].append(key)

  def display(self):
    print("Hash Table (Chaining):")
    for i, bucket in enumerate(self.table):
      if bucket:
        print(f"Key {str(i).zfill(7)}: {bucket}")

ht_chain = HashChaining()
ht_chain.insert("cat")
ht_chain.insert("dog")
ht_chain.insert("act")
ht_chain.insert("god")
ht_chain.insert("Ishaan")
ht_chain.display()