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
            
if __name__ == '__main__':
    list_datas = [
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.54-7', 'Criação de suínos', '0154-7/00', 'Criação de suínos'],
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.55-5', 'Criação de aves', '0155-5/01', 'Criação de frangos para corte'],
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.55-5', 'Criação de aves', '0155-5/02', 'Produção de pintos de um dia'],
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.55-5', 'Criação de aves', '0155-5/03', 'Criação de outros ga...para corte'],
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.55-5', 'Criação de aves', '0155-5/04', 'Criação de aves, exc...galináceos'],
        ['A', 'AGRICULTURA, PECUÁRI...QÜICULTURA', '01', 'AGRICULTURA, PECUÁRI...LACIONADOS', '01.5', 'Pecuária', '01.55-5', 'Criação de aves', '0155-5/05', 'Produção de ovos']
        ]

    obj =  CreateExcel()
    obj.set_sheet_name()
    obj.set_headers()
    obj.write_lines(list_datas)
    obj.save_excel()
    ...