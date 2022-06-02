import json
# import sys
# sys.path.append('/.../ProductReviewer/SE_database')
from Shopee import Shopee
from Tiki import Tiki
from SE_database.utils.mongo_setup import global_init
from SE_database.utils.utils import *
global_init()
def crawl_by_keyword(keyword: str):
    shopee = Shopee('https://shopee.vn')
    tiki = Tiki('https://tiki.vn/')
    r1 = shopee.find_reviews_by_keyword(keyword)
    insert_many_products(r1)
    r2 = tiki.find_reviews_by_keyword(keyword)
    insert_many_products(r2)
def crawl_by_url(url: str):
    if 'shopee' in url:
        shopee = Shopee('https://shopee.vn')
        results = shopee.find_reviews_by_url(url)
        print(results)
        # for res in results:
        insert_many_products(results)
    elif 'tiki' in url:
        tiki = Tiki('https://tiki.vn/')
        results = tiki.find_reviews_by_url(url)
        print(results)
        insert_many_products(results)
    else:
        print("Nothing happen!!!")

def update_database():
    query = list(Product.objects.all())
    for p in query:
        test = [{"rating": 4, "comment_text": "ok", "images": [], "videos": []}]
        if p.source == 'shoppee':
            new = Shopee('https://shopee.vn')
            reviews  = new.get_reviews_list(p.shop_id, p.item_id)

            p.reviews = reviews
            insert_many_products([p])
            print('Update ', p.name, p.item_id)
        elif p.source == 'tiki':
            new = Tiki('https://tiki.vn/')
            reviews = new.get_reviews_list(p.item_id, 50)[0]

            p.reviews = reviews
            # print('reviews = ', reviews)
            insert_many_products([p])
            print('Update ', p.name, p.item_id)

shopee_url = 'https://shopee.vn/D%C3%89P-T%C3%94NG-N%C6%A0-K%E1%BA%BA-CARO-i.7332956.19101749350?sp_atk=08cca8a5-dabe-47ae-bcf5-6b8c3dc93d9d&xptdk=08cca8a5-dabe-47ae-bcf5-6b8c3dc93d9d'
tiki_url = 'https://tiki.vn/chuot-khong-day-multi-device-dell-ms5320w-hang-chinh-hang-p57866963.html?spid=117573048'

# delete_all_product()
# crawl_by_url(tiki_url)
# crawl_by_url(shopee_url)
# crawl_by_keyword('heat shrink tube tubing kit tool black shrinkage set safely protect electrical')
update_database()