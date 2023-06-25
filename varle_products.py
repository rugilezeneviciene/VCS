import requests
from bs4 import BeautifulSoup
import psycopg2   #kad mes galetume pasiekti postgresa, suteikia sasaja  tarp kodo ir duomenu bazes

def create_and_insert_product():
    connection = psycopg2.connect(    #reikia susikonektinti su DB
        host="localhost",                              #KURIAME prisijungima
        port=5432,
        database="products",
        user="postgres",
        password="mamamyja"
    )

    #creating management with database
    cursor = connection.cursor()

    create_table_query = """
        # CREATE TABLE IF NOT EXISTS varle_products (
        # id SERIAL PRIMARY KEY,
        # name VARCHAR(255),
        # price DECIMAL(10,2),
        # quantity INT
        # )
        """
    #executinam coursoriu
    #cursor.execute(create_table_query)
    #print("Table created succesfully")
    #reikia nusirodyti URL, define website
    url = "https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/" #screipinimas
    #atsakymas is website
    response = requests.get(url)
    #create bs4 object to parse the html content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    product_elements = soup.find_all('div', class_='ajax-content')
    #print(product_elements)
    #iterate over each product elemenet and extract product info
    for product_element in product_elements:    #reikia for kad galetume pasiimti mums reikalinga informacija
        product_name = product_element.find('div', class_='product-title').text.strip()       #find beutifulSoup bibliotekos sintaxe     text strip - rodo teksta, pasalina nereikalingus tarpus
        product_price = product_element.find('span', class_='price-value').text.strip()[:3]
        product_quantity = product_element.find('b').text.strip()[:1]

#inserting product data into the varle_products table

        #print(product_quantity)
        # %s reiskia kad grazins STRING
        insert_query = "INSERT INTO varle_products (name, price, quantity) VALUES (%s, %s, %s)"
        cursor.execute(insert_query,(product_name, product_price, product_quantity))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    create_and_insert_product()

