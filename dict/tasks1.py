#Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs),
#которая принимает неограниченное количество параметров «ключ: значение» и
#обновляет созданный им словарь my_dict, состоящий всего из одного элемента
#«first_one» со значением «we can do it». Воссоздайте эту функцию.

#Ivan decided to create the largest dictionary in the world.
#To do this, he came up with the most_dict (** kwargs) function,
#which takes an unlimited number of key: value parameters and updates the
#dictionary he created my_dict, which consists of only one element “first_one” with the value “we can do this”.
#Recreate this function.

my_dict = {'first_one': 'we can do it'}


def biggest_dict(**kwargs):
    my_dict.update(**kwargs)


biggest_dict(k1=22, k2=31, k3=11, k4=91)
biggest_dict(name='Andrey', age=31, weight=61, eyes_color='grey')
print(my_dict)