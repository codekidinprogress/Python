def log_discount(func):
    def wrapper(amount):
        print("Applying discount...")
        result = func(amount)
        print("Discount applied successfully!")
        return result
    return wrapper

@log_discount
def apply_discount(amount):
    discount = amount * 0.10   # 10% discount
    final_price = amount - discount
    print("Final Price:", final_price)
    return final_price

apply_discount(2000)
