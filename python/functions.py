def add(num1, num2):
    return num1 + num2

print(add(34,6))

def fahr_to_celsius(temp):
    """
    This function converts temperature from fahrenheit
      to celsius.
      Args:
      -----
        tempInFahr: temperature in fahrenheit

      Returns:
      --------
        tempInCel: temperature in celsius
    """
    tempInCel = (temp - 32) * 5/9
    return tempInCel

print(fahr_to_celsius(-30))