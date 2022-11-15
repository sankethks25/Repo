from flask import Flask, render_template, request, redirect
from Authentication.LoginUser import LoginUser
from Beans.Passanger import Passanger
from Payment.MakePayment import makePayment
# from Service.PassangerService import PassangerService
from Validations.BusDetailsValidation import BusDetailValidation
import rook

app = Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return render_template("login.html")


@app.route("/check", methods=['POST'])
def checkDetails():
    if request.method == 'POST':
        username = request.form.get("login")
        password = request.form.get("password")
        login = LoginUser(username, password)
        if login.checkUserDetails():
            return render_template("home_details.html")


@app.route("/home_details")
def home_details():
    return render_template("home_details.html")


@app.route("/applypass")
def applyPass():
    return render_template("apply_home.html")


# @app.route("/savedetails", methods=['POST'])
# def saveDetails():
#     global passanger, passangerService
#     try:
#         if request.method == 'POST':
#             passanger = Passanger()
#             passangerService = PassangerService()
#             # setters ------------------------------------
#             passanger.name = request.form.get("name")
#             passanger.number = request.form.get("phno")
#             passanger.age = request.form.get("age")
#             passanger.gender = request.form.get("Gender")
#             passanger.passdetails = request.form.get("pass_details")
#             source = request.form.get("from")
#             dest = request.form.get("to")
#             passanger.setRoute(source, dest)
#             return takeToPaymentPortal(request.form.get("pass_details"))
#     finally:
#         if razorResponse() == "True":
#             print("-----success-----")
#             passangerService.applyPass(passanger)


@app.route("/view")
def readyToViewPass():
    return render_template("view_pass.html")


@app.route("/viewpass", methods=['POST'])
# def viewPass():
#     phno = request.form.get("phno")
#     passangerService = PassangerService()
#     passangerService.displayPass(phno)
#     importData = passangerService.importData()
#     return render_template("my_pass.html", result=importData)

@app.route("/busdetails")
def busDetails():
    # return render_template("navbar.html")
    return render_template("bus_details.html")


@app.route("/getbusdetails", methods=['POST'])
def getBusDetails():
    source = request.form.get("from")
    dest = request.form.get("to")
    busDetailValidation = BusDetailValidation(source, dest)
    result = busDetailValidation.validate()

    return render_template("bus_details_result.html", result=result)


# ------------------------------------PAYMENT-------------------------------------------------
def takeToPaymentPortal(details):
    paymentdetails = makePayment(details)
    payment = paymentdetails.razorPay()
    return render_template("pay.html", payment=payment)


@app.route("/responseid")
def razorResponse():
    return "True"

if __name__ == "__main__":
    rook.start(token='7580342505e87fa47b9d8e03b0f5df684e19960d951c83155c97192d114580b4',
               labels={"env": "dev1"})
    app.run(debug=True)
