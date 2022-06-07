from flask import request, redirect, url_for, render_template, flash, session
from salary import app
from decimal import Decimal, ROUND_HALF_UP

@app.route('/', methods=["GET", 'POST'])
def show_entries():
    if request.method == "GET":
        return render_template('input.html')
    else:
        return render_template('input.html')


@app.route('/output', methods=['GET','POST'])
def output():
    input_salary = request.form['salary']
    int_salary = int(input_salary)
    tax,payment = calcsalary(int_salary)
    return render_template("output.html", salary=input_salary, payment=payment, tax=tax)  #左のオレンジがHTML{{}}、右がdef outputの変数名
    



def calcsalary(salary):
    if salary > 1000000:
        tax = (salary - 1000000) * 0.2 + 100000
    else:
        tax = salary * 0.1
    tax = Decimal(str(tax)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
    payment = salary - tax
    return tax, payment


