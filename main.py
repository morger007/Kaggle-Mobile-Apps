# coding=utf-8
from openpyxl import load_workbook
import matplotlib.pyplot as plt


def contain_lis(cell, list):
    # method that check contain cell element from given list
    for elem in list:
        if cell.value.count(elem) > 0:
            return True
    return False


def percent(double):
    global summa
    return round(double/summa * 100, 2)

# add here fullpath name to your statement


workbook = load_workbook(filename="veb.xlsx")

SHOPS = ["MAXIMA", "KONSUM", "KAUBAMAJA", "RIMI", "SELVER"]
FASTFOODS = ["MCDONALDS", "Shaurma", "pizza", "R-kiosk", "KOHVIK", "KFC"]
TRANSPORTS = ["LIINIRONGID", "LUX EXPRESS", "Tankla", "OLEREX", "RIDANGO"]
RENT = ['ÜLIÕPILASKÜLA']
sheet = workbook["Sheet0"]
# i is 6 because statement actually starts from this row
i = 6
food = fastfood = transport = rent = other = 0


# run through excel sheet
while sheet["$C%i" % i].value and sheet["$E%i" % i].value:
    cell = sheet["$C%i" % i]
    if contain_lis(cell, SHOPS):
        food -= sheet["$E%i" % i].value
    elif contain_lis(cell, FASTFOODS):
        fastfood -= sheet["$E%i" % i].value
    elif contain_lis(cell, TRANSPORTS):
        transport -= sheet["$E%i" % i].value
    else:
        other -= sheet["$E%i" % i].value

    i += 1


summa = sum([food, fastfood, transport, other, rent])
print("Еда : %s \nФастфуд: %s \nТранспорт: %s \nАренда: %s \nДругое: %s \nВсего: %s" %
      (food, fastfood, transport, rent, other, summa))


# Make data: I have 5 groups and 7 subgroups
group_names = ['food %s' % percent(food), 'fastfood %s' % percent(fastfood),
               'transport %s' % percent(transport), 'rent %s' % percent(rent),
               'other %s' % percent(other)]
group_size = [food, fastfood, transport, rent, other]

for i in range(len(group_size) - 1):
    if group_size[i] == 0:
        del group_names[i]
        del group_size[i]


# Create colors
food_color, fastfood_color, transport_color, rent_color, other_color =\
    [plt.cm.Blues, plt.cm.Reds, plt.cm.Greens, plt.cm.Purples, plt.cm.Oranges]

# First Ring (Outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[food_color(0.6), fastfood_color(0.6),
                                                                      transport_color(0.6), rent_color(0.6),
                                                                      other_color(0.6)])
plt.setp(mypie, width=0.3, edgecolor='white')

plt.margins(0, 0)

# show it
plt.show()
