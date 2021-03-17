import requests

""" Uses api.coindesk.com to get exchange rates """


def main():
    dollars = 'USD'
    num_bitcoin = get_bitcoin_amount()
    converted = convert_bpi_to_dollars(num_bitcoin, dollars)
    display_result(num_bitcoin, converted)


def get_bitcoin_amount():
    """ Get number of Bitcoin """
    return float(input('Enter amount of Bitcoin to convert: '))


def convert_bpi_to_dollars(num_bitcoin, dollars):
    """ Convert amount of bitcoin to USD """
    exchange_rate = get_exchange_rate(dollars)
    converted = convert(num_bitcoin, exchange_rate)
    return converted


def get_exchange_rate(dollars):
    """ Call API and extra data from response """
    response = request_rates()
    rate = extract_rate(response, dollars)
    return rate


def request_rates():
    """ Perform API request, return response """
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(coindesk_url).json()
    return response


def extract_rate(rate, dollars):
    """ Process the JSON response from the API, extract rate data """
    return rate['bpi'][dollars]['rate_float']


def convert(num_bitcoin, exchange_rate):
    """ Convert using the given exchange rate """
    return num_bitcoin * exchange_rate


def display_result(num_bitcoin, converted):
    """ Format and display the result """
    print(f'${num_bitcoin:.2f} is equivalent to ${converted:.2f}.')


if __name__ == '__main__':
    main()
