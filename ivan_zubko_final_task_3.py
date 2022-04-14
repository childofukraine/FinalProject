import requests

currency_from = input("Enter your currency:").split(" ")
try:
    key = "8c7bbe5e8d1ff573a2eca963f9e861961478f1cb"
    parameters = {"api_key": key, "from": currency_from[0], "to": "UAH", "amount": 1}

    def get_data():
        if len(currency_from) == 1:
            url = "https://api.getgeoapi.com/v2/currency/convert"
            response = requests.get(url, parameters).json()
            print(response["rates"]["UAH"]["rate"])
        else:
            new_url = f"https://api.getgeoapi.com/v2/currency/historical/{currency_from[1]}"
            response_date = requests.get(new_url, parameters).json()
            if response_date['status'] == "success":
                print(response_date["rates"]["UAH"]["rate"])
            else:
                print(f"Invalid date: {currency_from[1]}")

    if __name__ == "__main__":
        get_data()
except KeyError as e:
    print(f"Invalid currency name: {str(currency_from[0])}")
