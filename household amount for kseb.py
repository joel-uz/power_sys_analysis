"""
This is a project based on economic evaluation of 10 houses and to get the
rough monthly estimate of the amount.
"""

bpl_val = 1.5
bpl_person = False
telescopic = [3.3, 4.1, 5.2, 6.9]
non_tele = [6.5, 6.5, 7.6, 7.6, 7.6, 8.7]

single_phase_fixed = {50:40, 100:80, 150:90, 200:120, 250:140, 300:140, 350:200, 400:200, 500:200}
three_phase_fixed = {50:135, 100:190, 150:190, 200:190, 250:190, 300:190, 350:205, 400:205, 500:205}

print("STARTING THE PROJECT")
print("Getting the data")

for i in range(1,11):
    print("\nDetails of house",i)
    bimonth = float(input("Bi-monthly energy usage in kWh(As per the bill): "))
    peak_power = float(input("Peak connected load value in kW: "))
    # 3 phase load when peak load greater than 7.5kW
    phase = int(input("Whether three phase or single phase load? (1[3phase]/0[1phase]): "))
    monthly = float(bimonth/2)

    cost = 0

    # TARIFF CONSUMER CHARGES

    if monthly <= 40 and peak_power <= 1:
        cost = monthly * bpl_val
        bpl_person = True
    elif monthly <= 200:
        if monthly <= 50:
            cost = monthly * telescopic[0]
        elif monthly <= 100:
            cost = 50 * telescopic[0] + (monthly-50) * telescopic[1]
        elif monthly <= 150:
            cost = 50 * telescopic[0] + 50 * telescopic[1] + (monthly-100) * telescopic[2]
        else:
            cost = (50 * telescopic[0] + 50 * telescopic[1] + 50 * telescopic[2] +
                    (monthly-150) * telescopic[3])
    else:
        if monthly <= 250:
            cost = monthly * non_tele[0]
        elif monthly <= 300:
            cost = monthly * non_tele[1]
        elif monthly <= 350:
            cost = monthly * non_tele[2]
        elif monthly <= 400:
            cost = monthly * non_tele[3]
        elif monthly <= 500:
            cost = monthly * non_tele[4]
        elif monthly > 500:
            cost = monthly * non_tele[5]

    fixed = 0

    # CONSUMER FIXED CHARGES

    if phase == 1 and bpl_person == False:
        for val in three_phase_fixed:
            if monthly < val:
                fixed += three_phase_fixed[val]
                break
        else:
            fixed += 265
    elif phase == 0 and bpl_person == False:
        for val in single_phase_fixed:
            if monthly < val:
                fixed += single_phase_fixed[val]
                break
        else:
            fixed += 255

    # SHOWING DETAILS
    print("details of house", i,"--")
    print("Energy: ",monthly, " kWh")
    print("Load Power: ", peak_power," kW")
    print("Monthly cost: Rs.", cost)
    print("Fixed rate: Rs.",fixed)
    print("Total: Rs.",cost + fixed)
    print("-------------------------------")

