import os

file = open('data.txt', 'a')

file.write('Hello, world of python files\n')

file.close()

try:
    file = open('data.txt', 'r')
    data = file.read()
    print(data)
    file.close()
except:
    pass
    # print('Something went wrong')



# os.remove('data.txt')

# print(os.path.exists('data.txt'))

def add():
    pass

if 10 > 11:
    pass



def get_dimens(image):
    return 10, 20, "png"

l, w, ext = get_dimens("image")

pops = [10, 9, 32]

x, y, z = pops

print(x)