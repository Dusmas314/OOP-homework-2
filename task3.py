file1 = open('1.txt', encoding='utf-8')
strings1 = file1.readlines()
len1 = len(strings1)
file2 = open('2.txt', encoding='utf-8')
strings2 = file2.readlines()
len2 = len(strings2)
file3 = open('3.txt', encoding='utf-8')
strings3 = file3.readlines()
len3 = len(strings3)


def printer(file_name, input_file, output_file):
    output_file.write(file_name)
    output_file.write('\n')
    output_file.write(str(len(input_file)))
    output_file.write('\n')
    for line in input_file:
        output_file.write(line)
    output_file.write('\n')
final_file = open('final_file.txt', 'a', encoding='utf-8')


max = len1
min = len1
if len2 < min:
    min = len2
if len3 < min:
    min = len3
if len2 > max:
    max = len2
if len3 > max:
    max = len3
avg = len1 + len2 + len3 - min - max
if min == len1:
    printer('1.txt', strings1, final_file)
    len1 = -1
if min == len2:
    printer('2.txt', strings2, final_file)
    len2 = -1
if min == len3:
    printer('3.txt', strings3, final_file)
    len3 = -1
if avg == len1:
    printer('1.txt', strings1, final_file)
    len1 = -1
if avg == len2:
    printer('2.txt', strings2, final_file)
    len2 = -1
if avg == len3:
    printer('3.txt', strings3, final_file)
    len3 = -1
if max == len1:
    printer('1.txt', strings1, final_file)
if max == len2:
    printer('2.txt', strings2, final_file)
if max == len3:
    printer('3.txt', strings3, final_file)
file1.close()
file2.close()
file3.close()