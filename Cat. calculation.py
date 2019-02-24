#cat. type selection
option1=int(input('''Please select: 1 for Ru/Al2O3, 2 for Cu/ZnO w/.Ru, 3 for Ru/ZnO, 4 for Cu/ZnO, 5 for Cu/Al2O3
'''))

#Ru-Al2O3 calculation
def ru1(x1,y1):
    a1=y1*x1/100/0.375 #0.445 is Ru content in ruthenium chloride
    b1=(1-x1/100)*y1
    print('Mass of RuCl3-xH2O is %4f in grams' % a1)
    print('Mass of alumina is %4f in grams' % b1)
    input('Press enter to exit')

#Cu/ZnO/Al2O3 w/. Ru calculation
def copper(a2,b2,c2,d2,t2):
    e2=a2/100*t2/63.546*241.56
    f2=b2/100*t2/81.408*297.36
    g2=c2/100*t2/101.96*374.996*2
    h2=d2/100*t2/0.375
    print('The weight of copper nitrate is %4fg,weight of zinc nitrate is %4fg,weight of aluminum nitrate is %4fg, the weight of RuCl3 is %4fg' %(e2,f2,g2,h2))

#Ru/ZnO/Al2O3 calculation
def zinc(b3,c3,d3,t3):
    f3=b3/100*t3/81.408*297.36
    g3=c3/100*t3/101.96*374.996*2
    h3=d3/100*t3/0.375
    print('The weight of zinc nitrate is %4fg,weight of aluminum nitrate is %4fg, the weight of RuCl3 is %4fg' %(f3,g3,h3))

def copper_zinc(a4,b4,t4):
    e4=a4/100*t4/63.546*241.56
    f4=b4/100*t4/81.408*297.36
    print('The weight of copper nitrate is %4fg,weight of zinc nitrate is %4fg' %(e4,f4))
def copper_alumina(a5,c5,t5):
    e5=a5/100*t5/63.546*241.56
    g5=c5/100*t5/101.96*374.996*2
    print('The weight of copper nitrate is %4fg,weight of aluminum nitrate is %4fg' %(e5,g5))
if option1==1:
    x1=float(input('Ru mass weight ratio in percentage '))
    if x1<0 or x1>100:
        print('Input value error')
        x1=float(input('Ru mass weight ratio in percentage '))
    y1=float(input('Total cat. weight in grams '))
    ru1(x1,y1)
elif option1==2:
    a2=float(input('Cu weight ratio in % '))
    if a2>100 or a2<0:
        print('Value range: 0 - 100')
        a2=float(input('Cu weight ratio in % '))
    b2=float(input('ZnO weight ratio in % '))
    if b2>100 or b2<0:
        print('Value range: 0 - 100')
        b2=float(input('ZnO weight ratio in % '))
    c2=float(input('Al2O3 weight ratio in % '))
    if c2>100 or c2<0:
        print('Value range: 0 - 100')
        c2=float(input('Al2O3 weight ratio in % '))
    d2=float(input('Ru weight ratio in % '))
    if d2>100 or d2<0:
        print('Value range: 0 - 100')
        d2=float(input('Ru weight ratio in % '))
    t2=float(input('Total catalyst weight in gram '))
    copper(a2,b2,c2,d2,t2)
    proceed2=int(input('Press 1 if you want to calculate solution volume? '))
    if proceed2==1:
        def volume(q,w,r):
            vol2=(a2*t2/63.546+b2*t2/81.408+c2*t2/101.96*2)/100*1000/q2     #Soultion volume to reach certain metal ion concentration
            mass2=r2/1000*w2*84.001     #Mass of NaHCO3 in gram
            print('Concentration of metal is %2fM, volume is %dml. You need %4fg of NaHCO3 and %dml water to get %2fM' %(q2,vol2,mass2,r2,w2))
            return vol2,mass2
        q2=float(input('Concentration of metal ion in mol/L '))
        w2=float(input('Concentration of NaHCO3 in mol/L '))
        r2=float(input('Volume of NaHCO3 solution in ml '))
        volume(q2,w2,r2)
        input('Press enter to exit ')
    else:
        input('Press enter to exit ')
elif option1==3:
    a3=int(input('''Press 1 using Al(NO3)3, 2 using Al2O3
'''))
    if a3==1:
        b3=float(input('ZnO weight ratio in % '))
        if b3>100 or b3<0:
            print('Value range: 0 - 100')
            b3=float(input('ZnO weight ratio in % '))
        c3=float(input('Al2O3 weight ratio in % '))
        if c3>100 or c3<0:
            print('Value range: 0 - 100')
            c3=float(input('Al2O3 weight ratio in % '))
        d3=float(input('Ru weight ratio in % '))
        if d3>100 or d3<0:
            print('Value range: 0 - 100')
            d3=float(input('Ru weight ratio in % '))
        t3=float(input('Total catalyst weight in gram '))
        zinc(b3,c3,d3,t3)
        proceed3=int(input('Press 1 if you want to calculate solution volume? '))
        if proceed3==1:
            def volume(q,w,r):
                vol3=(b3*t3/81.408+c3*t3/101.96*2)/100*1000/q3     #Soultion volume to reach certain metal ion concentration
                mass3=r3/1000*w3*84.001     #Mass of NaHCO3 in gram
                print('Concentration of metal is %2fM, volume is %dml. You need %4fg of NaHCO3 and %dml water to get %2fM' %(q3,vol3,mass3,r3,w3))
                return vol3,mass3
            q3=float(input('Concentration of metal ion in mol/L '))
            w3=float(input('Concentration of NaHCO3 in mol/L '))
            r3=float(input('Volume of NaHCO3 solution in ml '))
            volume(q3,w3,r3)
            input('Press enter to exit ')
        else:
            input('Press enter to exit ')
    elif a3==2:
        f3=float(input('The weight of alumina support in grams '))
        g3=float(input('The weight ratio of alumina in % '))
        h3=float(input('The weight ratio of Ru in % '))
        i3=f3/g3*100*(1-g3/100-h3/100)/81.408*297.36   #Weight of Zn(NO3)2
        j3=f3/g3*100*h3/100/0.375     #Weight of RuCl3
        print('Weight of Zn(NO3)2 is %4fg, weight of RuCl3 is %4fg'%(i3,j3))
        input('Press enter to exit')
elif option1==4:
    a4=float(input('Cu weight ratio in % '))
    if a4>100 or a4<0:
        print('Value range: 0 - 100')
        a4=float(input('Cu weight ratio in % '))
    b4=float(input('ZnO weight ratio in % '))
    if b4>100 or b4<0:
        print('Value range: 0 - 100')
        b4=float(input('ZnO weight ratio in % '))
    t4=float(input('Total catalyst weight in gram '))
    copper_zinc(a4,b4,t4)
    input('Press enter to exit ')
elif option1==5:
    a5=float(input('Cu weight ratio in % '))
    if a5>100 or a5<0:
        print('Value range: 0 - 100')
        a5=float(input('Cu weight ratio in % '))
    c5=float(input('Al2O3 weight ratio in % '))
    if c5>100 or c5<0:
        print('Value range: 0 - 100')
        c5=float(input('Al2O3 weight ratio in % '))
    t5=float(input('Total catalyst weight in gram '))
    copper_alumina(a5,c5,t5)
    input('Press enter to exit ')