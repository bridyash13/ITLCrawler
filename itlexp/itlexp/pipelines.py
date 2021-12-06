# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import mysql.connector

class ItlexpPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'Ganesh@6jan',
            database = "medals"
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS medals""")
        self.curr.execute("""CREATE TABLE medals(
            Country text,
            Gold text,
            Silver text,
            Bronze text,
            Total text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO medals VALUES (%s,%s,%s,%s,%s)""", (
            item['Country'],
            item['Gold'],
            item['Silver'],
            item['Bronze'],
            item['Total'],
        ))
        self.conn.commit()
