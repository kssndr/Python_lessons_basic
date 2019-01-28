# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os

current = os.getcwd()
print(os.listdir(current))
for i in range(1,10):
    os.mkdir("dir#"+str(i))
print(os.listdir(current))

for i in range(1,10):
    os.rmdir("dir#"+str(i))
print(os.listdir(current))
print()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

current = os.getcwd()
spisok = os.listdir(current)
for i in spisok:
    print(i)




# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


import os
import sys
import shutil
import re

"""
    скрипт создает папку, копирует туда запущенный файл, потом удаляет скопированный файл и созданную папку
    
    """

print("текущая дирректория:", os.getcwd())
d = sys.argv[0]
print("Запущеный файл", d)
os.mkdir("backup")
shutil.copy(d, "backup")
backup_file = str(os.listdir("backup"))
print("файлы в Backup:", backup_file)
# dd = os.listdir("backup")
# print(dd)
bf = os.path.abspath("backup") # путь к папке, созданной для клонирования файла
# print(bf)
oo = re.sub("[]['']", '', backup_file) # имя скопированного файла для создания пути к его удалению
backup_file_path = bf + '/' + oo
print("путь к файлу в Backup: ", backup_file_path)
os.remove(backup_file_path)
print("проверка Backup после удаления скопированного файла:", os.listdir("backup"))
os.rmdir("backup") # удаление созданной для копирования работающего файла папки
