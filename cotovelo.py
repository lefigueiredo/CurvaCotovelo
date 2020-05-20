'Porcetagem'
listax = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
          15, 16, 17, 18, 19, 20, 21, 22]

listay = [2.995420683143152E17, 1.48637849744363296E17,
          1.11916255663311344E17, 7.2851781127241536E16,
          5.3530103381035824E16, 3.9395581891888312E16, 3.3934229001199996E16,
          3.106144615990274E16, 2.4615937396344888E16, 1.60145653328451E16,
          1.6972212470907838E16, 1.2155487438242432E16, 1.108782966643766E16,
          9.470233742272172E15, 8.241956772787882E15, 6.92890991571094E15,
          6.472823918773062E15, 6.143544389650474E15, 5.67668257118002E15,
          4.925761577341026E15]


def findk(columnx, columny):
    datas = columnx
    percentage = []
    teste = []
    teste1 = []
    teste2 = []


    if datas[1] - datas[0] == 1:
        datas = columny

    for i in datas:
        percentage.append(i*100/datas[0])

    for i in range(len(percentage)):
        print(f'x = {listax[i]}, % = {percentage[i]}')
        if i == len(percentage) - 1:
            continue
        else:
            print(percentage[i] - percentage[i + 1])

        if percentage[i] - percentage[i+1] < 1:
            teste.append(listax[i])
        if percentage[i+1] - percentage[i] < -2:
            teste1.append(listax[i+1])

    for k in teste:
        if k in teste1:
            teste2.append(k)



    print(teste)
    print(teste1)
    print(teste2)


print(findk(listay, listax))

