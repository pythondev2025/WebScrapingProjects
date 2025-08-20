import openpyxl


wb = openpyxl.load_workbook("example.xlsx")
sheet = wb["Sheet1"]


def intro(sheet):
    print(wb.sheetnames)
    name = sheet.title
    print(name)
    sheet = wb.active
    print(sheet)
    print(sheet.title)


cell = sheet["B2"]
print(cell.value)
print(cell.coordinate)
print(cell.row)
print(cell.column)
cell2 = sheet["A1"]
print(cell2.value)

# cell.