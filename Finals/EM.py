x = [3,7]
u = [3,4,7]
z = [0,0,0,0,0,0]

for i in range(2):
    denom = 0;
    for j in range(3):
        denom += pow(2.718281828, -((x[i]-u[j])*(x[i]-u[j])))
    for k in range(3):
        z[3*i+k] = pow(2.718281828, -((x[i]-u[k])*(x[i]-u[k])))/denom

for i in range(3):
    denom = 0
    numer = 0
    for j in range(2):
        denom += z[3*j+i]
        numer += z[3*j+i]*x[j]
    u[i] = numer/denom

print(z)
print(u)

for i in range(2):
    denom = 0;
    for j in range(3):
        denom += pow(2.718281828, -((x[i]-u[j])*(x[i]-u[j])))
    for k in range(3):
        z[3*i+k] = pow(2.718281828, -((x[i]-u[k])*(x[i]-u[k])))/denom

for i in range(3):
    denom = 0
    numer = 0
    for j in range(2):
        denom += z[3*j+i]
        numer += z[3*j+i]*x[j]
    u[i] = numer/denom

print(z)
print(u)
