from dotenv import load_dotenv
import os

load_dotenv()
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")

# DB_PORT_INNER = os.environ.get("DB_PORT_INNER")

DB_ENGINE = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
DB_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
# SECRET_KEY = os.environ.get("SECRET_KEY")
JSERVICE_URL = os.environ.get("JSERVICE_URL")
