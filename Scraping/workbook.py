from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter


workbook = Workbook()
worksheet = workbook.active

file_name = "ok1.xlsx"

worksheet.title = "BBC"

ws3 = workbook.create_sheet(title="Data")

ws3.cell(row=1, column=2, value=4)

# for row in range(10, 20):
#     for col in range(27, 54):
#         d = ws3.cell(column=col, row=row)
#         d.value = f"{get_column_letter(col)}"
#         print(f"d:\t{d}\tvalue:\t{d.value}")
# print(ws3.cell(10, 27).value)
workbook.save(file_name)