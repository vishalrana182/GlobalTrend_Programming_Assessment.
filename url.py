import requests
from time import sleep


def download_content(urls):
    content_list = []

    for url in urls:
        attempts = 0
        success = False

        while attempts < 3 and not success:
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                content_list.append(response.content)
                success = True
            except requests.exceptions.Timeout:
                print(f"Timeout error on attempt {attempts + 1} for URL: {url}")
            except requests.exceptions.ConnectionError:
                print(f"Connection error on attempt {attempts + 1} for URL: {url}")
            except requests.exceptions.HTTPError as e:
                print(f"HTTP error on attempt {attempts + 1} for URL: {url} - {e}")
                break  # No point in retrying for client or server errors
            except requests.exceptions.RequestException as e:
                print(f"Error on attempt {attempts + 1} for URL: {url} - {e}")
                break  # Any other type of error, break the loop

            attempts += 1
            if not success:
                sleep(1)  # Wait a bit before retrying

        if not success:
            content_list.append(None)

    return content_list



urls = [
    "https://unsplash.com/photos/PDX_a_82obo/download?ixid=M3wxMjA3fDB8MXxzZWFyY2h8M3x8cmFuZG9tJTIwb2JqZWN0c3xlbnwwfHx8fDE3MjA4Njg2MTV8MA&force=true",
    "https://www.pexels.com/download/video/7296318/",
    "https://thispagedoesnotexist.com",
]

contents = download_content(urls)
for i, content in enumerate(contents):
    if content:
        print(f"Content of URL {urls[i]} downloaded successfully.")
    else:
        print(f"Failed to download content of URL {urls[i]} after 3 attempts.")
