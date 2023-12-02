import pandas as pd
import requests


def is_website_active(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False


file_path = "C:\\Users\\ddmat\\Downloads\\sms_list.csv"

df = pd.read_csv(file_path)
df["Aktivan"] = "Ne"
df["Website"] = df["Website"].apply(
    lambda x: "https://" + x if isinstance(x, str) and not x.startswith("https://") else x)
df['Aktivan'] = df['Website'].apply(lambda x: 'Da' if is_website_active(x) else 'Ne')

df.to_csv("sms_aktivni.csv")
