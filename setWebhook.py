import requests

token = "927033695:AAHfEAmklL4ZkN4c85epUiNNgN1ab-Nl1Zc"
url = f"https://api.telegram.org/bot{token}/setWebhook"

#del_url = f"https://api.telegram.org/bot{token}/deleteWebhook"
#res = requests.get(del_url).text
#ngrok_url = "https://8bf64099.ngrok.io/telegram"
python_url = "https://yeggutti.pythonanywhere.com/telegram"

set_webhook_url = f'{url}?url={python_url}'

res = requests.get(set_webhook_url).text

print(res)