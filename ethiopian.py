def multiply_two_numbers(num1, num2):
    origin_num1 = num1
    origin_num2 = num2

    result = 0
    while(num1 > 1):
        num1 //= 2
        num2 *= 2
        
        if num1 == 0:
            break

        if num1 == 1:
            result += num2
            break
        
        if num1 % 2 == 1:
            result += num2

    print(f'{origin_num1} x {origin_num2} =', result)

num1, num2 = list(map(int, input('Enter Two Numbers with blank: ').split()))

if __name__=='__main__':
    multiply_two_numbers(num1, num2)
