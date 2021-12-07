from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function


# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type = 'Overnight'):
  distance = get_distance(*from_coords, *to_coords)
  shipping_rate = SHIPPING_PRICES[shipping_type]
  price = distance * shipping_rate
  return format_price(price)


# Test the function by calling 
test_function(calculate_shipping_cost)