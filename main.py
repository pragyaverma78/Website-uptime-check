
import time
import requests


def check_website(url):
    """Check website status and response time."""

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    try:
        start_time = time.perf_counter()

        response = requests.get(url, timeout=10)

        end_time = time.perf_counter()
        response_time = (end_time - start_time) * 1000

        status_code = response.status_code

        if 200 <= status_code < 400:
            status = "ONLINE"
        else:
            status = "ISSUE"

        return {
            "url": url,
            "status": status,
            "status_code": status_code,
            "response_time": round(response_time, 2)
        }

    except requests.RequestException:
        return {
            "url": url,
            "status": "OFFLINE / ERROR",
            "status_code": "N/A",
            "response_time": "N/A"
        }


def main():
    print("=== Website Uptime Checker ===")

    websites = input(
        "Enter website URLs separated by commas: "
    ).split(",")

    print("\nChecking websites...\n")

    for website in websites:
        website = website.strip()

        if not website:
            continue

        result = check_website(website)

        print("-" * 45)
        print(f"Website       : {result['url']}")
        print(f"Status        : {result['status']}")
        print(f"Status Code   : {result['status_code']}")
        print(f"Response Time : {result['response_time']} ms")

    print("-" * 45)
    print("Check completed!")


if __name__ == "__main__":
    main()
