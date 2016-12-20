#!/usr/bin/python

# https://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup as bs
# https://www.tutorialspoint.com/python/python_command_line_arguments.htm
import sys, getopt
import requests



def main(argv):
    # Creating and accepting URL argument
    URL = ''
    # URL = "http://www.supremenewyork.com/shop/hats/fy7o3hm6q/x6940enzd"
    try:
        opts, args = getopt.getopt(argv,"hu:",["uri=","url="])
    except getopt.GetoptError:
        print ('ARGUMENT FAILURE.  SYNTAX NEEDED: atctest.py -u <URI_OF_ITEM>')
        sys.exit()
    if len(sys.argv) == 1:
        print ('ARGUMENT FAILURE.  SYNTAX NEEDED: atctest.py -u <URI_OF_ITEM>')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print('atctest.py -u <URL_OF_ITEM>')
            sys.exit()
        elif opt in ("-u", "--uri", "--url"):
            URL = arg

    base_url = 'http://www.supremenewyork.com'

    # Creating session
    websession = requests.Session()
    websession.headers.update({
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8,da;q=0.6'
    })

    # Get first response from site
    webresponse = websession.get(URL)
    parseresponse = bs(webresponse.text, 'html.parser')

    # Use parsed response to get parameters for POST
    cartparams = parseresponse.find('form', {'id':'cart-addf'})
    addtocarturl = base_url + cartparams.get('action')
    token = cartparams.find('input', {'name':'authenticity_token'}).get('value')
    utf = cartparams.find('input', {'name':'utf8'}).get('value')
    size = cartparams.find('input', {'name':'size'}).get('value')
    commit = cartparams.find('input', {'name':'commit'}).get('value')
    postparam = {'utf8': utf, 'authenticity_token': token, 'size': size, 'commit': commit}

    # Use the paramaters to send POST request
    add_to_cart = websession.post(addtocarturl, data=postparam)

    # Get Cart response
    cart = websession.get('http://www.supremenewyork.com/shop/cart')

    # Parse Cart response
    carttotalraw = bs(cart.text, 'html.parser')

    # Get cart toal
    carttotal = carttotalraw.find('span', {'class':'cart-price-span'})

    print("Cart Subtotal: " + carttotal.text)

if __name__ == "__main__":
   main(sys.argv[1:])
