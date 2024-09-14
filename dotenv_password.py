import os

from dotenv import load_dotenv

# 加载.env文件
load_dotenv()
database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY')

print(f'Database URL:{database_url}')
print(f'API Key:{api_key}')
