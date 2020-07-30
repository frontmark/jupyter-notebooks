from pyvacon.pricing import price as _price

def price(pr_data):
    if hasattr(pr_data, 'price'):
        return pr_data.price()
    else:
        return _price(pr_data)