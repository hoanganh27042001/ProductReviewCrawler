API documentation
Overviews
APIs for collecting and summarizing customers’ reviews from other E-commercial sites including Tiki, Shopee, …

Our API platform can provide the following functionalities for our partners:
signup a new admin user
authorize the admin user
retrieving products’ reviews by keywords, urls
delete products in the database
get the summary of all the products
Data format in database
Product
name: str  -> name of the product
item_id: str
shop_id: str
source: str -> shopee or tiki
query_times: int -> how many times the product is queried from the Database
reviews: List[Rating] -> list of rating
avg_rating: float
date: Datetime -> 
Rating:
rating: int
comment: str
images: List
videos: List

Functionalities
API for all users  (no need to log in)
retrieving products’ reviews by keywords, urls 
Send HTTP POST request to:  http://ecom404.herokuapp.com/rating

Request parameters:

Parameters
Type
Required
Valid value
Description
input_data
String
True


specify the product’s name if by keyword and product’s url if by url
by
String
True
“keyword” or “url”
query method
limit
int
True
> 0 
maximum number of products return


Response parameters:

Parameters
Description
message
Inform the success of the query and number of products returned
status_code
status code of the HTTPs request to the Database (200 = success)
data
List of the returned product

 
Request example (Python):

import requests
products = requests.post(r"http://ecom404.herokuapp.com/rating", json = {
    "input_data": "máy in",
    "by": "keyword",
    "limit": 5
})
print(products.json())


Login

Send HTTP POST request to:  http://ecom404.herokuapp.com/auth/login

Request parameters:

Parameters
Type
Required
Description
username
String
True
username 
password
String
True
password


Response parameters:

Parameters
Type
Description
access_token
String
access token used for admin APIs
token_type
String
token type used for admin APIs

 
Note that in order to login, you need to have your account already stored in the Database

Request example (Python):

import requests
login = requests.post(r'http://ecom404.herokuapp.com/auth/login',
                      data = {
                          "username": "chau",
                          "password": "1"
                      })
print(login.json())

API for admin users
Create user 
Send HTTP POST request to:  http://ecom404.herokuapp.com/auth/create-user

Request parameters:

Parameters
Type
Required
Valid value
Description
headers
Dictionary
True
{“Authentication:”: <token_type> <access_token>}
Authentication header
username
String
True




password
String
True






Response parameters:

{"code":"1000","message":"OK"} if user have not existed in the user database
{"detail":"User already exists"} otherwise

Request example (Python):
login = requests.post(r'http://ecom404.herokuapp.com/auth/login',
                      data = {
                          "username": "chau",
                          "password": "1"
                      })
responses = login.json()
# get access token
token = responses['access_token']
token_type = responses['token_type']
# create user
create = requests.post(r"http://ecom404.herokuapp.com/auth/create-user",
                       headers = {'Authorization': " ".join([token_type, token])},
                       json = {"username": "chau1921903", "password": "1"})
print(create.content.decode('utf-8'))

Crawl:
Send HTTP POST request to:  http://ecom404.herokuapp.com/operation/crawl

Request parameters:

Parameters
Type
Required
Valid value
Description
headers
Dictionary
True
{“Authentication:”: <token_type> <access_token>}
Authentication header url
input_data
String
True


specify the product’s name if by keyword and product’s url if by url
by
String
True
“keyword” or “url”
crawl method
limit
int
True
> 0 
maximum number of products to crawl


Response:

{
  "status": "success",
  "num_product_success": 4,
  "duplicate_db": 0
}

Request example (Python):

import requests
products = requests.post(r"http://ecom404.herokuapp.com/operation/crawl",
             headers = {'Authorization': " ".join([token_type, token])},
 		json = {
    "input_data": "máy in",
    "by": "keyword",
    "limit": 5
})
print(products.json())

Delete products
send HTTP POST request to:  http://ecom404.herokuapp.com/operation/operation/delete_by_ids

Request parameters:

Parameters
Type
Required
Valid value
Description
headers
Dictionary
True
{“Authentication:”: <token_type> <access_token>}
Authentication header url
source
String
True


specify the source of the product (tiki or shopee)
item_id
String
True


id of the product
shop_id
String
True
 
id of the shop


Response sample:
"Nothing happen!!!"
"Number of products before deletion: … Number of products after deletion: …”
Request example (Python):

import requests
delete = requests.post(r"http://ecom404.herokuapp.com/operator/delete_by_ids", headers = {'Authorization': " ".join([token_type, token])},
json = {
  "source": "shopee",
  "item_id": "12345",
  "shop_id": "54321"
}
)
 
print(products.json())

Get summary
send HTTP POST request to:  http://ecom404.herokuapp.com/operation/summary

Request parameters:

Name
Type
Required
Valid value
Description
headers
String
True
{“Authentication:”: <token_type> <access_token>}
Authentication header url

Response ís a list of all products in database

Request example (Python):
import requests
summary = requests.post(r"http://ecom404.herokuapp.com/operation/summary",
              headers = {'Authorization': " ".join([token_type, token])})
 
print(summary.content.decode('utf-8'))
 


