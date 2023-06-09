def cal_simple_int(principal,years,cust_type):
    if cust_type == 'male' and years >= 55:
        rate = 0.7
    elif cust_type == 'male':
        rate = 0.5
    elif cust_type == 'female' and years >= 55:
        rate = 0.8
    else:
        rate = 0.6
    
    interest = principal * years * rate
    return interest

principal = float(input("Enter the principal amount: " ))
years = int(input("Enter the no of years: "))
cust_type = input("Enter are you (male/female):")
simple_interest = cal_simple_int(principal ,years , cust_type)
print("simple interest is : ",simple_interest)





customer = input("")