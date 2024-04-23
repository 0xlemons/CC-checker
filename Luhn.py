class Luhn:
    def check(cc_number):
        
        weight = "2121212121212121"
        values = []
        index = 0
        for number in cc_number:
            num = int(weight[index])
            index += 1
            product = int(num) * int(number)
            if product >= 10:
                product = str(product)
                product = int(product[0]) + int(product[1])
                if product >= 10:
                    return False
            digit = str(product)
            if digit[0] == '4':
                brand = 'Visa'
            elif digit[:3] == '34' or digit[:3] == '37':
                brand = 'American Express'
            elif digit[:4] == '6011' or digit[:2] == '65' or (digit[:6] >= '622126' and digit[:6] <= '622925') or (digit[:3] >=  '644' and digit[:3] <= '649'):
                brand = 'Discover Card'
            elif digit[:2] >= '51' and digit[:2] <= '55':
                brand = 'Mastercard'
            else:
                brand = 'Unkown Brand'
            values.append(f'{product} : {brand}')
        total = 0
        for val in values:
            total += val
        total = str(total)
        if int(total[len(total) - 1]) % 10 == 0:

            return True
        return False
