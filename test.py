a = int(input("Введите номер аудитории: "))
room_responsible = {501: "Borubaeva",
                    502: "Sydykbekov",
                    503: "Zamirbekov",
                    504: "Imanalieva",
                    505: "Danshina",
                    506: "Kuldanbaev"}
def find_responsible(a):
    if a == 501:
        return "Borubaeva"
    elif a == 502:
        return "Sydykbekov"
    elif a == 503:
        return "Zamirbekov"
    elif a == 504:
        return "Imanalieva"
    elif a == 505:
        return "Danshina"
    elif a == 506:
        return "Kuldanbaev"
    else:
        print("Неизвестная аудитория")
print(find_responsible(a))
"""for a in room_responsible:
    print(a, room_responsible[a])"""

"""def find_responsible(a):
    if a in room_responsible:
        print(room_responsible.values())"""
"""b = 501
c = 502
d = 503
e = 504
f = 505
g = 506
h = "Borubaeva"
i = "Sydykbekov"
j = "Zamirbekov"
k = "Imanalieva"
l = "Danshina"
m = "Kuldanbaev"
def find_responsible(a):
    if a in room_responsible:
        print(a)
        print(o, "Your auditory is %s" % (nummer[b]))"""