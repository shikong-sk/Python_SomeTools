import xlrd
import xlsxwriter
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) < 7:
        print("====================")
        print(sys.argv[0] + " 文件路径 包含文件名 表头行数 数据结束行 必填字段列号 忽略包含的文件名")
        print("表头行数 从 1 开始 \t 若无则为 -1")
        print("数据结束行 从 1 开始 \t 若无则为 -1")
        print("必填字段列号 从 1 开始 \t 可设置多个以 , 分隔")
        print("忽略含有指定字符串的文件 \t 可设置多个以 , 分隔")
        print(sys.argv)
        sys.exit(0)

    data = []
    requireColumn = []
    root = sys.argv[1]
    keyword = sys.argv[2]
    headRow = int(sys.argv[3])
    endRow = int(sys.argv[4])
    for i in sys.argv[5].split(","):
        requireColumn.append(int(i))

    ignoreList = []
    for i in sys.argv[6].split(","):
        ignoreList.append(i)

    root = os.path.join(root)
    fileList = []
    # headRow = -1
    # endRow = -1

    # 起始位置
    # headRow = 5
    # # 结束位置
    # endRow = 25
    # # 必填字段
    # requireColumn = [2]

    for root, dirs, files in os.walk(root):
        for file in files:
            if keyword in file:
                flag = True
                for ignore in ignoreList:
                    if ignore in file:
                        flag = False
                        break
                if flag:
                    fileList.append(os.path.join(root, file))

    for file in fileList:
        xlsx = xlrd.open_workbook(file)
        assert isinstance(xlsx, xlrd.Book)

        for sheet in xlsx.sheets():
            assert isinstance(sheet, xlrd.sheet.Sheet)
            for row in range(sheet.nrows):
                if row in range(headRow - 1):
                    continue
                elif endRow != -1 and row >= endRow - 1:
                    break

                tmp = sheet.row_values(row)

                if len(requireColumn) != 0:
                    flag = True
                    for require in requireColumn:
                        if require - 1 >= sheet.ncols:
                            print("必填字段不正确")
                            sys.exit(0)
                        if tmp[require - 1] == "":
                            flag = False
                            break
                    if flag:
                        data.append(sheet.row_values(row))
                else:
                    data.append(sheet.row_values(row))
    for x in data:
        print(x)

    excelFile = xlsxwriter.Workbook(os.path.join(root, keyword + "_汇总.xlsx"))
    assert isinstance(excelFile, xlsxwriter.Workbook)

    sheet = excelFile.add_worksheet()
    assert isinstance(sheet, xlsxwriter.Workbook.worksheet_class)

    font = excelFile.add_format({"font_size": 12})
    for i in range(len(data)):
        for j in range(len(data[i])):
            sheet.write(i, j, data[i][j], font)
    excelFile.close()

    print("共计写入：" + str(len(data)) + "条数据")
