from openpyxl import Workbook, load_workbook

workbook = Workbook()
# worksheet = workbook.active
'''
worksheet1 = workbook.create_sheet("My_sheet")
worksheet2 = workbook.create_sheet("My_sheet_2", 0)
worksheet3 = workbook.create_sheet("My_sheet_3", -1)

worksheet.title = "New Title"
worksheet.sheet_properties.tabColor = "1072BA"
worksheet3 = workbook["New Title"]
print(workbook.sheetnames)

worksheet["A1"] = "hello"
worksheet["B1"] = "world!"
cell = worksheet['A4']
worksheet['A4'] = 4
'''
name_file = "work_Book.xlsx"
workbook = load_workbook(name_file)
print(workbook.sheetnames)
worksheet = workbook['New Title']
cell = worksheet['A4']
print(f"cell:\t{cell.value}\na4:\t{worksheet['A4'].value}")
print(f"cell():\t{worksheet.cell(row=4, column= 1).value}")

cell.value = 10
for row in worksheet.iter_rows(min_row=1, max_col=3, max_row=4, values_only=True):
    print(row)
workbook.save(filename=name_file)