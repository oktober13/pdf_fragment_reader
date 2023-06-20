import os
import fitz

def extract_statement_name(file_path, x1, y1, x2, y2):
    doc = fitz.open(file_path)
    page = doc.load_page(0)  # Получаем первую страницу

    # Получаем размеры страницы
    page_width = page.mediabox_size[0]
    page_height = page.mediabox_size[1]

    # Вычисляем координаты в пикселях на основе процентов
    x1_px = int(x1 * page_width / 100)
    y1_px = int(y1 * page_height / 100)
    x2_px = int(x2 * page_width / 100)
    y2_px = int(y2 * page_height / 100)

    # Извлекаем текст из указанного фрагмента страницы
    text = page.get_textbox(fitz.Rect(x1_px, y1_px, x2_px, y2_px))
    statement_name = text.strip()

    doc.close()

    return statement_name

def process_pdf_files(folder_path, output_file, x1, y1, x2, y2):
    with open(output_file, 'w') as output:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.pdf'):
                file_path = os.path.join(folder_path, file_name)
                statement_name = extract_statement_name(file_path, x1, y1, x2, y2)
                output.write(f'{file_name} - {statement_name}\n')

# Заданные параметры
folder_path = 'pdf_documents'
output_file = 'result.txt'
x1, y1, x2, y2 = 20, 30, 40, 50

process_pdf_files(folder_path, output_file, x1, y1, x2, y2)
