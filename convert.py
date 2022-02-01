import os
from PIL import Image

for filename in os.listdir('D:/furniture shop/Furniture-Ecommerce/public/assets/images/product/bathroom/doors/1'):
    i = 1
    if filename.endswith('.jpg'):
        with Image.open(os.path.join('D:/furniture shop/Furniture-Ecommerce/public/assets/images/product/bathroom/doors/1/', filename)) as f:
            file = 'D:/furniture shop/Furniture-Ecommerce/public/assets/images/product/bathroom/doors/1/'+str(i)+'.jpeg'
            f.save(file)
            i=i+1