from bs4 import BeautifulSoup
import requests
import smtplib

PRICE_BAR = 1000
USERNAME = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"
to_person = "SENDERS_EMAIL"

URL = "https://www.flipkart.com/introduction-algorithms-3rd/p/itmdwxyrafdburzg" \
      "?pid=9788120340077&lid=LSTBOK9788120340077E5D3W7&marketplace=FLIPKART&srno=s_1_3&" \
      "otracker=search&otracker1=search&fm=SEARCH&" \
      "iid=c18c5076-d734-4688-bcac-7b9056368ce7.9788120340077.SEARCH&ppt=sp&" \
      "ppn=sp&ssid=lx684the3h2hecjk1606924834434&qH=a59004ae485fd79e"

response = requests.get(URL)
website = response.text

soup = BeautifulSoup(website, "html.parser")
price_tag = soup.find(name="div", class_="_30jeq3 _16Jk6d").get_text()
price_value_string = price_tag.split("₹")[1]
current_price_value = "".join(price_value_string.split(","))
if float(current_price_value) < float(PRICE_BAR):
    with smtplib.SMTP("smtp.gmail.com", port=587) as mail_client:
        mail_client.starttls()
        mail_client.login(user=USERNAME, password=PASSWORD)
        mail_client.sendmail(to_addrs=to_person,
                             from_addr=USERNAME,
                             msg=f"Subject:Price Drop Alert !\n\n"
                                 f"Current Price is ${current_price_value}\n"
                                 f"Buy Soon !!! ")
