#Дана строка в виде случайной последовательности чисел от 0 до 9.
#Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
#а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте
#функцию count_it(sequence), принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.



#The given string has given the list of traces of numbers from 0 to 9.
#It is required to set up a vocabulary, for example keys will accept data about numbers
#(i.e., keys will be of type int),and for such signs - a number of numbers from the same inheritance.
#To induce the vocabulary, open the function count_it (last), I will accept a string of numbers.
#The function is guilty to turn to the word of the 3 most common system numbers.




def count_it(sequence):
    num_frequency = {int(item): sequence.count(item) for item in sequence}
    sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])

    return dict(sorted_num_frequency[-3:])

print(count_it('1111111111222'))
print(count_it('123456789012133288776655353535353441111'))
print(count_it('007767757744331166554444'))