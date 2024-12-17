import os
import json


gui_shu={}
jie_dian_dax={}
pai_chu=open("排除路径","r")
pai_chu=pai_chu.readlines()

def di_gui(a,b):
    if b not in pai_chu:
        uio=0
        while True:
            lei_x="文件"
            try:
                asd=os.listdir(a[uio])
                lei_x="列表"
                #print(asd)
                qwe=0
                try:
                    while True:
                        asd[qwe]=a[uio]+"/"+asd[qwe]
                        qwe=qwe+1
                except:
                    gui_shu[a[uio]]=asd
                if len([asd])>0:
                    jie_dian_dax[a[uio]]=0
                    di_gui(asd,a[uio])
            except Exception as e:
                #print(e)
                if lei_x=="文件":
                    jie_dian_dax[a[uio]]=os.stat(a[uio]).st_size
                    jie_dian_dax[b]=jie_dian_dax[b]+os.stat(a[uio]).st_size
                if lei_x=="列表":
                    jie_dian_dax[b]=jie_dian_dax[b]+jie_dian_dax[a[uio]]


            uio=uio+1
            #print(a[uio]+lei_x)
            if uio>len(a)-1:
                y=1/0




chu_lu="C:"

gui_shu[chu_lu]=os.listdir(chu_lu)
jie_dian_dax[chu_lu]=0
a=0
try:
    while True:
        gui_shu[chu_lu][a]=chu_lu+"/"+gui_shu[chu_lu][a]
        a=a+1
except:
    try:
        di_gui(gui_shu[chu_lu],chu_lu)
    except Exception as w:
        print(w)
        with open('文件路径.json','w',encoding='utf-8') as f:
            json.dump(gui_shu,f,ensure_ascii=False,indent=4)
        with open('节点大小.json','w',encoding='utf-8') as f:
            json.dump(jie_dian_dax,f,ensure_ascii=False,indent=4)

