## ProductReviewCrawler
- collecting review from 2 eCommerce website: Tiki and Shoppee. For each type of website:
  
search_product_by_keyword(keyword: str, limit: str = '20'):   
	return a list of product (name, shopid, itemid); limit = maximum products returned
  
find_reviews_by_keyword(keyword: str, limit: int = 20):  
	return a list of reviews corresponding to each product found from the keyword passing
  
find_reviews_by_url(url: str):  
	return a list of reviews corresponding to the product url
  
get_reviews_list():  
	return a list of all reviews for the product determined by id passing:  
     		Shopee: itemid, shopid  
     		Tiki: item id (or itemid, shopid, selling product id)  
  
- Method for the admin:  
  
crawl_by_keyword(keyword: str):  
	insert reviews for product found from the keywordto the database
  
crawl_by_url(url: str):  
	insert reviews for product found from the link (shopee link or tiki link) to the database
  
def update_database():  
	update reviews from the product already in the database
