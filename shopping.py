from bs4 import BeautifulSoup
import requests
import warnings
import tkinter as tk
from PIL import ImageTk, Image
import os
from io import BytesIO

url = "https://www.snapdeal.com/products/mobiles-mobile-phones/filters/Form_s~Smartphones"
warnings.filterwarnings("ignore")


page_response = requests.get(url,verify = False, timeout=5)

page_content = BeautifulSoup(page_response.content,"html.parser")

product_price = page_content.find_all('span',class_='lfloat product-price')

product_name = page_content.find_all('p',class_='product-title')

product_discount = page_content.find_all('div',class_='product-discount')

test = page_content.find_all('img',class_='product-image')


    

for i in range(len(product_name)):
    s = product_name[i].text
    s = s.lstrip()
    s = s.rstrip()
    print('PRODUCT '+str(i+1)+' :')
    print('PRODUCT NAME : ' + s)

    dis = product_price[i].text
    dis = dis.lstrip()
    dis = dis.rstrip()
    print('PRODUCT PRICE : ' + dis)

    n = product_discount[i].text
    n = n.lstrip()
    n = n.rstrip()
    print('PRODUCT DISCOUNT : '+ n)
    try:
        url = test[i]['src']
    except:
        url = test[i]['data-src']
    root = tk.Tk()
    response = requests.get(url)
    img_data = response.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    panel = tk.Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.mainloop()
    print('')


