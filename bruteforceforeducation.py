import itertools
import string 

repeat = 1
my_list = string.digits + string.ascii_letters
product = itertools.product(my_list, repeat=repeat)
password = "test"

while True:
    try:
        combination = next(product)
        temp = "".join(combination)
        print(temp)
        if temp == password:
            print("Şifre bulundu şifre: {}".format(temp))
            break
    except StopIteration:
        my_list_lenght = len(my_list)
        if repeat >= my_list_lenght:
            break
        repeat += 1
        product = itertools.product(my_list, repeat=repeat)