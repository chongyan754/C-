import json
import math

with open("文件路径.json",'r',encoding='utf-8') as shu:
    shu=json.load(shu)
with open("节点大小.json",'r',encoding='utf-8') as zi:
    zi=json.load(zi)


iop=0
fu="C:"
xuan=shu[fu]

def dayin():
    print(str(iop)+"号目标 "+xuan[iop]+"     "+str(math.floor(zi[xuan[iop]]/1048576))+"MB,占用约"+str(math.floor(zi[xuan[iop]]/zi[fu]*100))+"%")


try:
    print("父节点"+fu)
    while True:
        dayin()
        iop=iop+1
except:
    print("输入“/”返回C盘根目录，输入数字查看后续路径。如果输入非数字则会退出")
    while True:
        a=input("输入选择\n")
        print("父节点"+fu)
        iop=0
        if a=="/":
            fu="C:"
            xuan=shu[fu]
            try:
                while True:
                    dayin()
                    iop=iop+1
            except:
                pass
        else:

            fu=xuan[int(a)]
            xuan=shu[fu]
            try:
                while True:
                    dayin()
                    iop=iop+1
            except:
                pass




