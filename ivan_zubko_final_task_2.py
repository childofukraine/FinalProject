import requests

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
city_name = input("Enter your city: ").lower()
try:
    def response_func():
        api_url = 'https://api.api-ninjas.com/v1/city?name={}'.format(city_name)
        response = requests.get(api_url, headers={'X-Api-Key': "ixZwtSSbYFrVDZo3KaeA+Q==pRB0axCv4X0berXl"}).json()
        return response


    for i in numbers:
        while i in city_name:
            print("Incorrect city name")
            city_name = input("Enter correct city:")
        else:
            pass

    while response_func() == []:
        print(f"Invalid city name:{city_name}")
        city_name = input("Enter correct city:")


    def get_population(arg):
        return response_func()[0]['population']


    def get_country(arg):
        return response_func()[0]['country']


    def get_currency(country_code):
        url = "https://api.api-ninjas.com/v1/country?name={}".format(get_country(response_func))
        second_response = requests.get(url, headers={'X-Api-Key': "ixZwtSSbYFrVDZo3KaeA+Q==pRB0axCv4X0berXl"}).json()
        return second_response[0]['currency']['code']


    if __name__ == "__main__":
        print(get_country(response_func))
        print(get_currency(get_country))
        print(get_population(response_func))

except Exception as e:
    print("System Error")
