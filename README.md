# PDF Fragment Reader

Это скрипт на языке Python, предназначенный для извлечения названий заявлений из PDF-файлов. Он обрабатывает несколько PDF-файлов в указанной папке, считывает названия заявлений из заданных координат на каждой странице и сохраняет их в текстовый файл.

## Установка

1. Убедитесь, что на вашей системе установлен Python 3.x.
2. Клонируйте этот репозиторий на ваш компьютер.

## Использование

1. Поместите ваши PDF-файлы в папку `pdf_documents`.
2. Откройте файл `main.py` и установите следующие параметры:
   - `folder_path`: Путь к папке, содержащей PDF-файлы.
   - `output_file`: Имя текстового файла, в который будут сохранены результаты.
   - `x1`, `y1`, `x2`, `y2`: Координаты (в процентах) фрагмента на странице, из которого нужно извлечь название заявления.
3. Запустите скрипт `main.py`, используя команду `python main.py`.
4. Извлеченные названия заявлений будут сохранены в указанном `output_file`.

## Требования

Необходимые пакеты Python можно установить с помощью следующей команды:

```sh
pip install -r requirements.txt
```

## Лицензия

Этот проект не требует лицензии
