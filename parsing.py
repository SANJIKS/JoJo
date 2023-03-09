# Mission 1
mom = input('What is your mom name ?: ')
print('My mothers name is',mom,',and i love she')

# MIssion 2 
a = 2*5-1
print(a)
b = (3-5)/2
b = (3-5)//2
print(b)

c = (2+4)*(4-1)
if c == True:
    print(True,c)
else:
    print('error')
print(c)

d = (76 - 34)** 0.5
print(d) 

e = ((43-18) ** 0.5)/14
print(e)

f = ((5-25)**3)/14
print(f)

# Mission 3
dog = 'dog'
cat = 'cat'
humster = 'humster'
print('Do you walk evry day? ')
qw_1 = input('yes or no ')
print('Do like sleep with home animals? ')
qw_2 = input('yes or no ')
if qw_1=='yes' and qw_2=='yes':
  res = dog
  print('You like dog')
elif qw_1=='yes' and qw_2=='no':
  res = dog
  print('Maybe you like dog')
elif qw_1=='no' and qw_2=='no':
    print('Suits you ',humster)
elif qw_1=='no'and qw_2=='yes':
    print('Maybe you like cat')

# Mission 4

dog = 'dog'
cat = 'cat'
horse = 'horse'
print('Which animals are you?')
print('Do you like dirt ?')
qw_1 = input('yes or no ')
print('Do you like many sleep ?')
qw_2 = input('yes or no ')
print('Do you like run ?')
qw_3 = input('yes or no ')
if qw_1=='yes' and qw_2=='yes' and qw_3=='yes':
    print('You are a dog')
elif qw_1=='no' and qw_2=='no' and qw_3=='no':
    print('You are a cat')
elif qw_1=='no' and qw_2=='no' and qw_3=='yes':
    print('You are a horse')
else:
    print('You are a human')