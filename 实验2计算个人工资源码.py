import sys

def End_money(Number):
    Point=3500
    Protect =Number*(0.165)
    Cess=[0.03,0.1,0.2,0.25,0.3,0.35,0.45]
    Deduction=[0,105,555,1005,2755,5505,13505]
    Ratepaying_first=Number-Protect-Point
#    End_Money=Number-Ratepaying-Protect

    if Ratepaying_first >=0:
        if Ratepaying_first <=1500:
            Ratepaying = (Ratepaying_first * Cess[0]) - Deduction[0]
            return(Number-Ratepaying-Protect)
        elif Ratepaying_first <=4500 and Ratepaying_first>1500:
            Ratepaying = (Ratepaying_first * Cess[1]) - Deduction[1]
            return(Number-Ratepaying-Protect)
        elif Ratepaying_first <= 9000 and Ratepaying_first > 4500:
            Ratepaying = (Ratepaying_first * Cess[2]) - Deduction[2]
            return (Number-Ratepaying-Protect)
        elif Ratepaying_first <= 35000 and Ratepaying_first > 9000:
            Ratepaying = (Ratepaying_first * Cess[3]) - Deduction[3]
            return (Number-Ratepaying-Protect)
        elif Ratepaying_first <= 55000 and Ratepaying_first > 35000:
            Ratepaying = (Ratepaying_first * Cess[4]) - Deduction[4]
            return (Number-Ratepaying-Protect)
        elif Ratepaying_first <= 80000 and Ratepaying_first > 55000:
            Ratepaying = (Ratepaying_first * Cess[5]) - Deduction[5]
            return (Number-Ratepaying-Protect)
        elif Ratepaying_first > 80000:
            Ratepaying = (Ratepaying_first * Cess[6]) - Deduction[6]
            return (Number-Ratepaying-Protect)
        else:
            print("This is None!")
    else:
        return (Number - Protect)


First=sys.argv[1:]

money_list=[]
people_list=[]
hive=[]
for var in First:
    var=var.split(':')
    try:
        c=int(var[1])
    except:
        print('Parameter Error')
        continue
    money_list.append(c)
for people in First:
    people=people.split(':')
    people=people[0]
    people_list.append(people)
for kid in money_list:
    last_salary=(End_money(kid))
    hive.append(last_salary)

for x in range(len(First)):
    print('{0}:{1:.2f}'.format(people_list[x],hive[x]))








