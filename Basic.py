# Basic learning
# Huong will become Expert Data Analyst
# Huong không học đàng quàng sẽ bị Tuấn đánh!!!!
#%% Python Essential Tranining
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
