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
combo_file = "backup_list.txt" # Файл со списком директорий и файлов, которые должны попасть в архив
zip_path = "/home/zampolit/" # Путь для сохранения zip файла
######################
### Секция импорта ###
import os, zipfile, datetime
######################
lines = [line.rstrip('\n') for line in open(combo_file)]                        # Мы получаем список файлов и директорий, которые нужно архивировать
zip_date = str(datetime.date.today())                                           # Получаем текущую дату и время, для формирования имени zip файла
zip_name = 'Backup_' + zip_date + ".zip"                                        # Строка с названием zip файла

for i in lines:
    if os.path.isfile(i):
        print(i, 'Это файл')
    elif os.path.isdir(i):
        print(i, 'это папка')
    else: print(i, 'Это непонятно что')

print(zip_name, 'Так будет называться архив')
print(lines, 'Это список файлов и каталогов, которые нужно добавить в архив')
print(zip_path, 'Сюда будет сохраняться архив')
z = zipfile.ZipFile('spam.zip', 'w')
for k in lines:

    for root,dirs, files in os.walk(k):
        for file in files:
            z.write(os.path.join(root, file))
z.close()