# Basic learning
# Huong will become Expert Data Analyst
# Huong không học đàng quàng sẽ bị Tuấn đánh!!!!
#%% Python Essential Tranining
from unicodedata import name


x = [1,2,3,4,5]
for i in x:
    print(i)
# %%
x = {'one':1,'two':2,'three':3,'four':4,'five':5}
for k,v in x.items():
    print('k is {}, x is {}'.format(k,v))
print (x['one'])
# %%
x=[1,2,3,4,5]
for i in x:
    print ('i is {}'.format(i))
print (x[2])

# %%
x = (1,'two',3.0,[4,'four'],5)
y = (1,'two',3.0,[4,'four'],5)

if isinstance(x,tuple):
    print('true')
else:
    print('nope')
# %%
print('love is {1}{0}'.format('blind','bling'))
# %%
x = 4
y =7
hungry = x + y > 9
x = 'Feed the bear now' if hungry else 'Dont do that'
print (x)
# %%
x=10000
def Digits(x):
    d=1
    if (x>=10):
        d=d+1
    if (x>=100):
        d=d+1
    if (x>=1000):
        d=d+1
    if (x>=10000):
        d=d+1
    return(d)
print (Digits(500))
# %%
x=10000
def Digits(x):
    d=1
    if (x>=10):
        d=d+1
    elif (x>=100):
        d=d+1
    elif (x>=1000):
        d=d+1
    elif (x>=10000):
        d=d+1
    return(d)
print(Digits(x))
# %%
secret = 'fish'
pw = ''
while pw != secret:
    pw = input('what is your secret word?')
else:
    print('you got right pw')

# %%
animals = ('fish','dog','cat')
for pet in animals:
    print(pet)
# %%
secret = 'fish'
pw = ''
auth = False
count = 0
max_attemp = 5

while pw != secret:
    count +=1
    if count > max_attemp: break
    pw = input('What is your secret pw?')
print ('Authorized' if auth else 'Calling FBI')

# %%
animal = ('pet','bunny','chicken', 'cat','dog')
for pet in animal:
    if pet == 'bunny': continue
    if pet == 'cat': break
    print (pet)
else: 
    print ('thats all')
    

# %%
def main():
    kitten()
def kitten ():
    print('Meow.')

if __name__ == '__main__': main()
# %%
def main():
    kitten(5)
def kitten(a,a+=1,a+=2):
    print (a,a+=1,a+=2)

if __name__ =='__main__':main()
# %%
def main():
    x = ('meow','grr','purr','hello')
    kitten(*x)

def kitten(*args):
    print(args)

if __name__=='__main__': main()


# %%
def myfun (*args):
    if len (args):
        for i in argv:
            print (i)
    else: print('Meow')

myfun('Hello','Hi','How','are','you')

# %%

def hi():
    kitten('Hello','Hi','How','are','you')
def kitten(*args):
    if len(args):
        for i in args:
            print(i)
    else: print ('Meow')

if __name__ == '__main__':hi()

# %%
def HuongTuan(**kwargs):
    for k in kwargs:
        print('{} is {}'.format(k,kwargs[k]))

HuongTuan(Huong='Tuan', Tuan = 'Huong', HuongTuan ='Us')
# %%
def HuongTuan(**kwargs):
    for i,k in kwargs.items():
        print('%s == %s' % (i,k))

HuongTuan(Huong='Tuan', Tuan = 'Huong', HuongTuan ='Us')
# %%
def main():
    for i in inclusive_range(5,25,5):
        print(i,end=' ')
    print()
def inclusive_range(*args):
    numargs =len(args)
    start=0
    step =1

    if numargs <1:
        raise TypeError('Expected at least 1 item')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError ('More than 3 items')

    i=start
    while i<=stop:
        yield i
        i+=step

if __name__ == '__main__':main()

# %%
def create_generator():
    mylist = range(4)
    for i in mylist:
        yield i*i

def create_generator_return():
    mylist = range(3)
    for i in mylist:
        return i*i

if __name__ == '__create_generator__': create_generator
# %%
print(create_generator())
print(create_generator_return())

for x in create_generator():
    print(x)