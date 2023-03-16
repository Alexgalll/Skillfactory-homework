bilet = int(input("Укажите колличество биллетов: "))
vozrast = int(input("Сколько вам лет?: "))
if vozrast < 18:
    print("Вы проходите бесплатно")
if 18 <= vozrast <= 25:
    if bilet >= 3:
        cost = (bilet * 990) - (bilet * 990 * 0.1)
        print("Сумма к оплате: ", round(cost))
    else:
        cost = bilet * 990
        print("Сумма к оплате: ", round(cost))
if vozrast > 25:
    if bilet >= 3:
        cost = (bilet * 1390) - (bilet * 1390 * 0.1)
        print("Сумма к оплате: ", round(cost))
    else:
        cost = bilet * 1390
        print("Сумма к оплате: ", round(cost))