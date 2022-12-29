import mysql.connector
import praw
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

DB_PWD = os.getenv('DB_PWD')
DB_NAME = os.getenv('DB_NAME')

REDDIT_ID = os.getenv('REDDIT_ID')
REDDIT_SECRET = os.getenv('REDDIT_SECRET')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PWD = os.getenv('REDDIT_PWD')
REDDIT_USER_AGENT = os.getenv('REDDIT_USER_AGENT')

db = mysql.connector.connect(
    host='localhost', user="root", passwd=DB_PWD, database=DB_NAME, auth_plugin="mysql_native_password"
)

reddit = praw.Reddit(client_id=REDDIT_ID, client_secret=REDDIT_SECRET,
                     username=REDDIT_USERNAME, password=REDDIT_PWD, user_agent=REDDIT_USER_AGENT, check_for_async=False)
