import subprocess
import os 
print(subprocess.check_call("DIR", shell=True))


def find_all_files_in_dir(path):
    list_of_files = os.listdir(path)
    result = 0
    for i in list_of_files:
        for j in i:
            if j == '.':
                result+=1

    return result

abspath = os.path.abspath(".")
for dirpath, dirnames, filenames in os.walk("."):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог:", os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        print("Файл:", os.path.join(dirpath, filename))
print(find_all_files_in_dir(abspath))