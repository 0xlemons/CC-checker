class Luhn:
  @staticmethod
  def check(cc_number):
      weight = "2121212121212121"  
      while len(weight) < len(cc_number):
          weight += weight  
      values = []
      for i, number in enumerate(cc_number):
          num = int(weight[i])
          product = num * int(number)
          if product >= 10:
              product = sum(int(digit) for digit in str(product))
          values.append(product)
      total = sum(values)
      
      return total % 10 == 0
