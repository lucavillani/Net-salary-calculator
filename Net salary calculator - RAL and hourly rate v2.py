
tax_bracket_15k = 15000 - 0
tax_bracket_28k = 28000 - 15000
tax_bracket_50k = 50000 - 28000
#tax_bracket_over50k da calcolare post
tax_rate_15k = 0.23 
tax_rate_28k = 0.25 
tax_rate_50k = 0.35 
tax_rate_over50k = 0.43 

def net_salary_calculator():
    if (gross_salary) < 15000:
        net_salary = gross_salary - gross_salary * (tax_rate_15k)
    if (gross_salary) > 15000 and (gross_salary) < 28000:
        net_salary = gross_salary - (tax_bracket_15k * (tax_rate_15k) + (gross_salary - 15000) * (tax_rate_28k))
    if (gross_salary) > 28000 and (gross_salary) < 50000:
        net_salary = gross_salary - (tax_bracket_15k * (tax_rate_15k) + tax_bracket_28k * (tax_rate_28k) + ((gross_salary - 28000) * (tax_rate_50k)))
    if (gross_salary) > 50000:
        net_salary = gross_salary - (tax_bracket_15k * (tax_rate_15k) + tax_bracket_28k * (tax_rate_28k) + tax_bracket_50k * (tax_rate_50k) + ((gross_salary - 50000) * (tax_rate_over50k)))
    print()
    print("Il tuo stipendio mensile netto è di circa", int(net_salary / 14),"€") #ATTUALMENTE 14 MENSILITA 

print()
print()
print("BENVENUTO NEL CALCOLATORE DI STIPENDIO NETTO")
print()
print()
type_of_salary = input("Vuoi inserire la tua RAL o il tuo rate orario? ")
print()

if type_of_salary != "RAL" and type_of_salary != "rate orario":
    print("Per scegliere digita le parole 'RAL' o 'rate orario'")
    print()
    type_of_salary = input("Vuoi inserire la tua RAL o il tuo rate orario? ")

if type_of_salary == "RAL":
    gross_salary = int(input("Inserisci la tua RAL: "))
    net_salary_calculator()


if type_of_salary=="rate orario":
    hourly_rate = input("Inserisci il tuo rate orario: ")
    print()
    hours = input("Quante ore lavori a settimana? ")
    print()
    gross_salary = ((int(hourly_rate)*int(hours)) / 7) * 364
    net_salary_calculator()

print()

print("Lo stipendio viene calcolato sulla base di 14 mensilità.")

print()

input("")