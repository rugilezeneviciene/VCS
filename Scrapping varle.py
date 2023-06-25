import requests
from bs4 import BeautifulSoup
import psycopg2


def create_and_insert_product():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="products",
        user="postgres",
        password="mamamyja"
    )

    # creating management with database
    cursor = connection.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS varle_products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(500),
        price DECIMAL(10, 2),
        quantity INT
        )
    """

    # execute SQL statement
    # cursor.execute(create_table_query)
    # print("Table created successfully!")

    # define website
    url = "https://www.varle.lt/nesiojami-kompiuteriai/nesiojami-kompiuteriai/"

    # response from the website
    response = requests.get(url)
    # create a bs4 object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # find all product elements in the category
    product_elements = soup.find_all('div', class_='GRID_ITEM')

    # iterate over each product element and extract product information
    for product_element in product_elements:
        product_name = product_element.find('div', class_='product-title').text.strip()
        product_price = product_element.find('span', class_='price-value').text.strip()[:3]
        product_quantity = product_element.find('b').text.strip()[:1]

        # inserting product data into the 'varle_products' table
        insert_query = "INSERT INTO varle_products (name, price, quantity) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (product_name, product_price, product_quantity))

        print(f"Adding products to the database: {product_name}")
        print("Products inserted into database successfully!")

    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    create_and_insert_product()