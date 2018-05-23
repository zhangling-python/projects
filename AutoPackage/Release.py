#coding=utf-8;
import os
import time
import pickle
from urllib import request
import requests

USER_KEY = "87de0418e40150c996b3523f95d31f63"
API_KEY = "5dc590cf31e2bdb99ff655d20a3a4dec"
global ipa_temp_path

def readConfiguration():	
        global PROJECT_PATH
        global PROJECT_NAME
        global TARGET_NAME
        global TARGET_FOLDERPATH
        global HAS_WORKSPACE

        userConfiguation = open('user_Configuration.pkl','rb')
        userList = pickle.load(userConfiguation)
        print(userList)

        PROJECT_PATH = userList["projectPath"]
        PROJECT_NAME = userList["projectName"]
        TARGET_NAME = userList["targetName"]
        TARGET_FOLDERPATH = userList["targetPath"]
        HAS_WORKSPACE = userList["hasWorkspace"]

def chooseOption():
        global RELEASE_TYPE

        theType = input('choose build type:\n----------debug ----------> 0\n----------release ----------> 1\n:')

        if theType == '0':
              RELEASE_TYPE = 'Debug'
        elif theType == '1':
              RELEASE_TYPE = 'Release'
        else:
              RELEASE_TYPE = 'Release'

        return waitConfirm()

def waitConfirm():
	isConfirmed = input('you have choose build type : %s , confirm to release?(y/n) : ' %(RELEASE_TYPE))
	if isConfirmed == 'Y' or isConfirmed == 'y':
		return True
	elif isConfirmed == 'N' or isConfirmed == 'n':
		return chooseOption()
	else:
		return waitConfirm()

def createFolder(targetName):
	d = time.ctime().split(' ')
	curTime = d[3]
	dirStr = '%s/%s%s' %(TARGET_FOLDERPATH,targetName,curTime)
	os.system('mkdir %s' %(dirStr))
	return dirStr

def createTempFolder():
	dirStr = '%s/temp' %(TARGET_FOLDERPATH)
	os.system('mkdir %s' %(dirStr))
	return dirStr

def release():
    cdStr = 'cd %s' %(PROJECT_PATH)
    os.system(cdStr + '\n')
    cleanStr = 'xcodebuild -project "%s/%s.xcodeproj" -target "%s" -configuration "%s" clean' %(PROJECT_PATH,PROJECT_NAME,TARGET_NAME,RELEASE_TYPE)
    os.system(cleanStr)
    tempDirPath = createTempFolder()
    if HAS_WORKSPACE:
        buildStr = 'xcodebuild -workspace %s/%s.xcworkspace -sdk iphoneos  -scheme "%s" -configuration "%s" CONFIGURATION_BUILD_DIR="%s"' %(PROJECT_PATH,PROJECT_NAME,TARGET_NAME,RELEASE_TYPE,tempDirPath)
    else:
        buildStr = 'xcodebuild -project %s/%s.xcodeproj -sdk iphoneos  -scheme "%s" -configuration "%s" CONFIGURATION_BUILD_DIR="%s"' %(PROJECT_PATH,PROJECT_NAME,TARGET_NAME,RELEASE_TYPE,tempDirPath)
    os.system(buildStr)
    folderStr = createFolder(TARGET_NAME)
    releaseStr = 'xcrun -sdk iphoneos packageApplication -v  %s/%s.app -o %s/%s.ipa' %(tempDirPath,TARGET_NAME,folderStr,TARGET_NAME)
    global ipa_temp_path
    ipa_temp_path = '%s/%s.ipa' %(folderStr,TARGET_NAME)
    os.system(releaseStr)
    os.system('rm -rf %s' %(tempDirPath))

#上传蒲公英
def uploadIPA(IPAPath):
    if(IPAPath==''):
        print(" *************** 没有找到对应上传的IPA包 ********************* ")
        return
    else:
        print(" ***************开始上传到蒲公英********************* ")
        url='http://www.pgyer.com/apiv1/app/upload'
        data={
            'uKey':USER_KEY,
            '_api_key':API_KEY,
            'installType':'2',
            'password':'Ccydsz@2017',
            'updateDescription':"测试自动化打包"
        }
        files={'file':open(IPAPath,'rb')}
        r=requests.post(url,data=data,files=files)

readConfiguration()
if chooseOption() == True  :
    release()

print(ipa_temp_path)
uploadIPA(ipa_temp_path)
