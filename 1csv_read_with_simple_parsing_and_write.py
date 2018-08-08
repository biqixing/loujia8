#！/usr/bin/env python3
#导入基础需要的模块
import sys

#从前台传值赋给变量分别为导入文件名和导出文件名
input_file=sys.argv[1]
output_file=sys.argv[2]


#打开输入文件，写入内容

with open(input_file,'r',newline='') as filereader:
	with open(outfilr,'w',newline='') as filewriter:
		header=filereader.readline()
		header=header.strip()
		header_list=header.split(',')
		print(header_list)
#写入内容 map函数的用法 map(fun,varable)对值进行fun 操作

        filewriter.write(','.join(map(str,header_list))+'\n')
        for row in filereader:
        	row=row.strip()
        	row_list=row.split(',')
        	print(row_list)
            filewriter.write(',',join(map(str,row_list)+'\n'))


#----这是一个test