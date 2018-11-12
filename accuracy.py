#coding=UTF-8
#str = "201389 0.005646 246.713013 118.583260 412.077148 370.948975"
#list1 = str.split()
#print(list1[1])
'''
str = "comp4_det_test_118"
list2 = str.split('_')[3];
print(list2)
'''


import os
import  time
path = "D:/results" #测试结果txt文件夹路径
dirs = os.listdir(path)
path1 = "D:/test_1110/" #测试图片文件夹路径
count = 0 #true_positive
num = 0
pic_num = 0
positive = 0  #true_positive + false_positive
false_nav = 0

dirs1 = os.listdir(path1)
for pic_dir in dirs1:
    pic1 = os.listdir(path1+pic_dir)
    for i in pic1:
        pic_num+=1
#print(pic_num)



#time.sleep(100)
for files in dirs:
    filename = os.path.splitext(files)[0]  # 读取文件名
    #print(filename)
    class_name = filename.split('_')[3] #类名
    path_mid = path1+class_name;    #找到类对应的图片文件夹
    txt_content = open(path+"/"+files, 'r+', encoding='UTF-8')
    f= txt_content.readline()
    while (f) :
        #time.sleep(0.1)
        num+=1
        #if num%100 ==0:
            #print("1:%s / %s" %(count,num))
            #print("2:%s / %s" % (count,(count+false_pos) ))
        list = f.split();
        image_name = list[0] #txt中图片名字
        #print("图片名： "+image_name)
        accuracy = list[1]
        if float(accuracy) >= 0.5:
            positive+=1
        #print("准确率： "+accuracy)
        if os.path.exists(path_mid):
            class_imgname = os.listdir(path_mid)
            for imagename in class_imgname:
                img_name1 = os.path.splitext(imagename)[0]#文件夹下每个图片名字
                if (img_name1 == image_name) and (float(accuracy) >= 0.25):
                    count+=1
                    #false_pos+=1
                    #print("count++")
                    break

                if (img_name1 == image_name) and (float(accuracy) <= 0.25):
                    false_nav+=1

        f=txt_content.readline()


print(num) #所有框（有重框现象，就是一个图片框了几个框）
print(count/pic_num) #框对的图片/所有图片数
print(count/positive)  #precision
print(count/(count+false_nav))   #recall















