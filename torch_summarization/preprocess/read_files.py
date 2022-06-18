#阅读一些常见格式的文件：目前仅支持直接全部加载进内存的方式，一个函数只能读一个文件

def read_textfile_by_line(text_file_path:str):

    return 

def read_paper_pdf(pdf_file_path:str,abstract_begin_flag:str="Abstract",
                    abstract_end_flag:str="1 Introduction"):
    """
    抽取PDF格式论文中的摘要部分作为摘要，其他后文作为原文
    一篇论文返回一个tuple格式的原文-摘要对
    常见的abstract_begin_flag：Abstract
    常见的abstract_end_flag：1 Introduction, Introduction, Index Terms
    """
    from PyPDF2 import PdfReader
    pdf_text=""
    pdfReader=PdfReader(pdf_file_path)
    count=len(pdfReader.pages)  #PDF页数
    for i in range(count):
        page=pdfReader.pages[i]
        output=page.extract_text()
        pdf_text+=' '
        pdf_text+=output  #每页直接用PdfReader输出的文本格式，未经处理，用空格简单地加在一起
    
    begin_index=pdf_text.find(abstract_begin_flag)
    end_index=pdf_text.find(abstract_end_flag)
    target=pdf_text[begin_index:end_index]
    source=pdf_text[end_index:]
    return (source,target)

#测试read_paper_pdf函数的效果
#pdf_file="1_ImageNet Classification with deep convolutional neural networks.pdf"
#pair=read_paper_pdf(pdf_file)
#print(pair[0])
#print()
#print(pair[1])