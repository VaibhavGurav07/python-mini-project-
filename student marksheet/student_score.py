# ---- Input Section
# Enter your name : Joy
# Enter Your Roll Number : A1023

# Enter Your JAVA Marks : 50
# Enter Your C++ Marks : 20
# Enter Your go Marks : 25
# Enter Your Ruby Marks : 96
# Enter Your C# Marks : 70
# Enter Your Python Marks : 65

# ---- Output Section
# JAVA = 50/100
# C++ = 20/100 F
# go = 25/100 F
# Ruby = 96/100
# C# = 70/100
# Python = 65/100

# Total = 326/600
# per = 54% FAIL
# IF PASS
# Grading System
# 80 - 100 = Grade A
# 60 - 80 = Grade B
# 35 - 60 = Grade C

name=(input('enter your name:'))
rollno = int(input('enter your Roll no:'))

java=int(input('enter the java marks : '))
cplus=int(input('enter the cplus marks : '))
go=int(input('enter the go marks : '))
ruby=int(input('enter the ruby marks : '))
cslash=int(input('enter the cslash marks : '))
python=int(input('enter the python marks :'))

total = java + cplus + go + ruby + cslash + python

if java>35 :
  print('java',java,'/100')
else:
  print('java',java,'f')

if cplus>35:
  print('cplus',cplus,'/100')
else:
    print('cplus',cplus,'f')

if go>35:
  print('go',go,'/100')
else:
  print('go' ,go,'f')

if ruby>35:
  print('ruby',ruby,'/100')
else:
  print('ruby',ruby, 'f')

if cslash>35:
  print('cslash',cslash,'/100')
else:
  print('cslash',cslash, 'f')

if python>35:
  print('pyhon',python,'/100')
else:
  print('python' ,python, 'f')

print(total,"%")

total_marks = (total *(100/600))
print(total_marks,"%")

if total_marks>=80 and total_marks<100:
  print('your pass in A grade')
elif total_marks>=60 and total_marks<80:
  print('your pass in B grade')
elif total_marks>=35 and total_marks<60:
  print('your pass in C grade')
