from xlutils.copy import copy
import xlrd

book = xlrd.open_workbook('test.xlsx')#打开一个excel
sheet = book.sheet_by_index(0)#根据顺序获取sheet
sheet2 = book.sheet_by_name('Sheet1')#根据sheet页名字获取sheet

target_danyuange=sheet.col_values(3)
target_all=[]
for single in range(len(target_danyuange)):
    if target_danyuange[single]==42:
        target_all.append([single,3])


second_danyuange=sheet.col_values(7)
second_target_all=[]
for single_seconde in range(len(second_danyuange)):
    if second_danyuange[single_seconde]!='':
        second_target_all.append([single_seconde,2,second_danyuange[single_seconde]])

print('这是结果：')
print(target_all)

print('这是结果1111：')
print(second_target_all)#取第二列的数据


#xlutils:修改excel
book1 = xlrd.open_workbook('test.xlsx')
book2 = copy(book1)#拷贝一份原来的excel
# print(dir(book2))
sheet = book2.get_sheet(0)#获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的

for org_item in range(len(target_all)):

    sheet.write(target_all[org_item][0],target_all[org_item][1], str(second_target_all[org_item][2]))


book2.save('stu.xls')

# sheet.write(1,3,0)
# sheet.write(1,0,'hello')