yup = "cOULD YOU aPPLY A pRINT STATEMENT?"

# 1


def any_lowercase1(s):
     for c in s:
          if c.islower():
               return True
          else:
               return False
lowercase = any_lowercase1(yup)
print(lowercase)

# 2

def any_lowercase2(s):
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'

lowercase = any_lowercase2(yup)
print(lowercase)

# 3

def any_lowercase3(s):
     for c in s:
          flag = c.islower()
     return flag

lowercase = any_lowercase3(yup)
print(lowercase)

# 4

def any_lowercase4(s):
     flag = False
     for c in s:
          flag = flag or c.islower()
     return flag

lowercase = any_lowercase4(yup)
print(lowercase)

# 5

def any_lowercase5(s):
     for c in s:
          if not c.islower():
               return False
     return True

lowercase = any_lowercase5(yup)
print(lowercase)