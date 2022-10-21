import razorpay


class makePayment:
    def __init__(self, passdetails):
        self.passdetails = passdetails

    def validatePassdetails(self):
        if self.passdetails == "day":
            amount = 70 * 100
            return amount
        elif self.passdetails == "month":
            amount = 1000 * 100
            return amount

    def razorPay(self):
        amount = self.validatePassdetails()
        print(amount)
        client = razorpay.Client(auth=("rzp_test_rOZoAHYpnFYbrD", "iI8xiTkJPUsJsOr6haasNY9P"))
        data = {"amount": amount, "currency": "INR", "receipt": "#11"}
        payment = client.order.create(data=data)
        return payment
