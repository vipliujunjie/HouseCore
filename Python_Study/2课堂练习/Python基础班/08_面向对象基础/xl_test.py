import xlwt

new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet("test")
worksheet.write(0, 1, "test2")
new_workbook.save("/Users/junjie/Desktop/向隆维修记录.xls")
