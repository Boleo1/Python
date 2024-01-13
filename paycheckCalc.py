# This program will calculate your paycheck for you based on your hours worked and your hourly wage.
import turtle


hourly_wage = float(input("What is your hourly wage? "))
hours_worked = float(input("How many hours did you work this pay period? "))
hours_print = "If your hourly wage is ( %i ) and you worked ( %i ) hours the following calculations should be on your paycheck:" % (hourly_wage, hours_worked)
print(hours_print)
print("")
gross_pay = float(hourly_wage) * float(hours_worked)
gross_pay = float(gross_pay)
gross_print = "Your gross pay is %.2f" % (gross_pay)
print(gross_print)


employee_health_premium = float(22.91)
pension_employee_contribue = float(.06)
federal_tax_rate = float(.0750)
fica_employee = float(.0610)
ficamed_employee = float(.0142)

federal_tax = gross_pay * federal_tax_rate
print("FED INC TAX: %.2f" % (federal_tax))

fica_employee_tax = gross_pay * fica_employee
print("FICA/EMPLOYEE tax: %.2f" % (fica_employee_tax))

securian_tax = gross_pay * pension_employee_contribue
print("Securian investment: %.2f" % (securian_tax))

ficamed_tax = gross_pay * ficamed_employee
print("FICAMED/EMPLOYEE tax: %.2f" % (ficamed_tax))



total_tax = federal_tax + fica_employee_tax + securian_tax + ficamed_tax + employee_health_premium
print("Total taxation: %.2f" % (total_tax))

net_pay = gross_pay - total_tax

print("Total net pay: %.2f" % (net_pay))

monthly_net_pay = net_pay * 2
monthly_tax = total_tax * 2
print("Monthly pay would be: %.2f" % (monthly_net_pay))

quarterly_pay = monthly_net_pay * 3
quarterly_tax = monthly_tax * 3
print("Quarterly pay would be: %.2f" % (monthly_net_pay))

annual_pay = quarterly_pay * 4
annual_tax = quarterly_tax * 4
print("Annual pay would be: %.2f" % (annual_pay))
print("Annual tax would be: %.2f" % (annual_tax))

win = turtle.Screen()
win.title("Pong by @BoleoTV")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Gross Pay: {gross_pay}  Net Pay: {net_pay}", align="center", font=("courier", 24,"normal"))