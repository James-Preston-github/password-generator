import random as rd
characters=[]
letters='qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM!@£$%^&*()'
for i in letters:
    characters.append(i)


def password_generator(length):
    i=0
    pword=''
    while i<=length:
        pword+=(characters[rd.randint(0,len(characters)-1)])
        i+=1
    return pword
x=int(input('How long do you want your password to be'))
z=int(input('How many passwords do you want'))
pass_generator=(password_generator(x) for y in iter(int,1))
for i in range(0,z):
    print(next(pass_generator))