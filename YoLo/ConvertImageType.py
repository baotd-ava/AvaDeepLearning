"""
Cach chay: python changeFormat.py ten_duong_dan_chua_anh_bmp ten_duong_dan_luu_anh_jpg
#Chuong trinh nay dung de doi format anh
"""

""" Khai bao thu vien can thiet"""
import shutil
import cv2
import os
import glob
import sys


""" Duyet qua tat cac cac file trong thu muc """
def dirwalk(dir, bag, wildcards):
    if glob.glob(os.path.join(dir,"*")):
        bag.extend(glob.glob(os.path.join(dir,wildcards)))
        dirwalk(os.path.join(dir,"*"),bag, wildcards)
        
"""Ham doi ten File """   
def reName(oldName, newExt,savedDir):

    newName = oldName[0:oldName.rfind(".") + 1] + newExt
    img = cv2.imread(oldName)
    cv2.imwrite(newName,img)
# Di chuyen file sang thu muc can luu
    #shutil.move(newName,savedDir)




"""Ham Duyet qua tat ca cac file can doi ten va doi ten"""
def WalkAndRename(dir,newDir, oldExt, newExt):
    files = []
    dirwalk(dir, files, "*" + oldExt)
    for f in files:
            reName(f, newExt,newDir)



"""Chuong trinh chinh 
   Chuong trinh nay doi format bmp sang jpg
   neu muon doi format khac thi chinh sua o dong 48,49
"""
if __name__ == "__main__":
   #day la cac kieu luu file khac nhau, cos the tuy chinh o day
    #path = input("file Directory: ")
    #savePath = input("saved Directory:")
    #oldExt = input("old extension: ")    # ten file cu 
    #newExt = input("new extension: ")    # ten file moi
    #path = sys.argv[1]
    #savePath = sys.argv[2] 
    

    # day la kieu luu file cung thu muc voi file changeFormat.py
    path = os.path.dirname(os.path.abspath(__file__))+"\\"
    savePath = os.path.dirname(os.path.abspath(__file__))+"\\"
    # dong code nay dung de doi file anh dinh dang bmp sang jpg
    # co the thay doi cac dinh dang khac nhau(bmp-->jpg,png,... or jpg-->bmp,png...)
    fromType = "bmp"
    toType = "jpg"
    WalkAndRename(path,savePath, fromType, toType)
    print("image is saved at:",savePath)
