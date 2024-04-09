import wikipediaapi
import sqlite3

user_agent = "TextGeneration/1.0 (simorifai181@gmail.com)"

# Connect to Sqlite
conn = sqlite3.connect('wikipedia.db')
c = conn.cursor()

# Create Table 
c.execute('''CREATE TABLE IF NOT EXISTS articles (id INTEGER PRIMARY KEY, title TEXT, content TEXT)''')

# Insert Data into Table
wiki = wikipediaapi.Wikipedia('en', user_agent=user_agent)
category = wiki.page("Categories:IT")

for article in category.categorymembers.values():
    c.execute("INSERT INTO articles (title, content) VALUES (?, ?)", (article.title, article.text))

# Commit changes and close the connection
conn.commit()
conn.close()
