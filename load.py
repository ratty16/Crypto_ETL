import psycopg2

def load_data(data):
    conn = psycopg2.connect(
        host="localhost",
        database="crypto_data",
        user="postgres",
        password="your_password"  # Replace with your PostgreSQL password
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO crypto_prices (currency, price, timestamp) VALUES (%s, %s, %s)", 
                   (data['currency'], data['price'], data['timestamp']))
    conn.commit()
    cursor.close()
    conn.close()
