# Basic learning
# Huong will become Expert Data Analyst
# Huong không học đàng quàng sẽ bị Tuấn đánh!!!!
#%% Python Essential Tranining
from ossaudiodev import SOUND_MIXER_ALTPCM
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
""" Day 6"""
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

# %%
"""Day 7"""
def f1(f):
    def f2():
        print ('this is before the function call')
        f()
        print('this is after the function call')
    return f2()

def f3():
    print('this is f3')

a = f1(f3)
a()

# %%
import time
x = time.time()
print (x)
# %%
import time
def elapsed_time(big_sum):
    def wrapper():
        t1 = time.time()
        big_sum()
        t2=time.time()
        print(f'Elapsed time:{(t2-t1)*1000}ms')
    return wrapper

def big_sum():
    num_list= []
    for num in (range(0,10000)):
        num_list.append(num)
    print (f'Big sum: {sum(num_list)}')

main = elapsed_time(big_sum)
main()



# %%
def F1(f):
    print('A')
    def F2():
        print('B')
        f()
        print('C')
    print('D')
    return F2
@F1
def F3():
    print('E')
F3()
# %%
def Func (a,b):
    a=1; b[0]=1


x=0 ; y=[0]
print(y)
Func(x, y)
print(x, y)
# %%
"""Day 8"""
def main():
    game = ['Rock','Paper','Scissors','Lizard','Spock']
    game.append('Computer')
    print(game)

def print_list(o):
    for i in o: print (i, end =' ', flush = True)
    print()

if __name__ == '__main__': main()
# %%

# %%
def main():
    game = ['Rock','Paper','Scissors','Lizard','Spock']
    game.insert(1,'Computer')
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush= True)
    print()

if __name__ == '__main__': main()
# %%
def main():
    game = ['Rock','Paper','Scissors','Lizard','Spock']
    game.remove('Paper')
    print_list(game)

def print_list(o):
    for i in o: print(i, end =' ', flush = True)

if __name__ == '__main__':main()
# %%
def main():
    game = ['Rock','Paper','Scissors','Lizard','Spock']
    x=game.pop()
    print(x)
    print_list(x)

def print_list(o):
    for i in o: print(i, end =' ', flush = True)

if __name__ == '__main__':main()
# %%
def main():
    game = ['Rock','Paper','Scissors','Lizard','Spock']
    del game[1:3]
    print_list(game)

def print_list(o):
    for i in o: print(i, end =' ', flush = True)

if __name__ == '__main__':main()
# %%
def main():
    game = ['Rock','Paper','Scissors','Lizard','Spock']
    print(', '.join(game))
    print_list(game)

def print_list(o):
    for i in o: print(i, end =', ', flush = True)

if __name__ == '__main__':main()
# %%
"""Dictionary Option 1"""
def main():
    animals = {'kitten':'meow', 'puppy' :'ruff', 'lion' :'grr', 'giraffe' :'I am a giraffe','dragon':'rawr'}
    print_dict(animals)

def print_dict(o):
    for k,v in o.items(): print (f'{k} is {v}')

if __name__ == '__main__': main()

# %%
animals = {'kitten':'meow', 'puppy' :'ruff', 'lion' :'grr', 'giraffe' :'I am a giraffe','dragon':'rawr'}
for k,v in animals:
    print(f'{k} is {v}')
# %%
"""Dictionary Option 2"""
def main():
    animals = {'kitten':'meow', 'puppy' :'ruff', 'lion' :'grr', 'giraffe' :'I am a giraffe','dragon':'rawr'}
    animals['monkey'] ='haha'
    print_dict(animals)

def print_dict(o):
    for x in o: print (f'{x} is {o[x]}')

if __name__ == '__main__': main()

# %%
def main():
    animals = dict(kitten='meow', puppy ='ruff', lion ='grr', giraffe ='I am a giraffe',dragon='rawr')
    print_dict(animals)

def print_dict(o):
    for k in o.keys(): print (k)

if __name__ == '__main__': main()
# %%
def main():
    animals = dict(kitten='meow', puppy ='ruff', lion ='grr', giraffe ='I am a giraffe',dragon='rawr')
    print_dict(animals)

def print_dict(o):
    for k in o.values(): print (k)

if __name__ == '__main__': main()
# %%
"""Print_set a -b """
def main():
    a = set ("abc.")
    b = set (" cde?")
    print_set(a-b)


def print_set(o):
    print('{',end='')
    for x in o: print(x,end='')
    print('}')

if __name__ == '__main__': main()

# %%
"""Print_set a or b"""
def main():
    a = set ("abc.")
    b = set (" cde?")
    print_set(a|b)


def print_set(o):
    print('{',end='')
    for x in o: print(x,end='')
    print('}')

if __name__ == '__main__': main()
# %%
"""Print_set mutual elements between a & b"""
def main():
    a = set ("abc.")
    b = set (" cde?")
    print_set(a^b)


def print_set(o):
    print('{',end='')
    for x in o: print(x,end='')
    print('}')

if __name__ == '__main__': main()
# %%
"""Print_set appearin both set a & b"""
def main():
    a = set ("abc.")
    b = set (" cde?")
    print_set(a&b)


def print_set(o):
    print('{',end='')
    for x in o: print(x,end='')
    print('}')

if __name__ == '__main__': main()
# %%
"""Day 9"""
def main():
    seq = range(11)
    seq2= [x*2 for x in seq]
    print_list (seq)
    print_list (seq2)

def print_list(o):
    for x in o:
        print (x, end =' ')
    print ()

if __name__=='__main__': main()

