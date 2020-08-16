#!/usr/bin/env python3
"""
Скрипт для бэкапа важных файликов, сохраняется в zip файл. Название архива -
- дата создания. Скрипт написан в Августе 2020г как практический урок при обу-
чении программировании на Python3
Условия ТЗ:
1) Файлы и каталоги, которые необходимо скопировать, собираются в список;
2) Резервные копии должны храниться в основном каталоге резерва
3) Файлы помещаются в .zip архив
4) Именем архива служит текущая дата и время
"""
### Секция настроек###
combo_file = "/home/zampolit/PycharmProjects/Backuper/backup_list.txt"                                                  # Файл со списком директорий и файлов, которые должны попасть в архив
zip_path = "/home/zampolit/Backup/" # Путь для сохранения zip файла
max_zip_files = 5                                                                                                       # Количество файлов в папке с архивами
######################
### Секция импорта ###
import os, zipfile, datetime, glob
######################
oldest_zip=[]                                                                                                           # Пока пустой список. Используется позднее для сортировки zip файлов по дате создания
new_list_zip=[]
lines = [line.rstrip('\n') for line in open(combo_file)]                                                                # Мы получаем список файлов и директорий, которые нужно архивировать
zip_date = str(datetime.date.today())                                                                                   # Получаем текущую дату и время, для формирования имени zip файла
zip_name = zip_path + 'Backup_' + zip_date + ".zip"                                                                     # Строка с названием zip файла
z = zipfile.ZipFile(zip_name, 'w')
for k in lines:
    for root, dirs, files in os.walk(k):
        for file in files:
            z.write(os.path.join(root, file))
z.close()
#### Считаем, сколько файлов zip содержиться в директории zip_path ###
for root, dirs, files in os.walk(zip_path):                                     # Получаем все файлы в каталоге с архивами
    for am in files:                                                            # Перебираем каждый файл
        oldest_zip.append(am)                                                   # Добавляем все названия файлов в список файлов каталога с zip файлами
print(oldest_zip)                                                               # Печатаем список всех файлов в папке с zip
for ups in oldest_zip:

    print(ups)
summa_zip = len(list(glob.iglob(str(zip_path+"*.zip"), recursive=True)))        # Количество файлов .zip в каталоге архива
if summa_zip > 5:
    print('больше 5, нужно удалять')
else: print('меньше 5, не нужно удалять')
print(summa_zip)

##########################
for root, dirs, files in os.walk(zip_path):                                     # Получаем все файлы в каталоге с архивами
    for am in files:                                                            # Перебираем каждый файл
        oldest_zip.append(am)                                                   # Добавляем все названия файлов в список файлов каталога с zip файлами
print(oldest_zip)                                                               # Печатаем список всех файлов в папке с zip
for a in oldest_zip:
    if a.startswith("Backup") and a.endswith(".zip"):
        new_list_zip.append(a)
    else:
        print('не подходит нам такое', a)
print(new_list_zip)
new_list_zip.sort()
c = len(new_list_zip)
if c>max_zip_files:
    print("В списке много файлов, надо лишний удалить", new_list_zip)
    d = new_list_zip[0]
    print(d)
    os.remove(zip_path+d)
else:
    print('В списке файлов недостаточно, для удаления, ждем дальше')