# Python 爬虫
-------------------------------------------------------------
## 开发环境
  - **Windows 7 64位**
  - **python 3.6**
  - **Visual Studio 2017**


## 准备工具

- **requests**: 用于请求网络
- **beautifulsoup**: 用于操作 html 数据
- **wkhtmltopdf**: 用来把获取到的网络的 html 文件转换为 PDF 文件； 其中所使用的 pdfkit 是 wkhtmltopdf 的Python封装包


所以，需要先安装好下面的依赖包：


    pip install requests
    pip install beautifulsoup4
    pip install pdfkit

然后需要在[wkhtmltopdf](http://wkhtmltopdf.org/downloads.html)官网下载稳定版进行安装，安装完成之后把该程序的执行路径加入到系统环境 $PATH 变量中（若在安装的时候将选择信息的两个选项打钩，安装过程中会自动将路径添加到环境变量）。

## 运行
1. 以命令行的形式：

		python RunoobToPdf.py

2. 或者在IED环境中直接点击图标 ![](https://i.imgur.com/ssy87tr.png) 运行

## 说明


1. 该程序是爬取[RUNOOB.COM](http://www.runoob.com/python3/python3-tutorial.html)网站上的Python3教程并转换成 PDF 文档，若需爬取该网站其他信息或者其他网站，只需要做部分修改即可。

2. 在该仓库中，附带有作者爬取到的RUNOOB.COM中的 **Python3教程** 。

3. 另外，还附带有[廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000)中的Python3教程，可以做学习使用。




## 效果图
该程序是在号称宇宙最强的IED **Visual Studio 2017** 环境下编写的，其编辑界面如图：

![](https://i.imgur.com/82l1jWe.png)

爬虫运行完成之后，生成的 **PDF** 文件界面如图：

![](https://i.imgur.com/N3cFMxN.png)


## Other

>Author：Regan_Chai
>
>E-Mail： regan_chai@163.com


