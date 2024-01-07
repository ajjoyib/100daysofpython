import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

def get_data(url, headers):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        website_html = response.text

        soup = BeautifulSoup(website_html, "lxml")
        # Getting the product name
        name = soup.find("span", id="productTitle").get_text().strip()
        # Getting the price
        price_tag = soup.find("span", id="price").get_text()
        price = float(price_tag.split("$")[1])
        return [name, price]
    except requests.RequestException as e:
        print(f"Error: {e}")


def send_email(sender_email, sender_password, receipent_email, subject, body):
    # Gmail SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receipent_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as connection:
            connection.starttls()
            connection.login(sender_email, sender_password)
            connection.sendmail(send_email, receipent_email, message.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except Exception as e:
        print(f"Error sending email: {e}")


def main():
    URL = "https://www.amazon.com/Walter-Isaacson-Biography-Geniuses-Benjamin/dp/1982130423/?_encoding=UTF8&pd_rd_w=wvttL&content-id=amzn1.sym.9119971c-28e7-426d-b1df-798ac36bb5cd%3Aamzn1.symc.e5c80209-769f-4ade-a325-2eaec14b8e0e&pf_rd_p=9119971c-28e7-426d-b1df-798ac36bb5cd&pf_rd_r=MFBPG2N7Q99HG7WQC370&pd_rd_wg=XgSvy&pd_rd_r=a167295c-f8a3-4fcf-928c-c258b8f68c38&ref_=pd_gw_ci_mcx_mr_hp_atf_m"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Whale/3.24.223.18 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ja;q=0.8",
    }

    sender_email = "hamidullo287@gmail.com"
    sender_password = getpass("Enter your email password: ")
    recipient_email = "memor.first@gmail.com"

    data = get_data(URL, headers)
    print(data)
    if data and data[1] < 75:
        subject = f"Price Drop Alert: {data[0]}"
        body = f"Hello, \nWe hope this message finds you well. We wanted to inform you about an exciting update regarding the product you've been keeping an eye on - {data[0]}.\nWe're pleased to let you know that the price for {data[0]} has dropped below what you saw last time. Now it costs {data[1]}. Use this great opportunity to make your purchase and take advantage of this special offer."
        send_email(sender_email, sender_password, recipient_email, subject, body)


if __name__ == "__main__":
    main()
