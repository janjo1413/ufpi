salario = float(input("Digite seu salário: "))
f1 = 2259.20
f2 = 2826.65
f3 = 3751.05
f4 = 4664.68
taxa = 0.0

if salario > f4:
    taxa += (salario - f4) * 0.275
    salario = f4
if salario <= f4 and salario > f3:
    taxa += (salario - f3) * 0.225
    salario = f3
if salario <= f3 and salario > f2:
    taxa += (salario - f2) * 0.15
    salario = f2
if salario <= f2 and salario > f1:
    taxa += (salario - f1) * 0.075
print(f"Taxa total é {taxa:.2f}")


