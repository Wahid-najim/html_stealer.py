import os 
url=input('put your website link here:')
os.system('wget "'+url+'"')
print('html saved')
