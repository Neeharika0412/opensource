x=int(input().strip())
discount_1=x*0.10
discount_2=100
max_discount=max(discount_1,discount_2)
amount_to_pay=x-max_discount
print(int(amount_to_pay))
