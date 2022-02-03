import requests
import re
from bs4 import BeautifulSoup


def generate_links(base_link):
    links = []
    bl_start = base_link[:54]
    bl_end = base_link[55:]

    #print(bl_start)
    #print(bl_end)

    for i in range(0,2):
        #print(f'{bl_start}{i}{bl_end}')
        links.append(f'{bl_start}{i}{bl_end}')
    return links

def get_html(link):
    result = requests.get(link)
    soup = BeautifulSoup(result.text, "html.parser")
    
    
    return soup
    
    


if __name__ == '__main__':
    base_link = 'https://www.avito.ru/sankt-peterburg/transport?cd=1&p=1&q=tohatsu+18'
    links = generate_links(base_link)
   
    for link in links:
        soup =  get_html(link)
        blocks = soup.findAll('div', class_='iva-item-root-_lk9K photo-slider-slider-S15A_ iva-item-list-rfgcH iva-item-redesign-rop6P iva-item-responsive-_lbhG iva-item-ratingsRedesign-ydZfp items-item-My3ih items-listItem-Gd1jN js-catalog-item-enum')
        #print(blocks)
        print(type(blocks))
        for block in blocks:
            #print(block)
            print('---------------------------------------------------------------------------------------------------------')
            ob_name = re.search(r'title="(.*?)><div class="photo-slider',str(block))
            ob_cena = re.findall(r'<meta content="(.*?)" itemprop="price"',str(block))
            
            print(ob_name.group(1))
            print(ob_cena)
        
        
        
        
    
    