import datetime


def generate_order_number(pk):
  current_datetime = datetime.datetime.now().strftime('%Y%m%d%H%M%S') #202206162333 + pk
  order_number = current_datetime + str(pk)
  return order_number