import os
os.chdir(r'C:\Users\multicampus\TIL\dummy') #r은 백슬러시를 문자로 인지하기 위해

for f os.listdir('.') :
    os.rename(f, 'SSAFY_'+ f)
    #os.rename(f, f.replace('SSAFY_','SAMSUNG_'))