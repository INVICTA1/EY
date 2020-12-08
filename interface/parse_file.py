import datetime

from .mysqlConnector import insert_request_in_database
from enum import Enum
import xlrd

def get_data_from_database(file_id):
    request = 'select * from sheet where file_id = {0};'.format(file_id)
    rows = insert_request_in_database(request)
    return rows
def insert_rows_in_database(rows):
    request = 'insert into sheet values'
    for row in rows:
        request += '(' + str(row[0]).replace(' ', ',') + ')' + ','
    request = request[:-1] + ';'
    insert_request_in_database(request)

def insert_name_table_in_database(file_id,name):
    request = "insert into file() values({0},'{1}','{2}');".format(file_id,name,datetime.datetime.today())
    insert_request_in_database(request)


def insert_data_in_database(file, file_id):
    name = str(file).split('/')[1]
    start_row_number = 8
    rb = xlrd.open_workbook(file, formatting_info=True)
    sheet = rb.sheet_by_name('Sheet1')

    class ClassType(Enum):
        class_1 = 'КЛАСС  1  Денежные средства, драгоценные металлы и межбанковские операции'
        class_2 = 'КЛАСС  2  Кредитные и иные активные операции с клиентами'
        class_3 = 'КЛАСС  3  Счета по операциям клиентов'
        class_4 = 'КЛАСС  4  Ценные бумаги'
        class_5 = 'КЛАСС  5  Долгосрочные финансовые вложения в уставные фонды юридических лиц, основные средства и прочее имущество'
        class_6 = 'КЛАСС  6  Прочие активы и прочие пассивы'
        class_7 = 'КЛАСС  7  Собственный капитал банка'
        class_8 = 'КЛАСС  8  Доходы банка'
        class_9 = 'КЛАСС  9  Расходы банка'
    rows = []
    data = []
    temp_class_type = ''
    for row_itr in range(start_row_number, sheet.nrows):
        cells = sheet.row_values(row_itr)
        if str(cells[0]) == 'ПО КЛАССУ' or str(cells[0]).__contains__('БАЛАНС'):
            continue
        if str(cells[0]).__contains__('КЛАСС'):
            temp_class_type = ClassType(str(cells[0])).name
            continue
        is_valid_row = False
        for cell_itr in range(7):
            data = []
            if cells[cell_itr] != '':
                is_valid_row = True
        if is_valid_row:
            data.append(str("{0},{1},{2},{3},{4},{5},{6},'{7}',{8}").format((cells[0]), cells[1], cells[2], cells[3], cells[4], cells[5], cells[6],temp_class_type ,int(file_id)))
            rows.append(data)
    insert_name_table_in_database(file_id,name)
    insert_rows_in_database(rows)


if __name__ == "__main__":
    pass
