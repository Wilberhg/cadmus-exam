from xlsxwriter import Workbook
import os

class CreateExcel:
    def __init__(self, excel_path=os.getcwd()+'\\files', excel_name='VagasCadmus.xlsx'):
        self.excel_path = excel_path
        self.excel_name = excel_name
        os.makedirs(self.excel_path, exist_ok=True)
        self.wb = Workbook(self.excel_path+"\\"+self.excel_name)

    def set_sheet_name(self):
        self.ws = self.wb.add_worksheet('Cadmus')

    def set_headers(self):
        bold = self.wb.add_format({'bold': 1})
        self.ws.write_string('A1', 'Nome', bold)
        self.ws.write_string('B1', 'Local', bold)
        self.ws.write_string('C1', 'Descrição', bold)

    def write_lines(self, table_datas):
        row = 1
        col = 0

        for nome, local, descricao in table_datas:
            self.ws.write_string(row, col, nome)
            self.ws.write_string(row, col+1, local)
            self.ws.write_string(row, col+2, descricao)
            row += 1

    def save_excel(self):
        self.wb.close()