# %%
def main():
    seq = range(11)
    seq2= [x for x in seq if x%3 !=0]
    print_list (seq)
    print_list (seq2)

def print_list(o):
    for x in o:
        print (x, end =' ')
    print ()

if __name__=='__main__': main()
# %%
def main():
    seq = range(11)
    seq2= {x:x*2 for x in seq if x%3 !=0}
    print_list (seq)
    print_dict (seq2)

def print_list(o):
    for x in o:
        print (x, end =' ')
    print ()

if __name__=='__main__': main()
# %%
"""Líst of a set"""
def main():
    seq = range(11)
    seq2= {x for x in 'hello how are you doing??' if x not in 'h?' }
    print_list (seq)
    print_set (seq2)

def print_list(o):
    for x in o:
        print (x, end =' ')
    print ()

if __name__=='__main__': main()
# %%
x = ['-','-','X','X']
x.insert(0,x.pop())
# %%
"""Day 10"""
class Duck:
    sound = 'Quack quack'
    movement = 'Walk like a duck'
    def quack(self):
        print(self.sound)
    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    donald.quack()
    donald.move()

if __name__ =='__main__': main()
# %%
class Animal:
    def __init__(self,type,name,sound):
        self._type = type
        self._name = name
        self._sound = sound 
    def type (self):
        return self._type
    def name(self):
        return self._name
    def sound(self):
        return self._sound
def print_animal(o):
    if not isinstance(o,Animal):
        raise TypeError ('print_animal():requires an Animal')
    print ('The {} is named "{}" and says "{}".'.format(o.type(),o.name(),o.sound()))
def main():
    a0= Animal('kitten','fluffy','rwar')
    a1 = Animal ('duck','donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velo','vero','hello'))

if __name__ == '__main__':main()


# %%
def main():
    animal_name = {'fluffy' : 'rwar', 'donald' :'quack', 'velo' : 'helo'}
    print_dict(animal_name)
def print_dict(o):
    for i,k in o.items():
        print('The {} says {}'.format(i,k))

if __name__ == '__main__': main()
# %%
class Animal:
    def __init__(self,type,name,sound):
        self._type = type
        self._name = name
        self._sound = sound
    def type(self):
        return self._type
    def name(self):
        return self._name
    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance (o,Animal):
        raise TypeError ('Wrong')
    print('This is {} called "{}" says "{}"'.format(o.type(),o.name(),o.sound()))

def main():
    a = Animal('fluffy','cat','rwar')
    print_animal(a)

if __name__ == '___main__': main()

#%% 
class Animal:
    def __init__(self,**kwargs):
        self._type = kwargs['type']
        self._name = kwargs['name']
        self._sound = kwargs['sound']
    def type(self):
        return self._type
    def name(self):
        return self._name
    def sound(self):
        return self._sound

def main():
   a0 = Animal(type ='kitten', name ='fluffy', sound = 'meow')
   print_animal(a0)

def print_animal(o):
    if not isinstance (o, Animal):
        raise TypeError ('Wrong')
    print('This is {} called {} says {}'.format(o.type(), o.name(), o.sound()))
if __name__ == '__main__': main()

#%%
class Animal:
    def __init__(self,**kwargs):
        self._type =kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'
    def type(self,t=None):
        if t: self._type=t
        return self._type
    def name(self, n= None):
        if n:self_name = n
        return self._name
    def sound(self, s=None):
        if s:self_sound = s
        return self._sound
    def __str__(self):
        return f'The {self._type()} is named "{self._name}" and says "{self._sound}" '

def main():
    a0= Animal(type ='dog',name='puppy',sound='gauz')
    a1= Animal (type ='chicken',name='chic', sound ='quack')
    print(a0)
    print(a1)

if __name__=='__main__': main()
# %%
def main():
    try: x=int('foo')
    except ValueError: print('Wrong')
if __name__=='__main__': main()

# %%

def main():
    try: 
        print (x)
    except ValueError: 
        print ('Value Error roi kia')
    except ZeroDivisionError:
        print ('Chia cho 0 la ngu ngok')

if __name__=='__main__':main()

0
# %%
class Animal:
    def __init__(self,type,name,sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type
    def name(self):
        return self._name
    def sound(self):
        return self._sound
def print_animal(o):
    if not isinstance (o,Animal): raise TypeError ('Loi roi ma')
    print ('This is {} called {} says {}'.format (o.type(),o.name(),o.sound()))
    
def main():
    a0 = Animal('cat','puppy','meow')
    print_animal(a0)

if __name__ == '__main__':main()
# %%
def inclusive_range(*args):
    numargs = len(args)
    start=0
    step =1
    #initialize parameters
    if numargs < 1:
        raise TypeError ('Expected at list 1 argument')
    elif numargs ==1:
        stop = args[0]
    elif numargs ==2: 
        (start,stop) = args
    elif numargs ==3:
        (start,stop,step)=args
    else:
        raise TypeError('Loi roi')

    i = start
    while i <= stop:
        yield i
        i += step

def main():
    try:
        for i in inclusive_range(4,100,5,4,9):
            print (i,end=' ')
    except TypeError as e:
        print (f'range error:{e}')

        
if __name__=='__main__':main()
    
# %%
class Mystring(str):
    def __str__(self):
        return self.upper()
s = Mystring('Hello World')
print (s)

# %%
print ('hello WORrld'.swapcase())
# %%
"""Day 11"""
x = 43
y = 71 

print ('Hello I am {0:10} and you are {1:5}'.format(x,y))
# %%
x =50*1000*200
print('Hello co gang len {:,}'.format(x))
# %%

