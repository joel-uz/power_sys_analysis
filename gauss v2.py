from Y_bus import y_bus
import cmath, math

"Find out the admittance matrix"

admit_matrix, bus = y_bus()

"Get the bus details and voltage or angle values"
P = []  # Active power
Q = []  # Reactive power
V = []  # Voltage levels
D = []  # Delta angle/ excitation angle
bus_details = []

for i in range(1, bus+1):
    print(f"Enter the details of bus {i}")
    while True:
        ask = int(input("IS the bus a PQ(1), PV(2) or a reference bus(3) :"))
        if ask == 1:
            p = float(input("Enter the Active power in p.u = "))
            q = float(input("Enter the Reactive power in p.u = "))
            P.append(p)
            Q.append(q)
            V.append(1)
            D.append(0)  # assumptions
            bus_details.append(ask)
            break

        elif ask == 2:
            p = float(input("Enter the Active power in p.u = "))
            v = float(input("Enter the voltage in p.u = "))
            P.append(p)
            Q.append(0)
            V.append(v)
            D.append(0)  # assumptions
            bus_details.append(ask)
            break

        elif ask == 3:
            v = float(input("Enter the voltage in p.u = "))
            d = float(input("Enter the excitation angle = "))
            P.append(0)
            Q.append(0)
            V.append(cmath.rect(v, d))
            D.append(d)
            bus_details.append(ask)
            break
        else:
            print("Not a valid number!! \n")

print("\n")
print("Completed data collection")
print(P,Q,V,D)


#  ----------------------Iterations -----------------------
print("\n")
iterations = int(input("How many iterations do you require?: "))

for iter in range(1,iterations+1):
    print(f"For the {iter} iteration, the values are")
    print(f"V_bus 1 = {complex(V[0], 0)}")

    for each_voltage in range(1,len(V)):
        sum_of_voltage = 0
        q_temp = 0
        for current in range(0,bus):
            q_temp += admit_matrix[each_voltage][current]*V[current]
            if each_voltage != current:
                sum_of_voltage += admit_matrix[each_voltage][current]*V[current]
            else:
                continue

        if bus_details[each_voltage] == 2:
            q_temp *=V[each_voltage]
            Q[each_voltage] = q_temp.imag * (-1)

        new_voltage = (1/admit_matrix[each_voltage][each_voltage])*((
                (P[each_voltage]-complex(0,Q[each_voltage]))/V[each_voltage])-sum_of_voltage)
        V[each_voltage] = new_voltage
        print(f"The voltage for bus {each_voltage} is ",new_voltage)
    print('\n')