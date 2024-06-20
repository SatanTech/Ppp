import requests

URL = 'https://bot-telegram-henna.vercel.app/hook'
TOKEN = '7395813848:AAGDJ1NLy7WiXqR642K3fwsCd8WZVroPgV0'
requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={URL}')
