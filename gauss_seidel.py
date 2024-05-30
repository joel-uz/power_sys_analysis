"""The code performs gauss seidel power flow analysis and gives the value of voltage and
power angle for each of the iterations
 Applicable for 2bus and 3 bus systems"""

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
    ask = int(input("IS the bus a PQ(1), PV(2) or a reference bus(3) :"))
    bus_details.append(ask)
    if ask == 1:
        p = float(input("Enter the Active power in p.u = "))
        q = float(input("Enter the Reactive power in p.u = "))
        P.append(p)
        Q.append(q)
        V.append(1)
        D.append(0)  # assumptions

    elif ask == 2:
        p = float(input("Enter the Active power in p.u = "))
        v = float(input("Enter the voltage in p.u = "))
        P.append(p)
        Q.append(0)
        V.append(v)
        D.append(0)  # assumptions


    elif ask == 3:
        v = float(input("Enter the voltage in p.u = "))
        d = float(input("Enter the excitation angle = "))
        P.append(0)
        Q.append(0)
        V.append(cmath.rect(v,d))
        D.append(d)

print("\n")
print("Completed data collection")
print(P,Q,V,D)

#  ----------------------Iterations -----------------------
print("\n")
iterations = int(input("How many iterations do you require?: "))
k = 0

V1 = V[0]
V2 = [V[1]]

if bus == 3:
    V3 = [V[2]]


for i in range(0, iterations):

    print(f"after {i+1} iterations the values are:")
    print("V1 = ", V1)

    if bus_details[1] == 1:
        new_v = (1/admit_matrix[1][1]) * ( ((P[1]-complex(0, Q[1])) /V2[i]) - ( admit_matrix[1][0] * V1 + admit_matrix[1][2] * V3[i] ))
        V2.append(new_v)
        k += 1

    elif bus_details[1] == 2:
        new_q = V2[i]*(admit_matrix[1][0]*V1 + admit_matrix[1][1]*V2[i] + admit_matrix[1][2]*V3[i])
        actual_q = new_q.imag * (-1)
        new_v = (1 / admit_matrix[1][1]) * (
                    ((P[1] - complex(0, actual_q)) / V2[i]) - (admit_matrix[1][0] * V1 + admit_matrix[1][2] * V3[i]))
        V2.append(new_v)
        k += 1

    print("V2 = ", abs(V2[i + 1]))
    print("V2 phase = ", cmath.phase(V2[i + 1]) * 180 / math.pi)

    if bus == 3:
        if bus_details[2] == 1:
            new_v = (1 / admit_matrix[2][2]) * (
                        ((P[2] - complex(0, Q[2])) / V3[i]) - (admit_matrix[2][0] * V1 + admit_matrix[2][1] * V2[k]))
            V3.append(new_v)

        elif bus_details[2] == 2:
            new_q = V3[i] * (admit_matrix[2][0] * V1 + admit_matrix[2][1] * V2[k] + admit_matrix[2][2] * V3[i])
            actual_q = new_q.imag * (-1)
            new_v = (1 / admit_matrix[2][2]) * (
                    ((P[2] - complex(0, actual_q)) / V3[i]) - (admit_matrix[2][0] * V1 + admit_matrix[2][1] * V2[k]))
            V3.append(new_v)

        print("V3 = ", abs(V3[i+1]))
        print("V3 phase = ", cmath.phase(V3[i+1])*180/math.pi)


