import os

def dir_inf(path=os.getcwd()):
     for root, dirs, files in os.walk(path):
         print('Текущая директория: ', root)
         print("-" * 10)

         if dirs:
             print("Список папок:", dirs)
         else:
             print('Папок нет')

         if files:
            print('Список файлов: ', files)
         else:
             print('Файлов нет')

         if files and dirs:
             for f in files:
                 print('Файл', os.path.join(root, f))
             for d in dirs:
                 print("Папка", os.path.join(root, d))
         print('=' * 10)




dir_inf('D:\\new_life_new_dir\Skillfactory')