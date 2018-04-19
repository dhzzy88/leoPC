#!/bin/python3
# author:LeoZhao

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
import os
import sys
'''
 解析pdf 文本，保存到txt文件中
'''
#path = '.pdf'


def parse(path):
    txtname = path.split("/")[-1].split(".")[0]+"."+"txt"
    if os.path.isfile(txtname):
        print("文件已经存在：", txtname)
        print("接下来的操作将会删除已经存在的文件：\t", txtname)
        a = input("你确定吗？   (y or n)")
        if a.lower()=="y":
            with open(txtname, "w") as f:
                f.write("")
        elif a.lower() =="n":
            return

    # print(txtname)
    fp = open(path, 'rb')  # 以二进制读模式打开
    # 用文件对象来创建一个pdf文档分析器
    praser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    praser.set_document(doc)
    doc.set_parser(praser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages():  # doc.get_pages() 获取page列表
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()

            """这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括LTTextBox, LTFigure, LTImage, 
            LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性"""
            for x in layout:
                # if type(x) is LTFigure:
                #     x1 = x
                #     print(list(x1))
                #     # with open("1.jpg", "w") as f1:
                #     #    f1.write(str(x1))
                if (isinstance(x, LTTextBoxHorizontal)):

                    with open(txtname, 'a') as f:
                        results = x.get_text()
                        print(results+"\n")
                        f.write(results + '\n')
        print("生成 %s" % txtname)


class PDF:
    def __init__(self):
        print("------------------------------------start---------------------------------------\n")
        print("如果你的文件在当前目录，直接输入文件名。退出请输入exit")
        self.path = input("please post filepath of your file:\n")

    def checkpath(self):
        if os.path.isfile(self.path):
            real = os.path.abspath(self.path)
            real = real.split(".")
            if real[-1].lower() == "pdf":
                print("文件存在", real[-1])
                return True
            else:
                print("文件格式不支持！本程序支持PDF解析")
                return False
        elif self.path == "exit" or self.path.lower() =="exit":
            print("Bye")
            sys.exit()
        else:
            print("输入的路径无效。\n请检查文件路径和文件名")
            print("------------------------------------end-----------------------------------------\n")

    def pdf(self):
        check = self.checkpath()
        if check is True:
            parse(self.path)
        else:
            pass


if __name__ == '__main__':
    print("*******************欢迎你使用由太阳编写的pdf文本解析器************")
    while True:
        pdf = PDF()
        pdf.pdf()
        print("退出请输入exit")
