from bs4 import BeautifulSoup
import requests
import pandas as pd
import mysql.connector

URL = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

HEADERS ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
webpage = requests.get(URL, headers=HEADERS)
type(webpage.content)
soup = BeautifulSoup(webpage.content, "html.parser")
table = soup.find_all('table')[2]
print(table)
world_titles = table.find_all('th')
world_titles
world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)
import pandas as pd
df = pd.DataFrame(columns = world_table_titles)

df

column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data
df


df.to_csv(r'C:\Users\Lenovo\Desktop\music.csv\finkk.csv',index=False)





import mysql.connector
import pandas as pd

# Define your MySQL database connection details
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "T#9758@qlph",
    "database": "vicky",
}


connection = mysql.connector.connect(**db_config)


cursor = connection.cursor()


csv_file_path = 'C:/Users/Lenovo/Desktop/music.csv/finkk.csv'


df = pd.read_csv(csv_file_path)


table_name = 'companyda'


for _, row in df.iterrows():
    values = tuple(row)
    insert_query = f"INSERT INTO {'companyda'} VALUES ({', '.join(['%s'] * len(row))})"
    cursor.execute(insert_query, values)


connection.commit()
connection.close()

print("Data inserted into MySQL successfully!")






