import datetime
import random
import pymysql

# DB connection details
MYSQL_HOST = "tracktechlk.com"
MYSQL_USER = "tracktec_inuka"
MYSQL_PASSWORD = "Kasuni.2000"
MYSQL_DATABASE = "tracktec_inuka1"

# Establish a connection to DB
db = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)

cursor = db.cursor()
def get_random_time():
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Define a range of five months ago from the current date
    five_months_ago = current_datetime - datetime.timedelta(days=30*5)

    # Get a random number of days within the last five months
    random_days = random.randint(0, (current_datetime - five_months_ago).days)

    # Generate the random timestamp
    random_timestamp = five_months_ago + datetime.timedelta(days=random_days)

    return random_timestamp

def insert_data(table_name, d):
        insert_query = ""

        if table_name == "Product_Chats":
            insert_query = "INSERT INTO Product_Chats (MsgTime, Lang, Product_Type, Product, Intent) VALUES (%s, %s, %s, %s, %s)"
            
        elif table_name == "General_Chats":
            insert_query = "INSERT INTO General_Chats (MsgTime, Lang, Intent) VALUES (%s, %s, %s)"
            

        cursor.execute(insert_query, d)
        db.commit()
        print("Added data: ",d)

def create_entry():
    lang=['Eng',"Sin","Tam"]
    types=['savings','fixed_deposits','services']
    sav_products=['boc_savings_plus','boc_smart_salary_saver','boc_senior_citizens','boc_2_in_1','boc_group_savings','boc_smartgen','boc_ran_kekulu','boc_savings_for_foreign_currency']
    fd_products = ['boc_fixed_deposits','boc_senior_citizens_fixed_deposits','boc_childrens_fixed_deposits']
    specific=['eligibility','benefits','description']

    services = ['greet','thank_you','check_balance','nlu_fallback','check_recipients','transfer_money']

    timestamp = get_random_time()
    lang = random.choice(lang)
    t = random.choice(types)

    if t == 'services':
        intent = random.choice(services)
        data = (timestamp, lang, intent)
        insert_data('General_Chats',data)

    if t == 'savings':
        product = random.choice(sav_products)
        intent = random.choice(specific)
        data = (timestamp, lang, t, product, intent)
        insert_data('Product_Chats',data)

    if t == 'fixed_deposits':
        product = random.choice(fd_products)
        intent = random.choice(specific)
        data = (timestamp, lang, t, product, intent)
        insert_data('Product_Chats',data)

for i in range(1000):
     create_entry()