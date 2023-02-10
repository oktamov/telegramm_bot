import csv
import os.path




def write_csv(student):
    with open('studentt.csv', 'a+', newline='\n', encoding='utf-8') as f:
        header = ['chat_id', 'fullname']
        csv_writer = csv.DictWriter(f, header)
        if os.path.getsize('studentt.csv') == 0:
            csv_writer.writeheader()
        csv_writer.writerow(student.get_attrs())

def get_students_from_csv():
    with open("studentt.csv") as f:
        csv_reader = csv.DictReader(f)
        return chat_id in [row.get("chat_id") for row in csv_reader]
