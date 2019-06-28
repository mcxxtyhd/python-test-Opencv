import xlrd
#只能读不能写
from numpy import int0

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



# for i in range(sheet.ncols):
#     print(sheet.col_values(i))#获取第几列的数据