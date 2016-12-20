# pyATCSup

### Requirements
- Python3
    - BeautifulSoup
    - requests
    - sys, getopt

### Usage
Clone the repo and execute the python script by passing the URL of the item you want carted as an argument.  This will return to you the price of the item added to your cart.

```

> python pyATCSup.py -u "http://www.supremenewyork.com/shop/accessories/r2efwvm5n/sg3ul6th5"
> Cart Subtotal: $460

```

### Work In Progress

+ Checkout
+ Item Size selection
+ Passing web session into a browser for manual checkout
+ Parsing site to search for an item instead of manually passing a URL
