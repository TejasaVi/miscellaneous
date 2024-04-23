import requests
from requests import Session

# Session to hold cookies
s = Session()
# Emulate browser
s.headers.update({"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"})

# Get the cookies from the main page (will update automatically in headers)
s.get("https://www.nseindia.com/")

url = "https://www.nseindia.com/api/reports?archives=%5B%7B%22name%22%3A%22F%26O%20-%20FII%20Derivatives%20Statistics%22%2C%22type%22%3A%22archives%22%2C%22category%22%3A%22derivatives%22%2C%22section%22%3A%22equity%22%7D%5D&date=19-Apr-2024&type=equity&mode=single"

# Headers
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Cookie": "your_cookie_here",
    "Pragma": "no-cache",
    "Referer": "https://www.nseindia.com/all-reports-derivatives",
    "Sec-Ch-Ua": '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "X-Requested-With": "XMLHttpRequest"
}

# Make the request
response = s.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Specify the file path where you want to save the downloaded file
    file_path = "downloaded_file.xls"  # Change the extension according to the file type

    # Write the content of the response to the file
    with open(file_path, "wb") as file:
        file.write(response.content)

    print("File downloaded successfully!")
else:
    print(f"Failed to download file. Status code: {response.status_code}")

