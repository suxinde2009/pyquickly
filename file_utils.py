import os


def ListFilesInDir(dirPath):
    return os.listdir(dirPath)


def CreateDirIfNeeded(dirPath):
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)


def DeleteFilesInDir(dirPath):
     for file_name in os.listdir(dirPath): 
        file_path = os.path.join(dirPath, file_name)
        os.remove(file_path)


def RemoveFileInDirWithFileType(dirPath, file_ext_name):
    
    for file_name in os.listdir(dirPath):
        # 如果文件名以指定后缀结尾
        if file_name.endswith(file_ext_name):
            # 拼接文件的完整路径
            file_path = os.path.join(dirPath, file_name)
            # 删除文件
            os.remove(file_path)


def RemoveFilesInDirWitoCondition(dirPath, func):

    for file_name in os.listdir(dirPath):
        # 如果文件名以指定后缀结尾
        if func(x) == True:
            # 拼接文件的完整路径
            file_path = os.path.join(dirPath, file_name)
            # 删除文件
            os.remove(file_path)