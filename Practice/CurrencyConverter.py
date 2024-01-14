def currencyConvertor(inr: float, currency: str):
    if currency.lower() == "dirham":
        print(f"{inr} INR is equal to {0.044 * inr} UAED")
    elif currency.lower() == "yen":
        print(f"{inr} INR is equal to {1.75 * inr} YEN")
    elif currency.lower() == "aud":
        print(f"{inr} INR is equal to {0.018 * inr} AUD")
    else:
        print("Please enter the correct currency")


print("Hi user, welcome to my currency converter.")
inr = float(input("Please enter ruppes to be converted: "))
curr = input(
    "Please choose the currency type. \n\nWe can convert it into "
    "following currencies. You can either input the currency name or "
    "choose options 1,2,3\n1.UAED \n2.YEN \n3.AUD \nCurrency Type: ")
if curr.lower() == "1":
    curr = "UAED"
elif curr.lower() == "2":
    curr = "YEN"
elif curr.lower() == "3":
    curr = "AUD"
print(f"Converting {inr} INR to {curr}")
currencyConvertor(inr, curr)
