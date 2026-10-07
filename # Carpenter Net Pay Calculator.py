# Carpenter Net Pay Calculator

hrly_pay = float(input("What is your hourly pay rate $"))
hrs_worked = float(input("What is your hours"))
fed_wh = 0.25
state_wh = 0.04
socsec_wh = 0.062
med_wh = 0.0145

grossInc = hrly_pay * hrs_worked
print(grossInc)

grossInc= grossIncssInc * fed_wh
state_whAmt = grossInc * state_wh
socsec_whAmt = grossInc * socsec_wh
med_whAMt = grossInc * med_wh
print(fed_whAmt)
print(state_whAmt)
print(socsec_whAmt)
print(med_whAMt)

total_whAmt = fed_whAmt + state_whAmt + socsec_whAmt + med_whAMt
print(total_whAmt)

net_Pay = grossInc - total_whAmthAmt
print("Your total net pay is")
print(net_Pay)