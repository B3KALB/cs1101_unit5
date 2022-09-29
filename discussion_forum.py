yup = "cOULD YOU aPPLY A pRINT STATEMENT?"
yup2 = "Could you Apply a Print statement?"

print("__#1___")# 1

def any_lowercase1(s):
     for c in s:
          if c.islower():
               return True
          else:
               return False
               
lowercase = any_lowercase1(yup)
lowercase2 = any_lowercase1(yup2)
print(lowercase)
print(lowercase2)

print("__#2___")# 2

def any_lowercase2(s):
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'

lowercase = any_lowercase2(yup)
lowercase2 = any_lowercase2(yup2)
print(lowercase)
print(lowercase2)

print("__#3___")# 3

def any_lowercase3(s):
     for c in s:
          flag = c.islower()
     return flag

lowercase = any_lowercase3(yup)
lowercase2 = any_lowercase3(yup2)
print(lowercase)
print(lowercase2)

print("__#4___")# 4

def any_lowercase4(s):
     flag = False
     for c in s:
          flag = flag or c.islower()
     return flag

lowercase = any_lowercase4(yup)
lowercase2 = any_lowercase4(yup2)
print(lowercase)
print(lowercase2)

print("__#5___")# 5

def any_lowercase5(s):
     for c in s:
          if not c.islower():
               return False
     return True

lowercase = any_lowercase5(yup)
lowercase2 = any_lowercase5(yup2)
print(lowercase)
print(lowercase2)