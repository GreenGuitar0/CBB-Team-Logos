import csv
import urllib.request
import mimetypes
import requests
import urllib.parse

def download_svgs():
    with open('TeamData.csv') as data:
        reader = csv.reader(data)

        for row in reader: 
            urllib.request.urlretrieve(row[7], "svgs/" + row[0] + ".svg")
            print("Downloaded", row[0])

def is_url_image(url):
    """
    Check if the URL is likely to point to an image by inspecting the file extension.
    """
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
    return url.lower().endswith(image_extensions)

def check_url(url):
    """
    Send a HEAD request to check if the URL exists.
    """
    try:
        response = requests.head(url)
        # Check if the response status is 200 (OK)
        return response.status_code == 200
    except requests.RequestException as e:
        # Handle exceptions (e.g., connection errors)
        print(f"An error occurred: {e}")
        return False


def download_pngs():
    with open('final_team_data.csv') as data:
        reader = csv.reader(data)
        filters = [
            "Kansas City",
            "St. Tomas",
            "Massachusetts Lowell",
            "lemoyne-alternate",
            "LIU",
            "Purdue Fort Wayne",
            "Houston Baptist"
        ]
        for row in reader:
            if row[0] in filters:
                url = "https://b.fssta.com/uploads/application/college/team-logos/" + row[0].replace(' ', '') + ".vresize.144.144.medium.0.png"
                if is_url_image(url) and check_url(url):
                    urllib.request.urlretrieve(url, "pngs/" + row[0] + ".png")
                else:
                    print(row[0])

download_svgs()