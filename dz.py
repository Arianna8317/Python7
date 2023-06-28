'''
Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 
'''
import os

def group_rename(end_name: str = "abc", num_digit: int =2, ext_old: str = 'rtf', ext_new: str = 'doc',
                left:int = 2, right:int = 4 ):
    
    dir_list = os.listdir()
    print(dir_list)
    counter = 1
    for file in dir_list:
        if os.path.isfile(file) and file.split(".")[1] == ext_old:
            str_counter = str(counter)
            if len(str_counter)< num_digit:
                for _ in range(num_digit-len(str_counter)):
                    str_counter = "0" + str_counter

            os.rename(file, file.split(".")[0][left:right]+end_name + str_counter + "."+ext_new)
            counter += 1   
                 
group_rename("xxx",num_digit = 3, ext_old="md", ext_new="doc")