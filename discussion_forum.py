low = "c"
cap = "C"

print("__#1__")

# 1
def any_lowercase1(s):
     for c in s:
          if c.islower():
               return True
          else:
               return False
               
lowercase = any_lowercase1(low)
lowercase2 = any_lowercase1(cap)

print(lowercase)
print(lowercase2)

print("__#2__")

# 2
def any_lowercase2(s):
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'

lowercase = any_lowercase2(low)
lowercase2 = any_lowercase2(cap)

print(lowercase)
print(lowercase2)

print("__#3__")

# 3
def any_lowercase3(s):
     for c in s:
          flag = c.islower()
     return flag

lowercase = any_lowercase3(low)
lowercase2 = any_lowercase3(cap)

print(lowercase)
print(lowercase2)

print("__#4__")

# 4
def any_lowercase4(s):
     flag = False
     for c in s:
          flag = flag or c.islower()
     return flag

lowercase = any_lowercase4(low)
lowercase2 = any_lowercase4(cap)

print(lowercase)
print(lowercase2)

print("__#5__")

# 5
def any_lowercase5(s):
     for c in s:
          if not c.islower():
               return False
     return True

lowercase = any_lowercase5(low)
lowercase2 = any_lowercase5(cap)

print(lowercase)
print(lowercase2)

# alt print
# print("Returns: ", lowercase, " Type is: ", type(lowercase))
# print("Returns: ", lowercase2, " Type is: ", type(lowercase2))