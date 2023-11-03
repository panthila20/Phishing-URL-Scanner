import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = 'AIzaSyAdvo2nRZI4wIGH31a4R2g5gxLDN1xxn_M'  # Replace with your actual Google Safe Browsing API key

def is_phishing(url):
    api_url = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"
    payload = {
        "client": {
            "clientId": "your-client-id",
            "clientVersion": "1.0",
        },
        "threatInfo": {
            "threatTypes": ["THREAT_TYPE_UNSPECIFIED", "MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}],
        }
    }

    response = requests.post(api_url, json=payload)
    if response.status_code == 200:
        response_data = response.json()
        if "matches" in response_data:
            return True

    return False

def check_phishing():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "URL is required.")
        return

    if is_phishing(url):
        messagebox.showinfo("Phishing Check Result", f"The provided URL ({url}) is flagged as a potential phishing site.")
    else:
        messagebox.showinfo("Phishing Check Result", f"The provided URL ({url}) is not identified as a phishing site.")

app = tk.Tk()
app.title("URL Phishing Checker")

# Custom Font
custom_font = ("Helvetica", 12)

# Custom Colors
bg_color = "#E6E6E6"
label_color = "#333333"

app.configure(bg=bg_color)

url_label = tk.Label(app, text="Enter a URL to check for phishing:", font=custom_font, bg=bg_color, fg=label_color)
url_label.pack()

url_entry = tk.Entry(app, width=50, font=custom_font)
url_entry.pack()

check_button = tk.Button(app, text="Check for Phishing", command=check_phishing, font=custom_font)
check_button.pack()

app.mainloop()
