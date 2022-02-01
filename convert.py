import os
from PIL import Image
path = os.getcwd()
print(path)
i = 1
for filename in os.listdir(path):
    print(filename)
    
    if filename.endswith('.jpg'):
        with Image.open(os.path.join(path, filename)) as f:
            file = path+"\\"+str(i)+'.jpeg'
            f.save(file)
            i=i+1