
import numpy as np
print("Calculadora do igor modelo 2.0")
print("Para usar a calculadora é bem simples, basta falar os dados que você tem e os que você precisa")
print("exemplo de dados:")
print("Para 'Quais dados você tem?:'")
print("Se você tem o dado basta colocar o valor e apertar enter, caso contrario apenas aperte enter")
print("exemplo: Eu tenho vcc, mas não vbb então - vbb = 12 e vbb deixo vazio ")
print("Para 'O que você quer saber?:'")
print("Só iserir dessa maneira os dados: 'r1 r2'")

while True:
    lista = ["vbb","vb1","vb2","vcc","trabalho1","trabalho2","r1","r2","c","rmin","rmax","vv","vi","ip","vp","fmax","fmin","n","rbb","rbbmin","tmin","tmax"]
    lista2 = []
    dic = {}
    dcalcs = {"vbb" :["vb1","vb2","vcc",'rmin','rmax','iv','vv','ip','vp','r2','n','rbbmin'],'vb1':['vb2','vbb'],'vb2':['vb1','vbb']}
    check = []
    checkd = {}
    r2type = ""

    
#Lista de variáveis para cada conta
#Vbb
    calc1 = ["vbb","vb1","vb2"]
    set1 = []
    calc2 = ["vbb","vcc"]
    set2 = []

#Trabalho
    calc3 = ["trabalho1","r1","c"]
    set3 = []
    calc4 = ["trabalho2","r2","c"]
    set4 = []

#Rmin e Rmax
    calc5 = ["rmin","vbb","vv","iv"]
    set5 = []
    calc6 = ["rmax","vbb","vp","ip"]
    set6 = []

#Frequencia
    calc7 = ["rmax","c","n","fmin"]
    set7 = []
    calc8 = ["rmin","c","n","fmax"]
    set8 = []

#rbb
    calc9 = ["r1","r2","rbb"]
    set9 = []

#r2 normal
    calc10 = ["vcc","rbb","n","r2"]
    set10 = []

#vp
    calc11 = ["vp","n","vbb","vd"]
    set11 = []

#T
    calc12 = ["tmax","rmin","c","n"]
    set12 = []

    calc13 = ["tmin","rmax","c","n"]
    set13 = []

#R2 outros
    calc14 = ["r2","n","vbb"]
    set14 = []

    calc15 = ["rbbmin","r2","n","vbb","r1"]
    set15 = []
#### calculos
    def fcalc1(x):
        if x == "vbb":
            vbb = dic["vb1"] + dic["vb2"]
            dic["vbb"] = vbb
            try:
                lista2.remove(x)
            except:
                pass
        elif x == "vb1":
            vb1 = dic["vbb"] - dic["vb2"]
            dic["vb1"] = vb1
            try:
                lista2.remove(x)
            except:
                pass
        elif x == "vb2":
            vb2 = dic["vbb"] - dic["vb1"]
            dic["vb2"] = vb2
            try:
                lista2.remove(x)
            except:
                pass

    def fcalc2(x):
        if x == "vbb":
            
            vbb = dic["vcc"]
            dic["vbb"] = vbb
            try:
                lista2.remove(x)
            except:
                pass
        if x == "vcc":
            vcc = dic["vbb"]
            dic["vcc"] = vcc
            try:
                lista2.remove(x)
            except:
                pass

    def fcalc3(x):
            if x == "trabalho1":
                trabalho1 = dic["r1"] * dic["c"]
                dic["trabalho1"] = trabalho1 
                try:
                    lista2.remove(x)
                except:
                    pass

            elif x == "r1":
                trabalho1 = dic["trabalho1"] / dic["c"]
                dic["r1"] = trabalho1
                try:
                    lista2.remove(x)
                except:
                    pass

            elif x == "c":
                trabalho1 = dic["trabalho1"] * dic["r1"]
                dic["c"] = trabalho1
                try:
                    lista2.remove(x)
                except:
                    pass
   
    def fcalc4(x):
            if x == "trabalho2":
                trabalho2 = dic["r2"] * dic["c"]
                dic["trabalho2"] = trabalho2
                try:
                    lista2.remove(x)
                except:
                    pass

            elif x == "r2":
                r2t = dic["trabalho2"] / dic["c"]
                dic["r2"] = r2t
                try:
                    lista2.remove(x)
                except:
                    pass

            elif x == "c":
                trabalho1 = dic["trabalho2"] * dic["r2"]
                dic["c"] = trabalho1
                try:
                    lista2.remove(x)
                except:
                    pass
   
    def fcalc5(x):
            if x == "rmin":
                rmin = (dic["vbb"] - dic["vv"])
                rmin = rmin/dic["iv"]
                dic["rmin"] = rmin
                try:
                    lista2.remove(x)
                except:
                    pass
            elif x == "iv":
                iv = (dic["vbb"] - dic["vv"])
                iv = iv/dic["rmin"]
                dic["iv"] = iv
                try:
                    lista2.remove(x)
                except:
                    pass
            elif x == "rbb":
                vbb = dic["rmin"] * dic["iv"]
                vbb = vbb + dic["vv"]
                dic["vbb"] = vbb
                try:
                    lista2.remove(x)
                except:
                    pass
            elif x == "vv":
                vv = dic["rmin"] * dic["iv"]
                vv = vv - dic["vbb"]
                dic["vv"] = vv
                try:
                    lista2.remove(x)
                except:
                    pass
    
    def fcalc6(x):
            if x == "rmax":
                rmin = (dic["vbb"] - dic["vp"])
                rmin = rmin/dic["ip"]
                dic["rmax"] = rmin
                try:
                    lista2.remove(x)
                except:
                    pass
            elif x == "ip":
                iv = (dic["vbb"] - dic["vp"])
                iv = iv/dic["rmmax"]
                dic["ip"] = iv
                try:
                    lista2.remove(x)
                except:
                    pass
            if x == "rbb":
                vbb = dic["rmax"] * dic["ip"]
                vbb = vbb + dic["vp"]
                dic["vbb"] = vbb
                try:
                    lista2.remove(x)
                except:
                    pass
            elif x == "vp":
                vv = dic["rmax"] * dic["ip"]
                vv = vv - dic["vbb"]
                dic["vp"] = vv
                try:
                    lista2.remove(x)
                except:
                    pass

    def fcalc7(x):
        if x == "fmin":
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            fmin = dic["rmax"] * dic["c"] * ln
            fmin = 1 / fmin
            dic["fmin"] = fmin
            try:
                lista2.remove(x)
            except:
                pass
        elif x == "c":
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            fmin = dic["rmax"] * dic["fmin"] * ln
            fmin = 1 / fmin
            dic["c"] = fmin
            try:
                lista2.remove(x)
            except:
                pass
        elif x == "rmax":
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            fmin = dic["fmin"] * dic["c"] * ln
            fmin = 1 / fmin
            dic["rmax"] = fmin
            try:
                lista2.remove(x)
            except:
                pass

    def fcalc8(x):
        if x == "fmax":
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            fmax = dic["rmin"] * dic["c"] * ln
            fmax = 1 / fmax
            dic["fmax"] = fmax
            try:
                lista2.remove(x)
            except:
                pass
        elif x == "c":
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            c = dic["rmin"] * dic["fmax"] * ln
            c = 1 / c
            dic["c"] = c
            try:
                lista2.remove(x)
            except:
                pass
        elif x == "rmin":
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            fmax = dic["fmax"] * dic["c"] * ln
            fmax = 1 / fmax
            dic["rmin"] = fmax
            try:
                lista2.remove(x)
            except:
                pass
    
    def fcalc9(x):
            if x == "r1":
                r1 = dic["r2"] * 10
                r1 = dic["rbb"] - r1
                r1 = r1 / 10
                dic["r1"] = r1
                try:
                    lista2.remove(x)
                except:
                    pass

    def fcalc10(x):
            if x == "r2":
                r2 = 0.015 * dic["vcc"] * dic["rbb"] * dic["n"]
                dic["r2"] = r2
                try:
                    lista2.remove(x)
                except:
                    pass

    def fcalc11(x):
            if x == "vp":
                vp = dic["n"] * dic["vbb"] + dic["vd"]
                dic["vp"] = vp
                try:
                    lista2.remove(x)
                except:
                    pass
            elif x == "n":
                n = dic["vp"] - dic["vd"]
                n = n / dic["vbb"]
                dic["n"] = n
                try:
                    lista2.remove(x)
                except:
                    pass
            elif x == "vd":
                vd = dic["n"] * dic["vbb"]
                vd = dic["vp"] / vd
                dic["vd"] = vd
                try:
                    lista2.remove(x)
                except:
                    pass
            elif x == "vbb":
                vbb = dic["vp"] - dic["vd"]
                vbb = vbb / dic["n"]
                dic["vbb"] = vbb
                try:
                    lista2.remove(x)
                except:
                    pass

    def fcalc12(x):
        if x == "tmax": 
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            t = dic['rmin'] * dic["c"] * (ln)
            t = t/100
            dic["tmax"] = t
            try:
                lista2.remove(x)
            except:
                pass
        elif x == "c": 
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            t = dic["tmax"] / (dic['rmin'] * ln)
            dic["c"] = t
            try:
                lista2.remove(x)
            except:
                pass
        if x == "rmin": 
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            t = dic["tmax"] / (dic['c'] * ln)
            dic["rmin"] = t
            try:
                lista2.remove(x)
            except:
                pass

    def fcalc13(x):
        if x == "tmin": 
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            t = dic['rmax'] * dic["c"] * ln
            dic["tmin"] = t
            try:
                lista2.remove(x)
            except:
                pass
        elif x == "c": 
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            t = dic["tmin"] / (dic['rmax'] * ln)
            dic["c"] = t
            try:
                lista2.remove(x)
            except:
                pass
        elif x == "rmax": 
            i = 1 - dic["n"]
            i = 1 / i
            ln = np.log(i)
            t = dic["tmin"] / (dic['c'] * ln)
            dic["rmax"] = t
            try:
                lista2.remove(x)
            except:
                pass

    def fcalc14(x):
        if x == "r2":
            r2 = 10000 / (dic["n"] * dic["vbb"])
            dic["r2"] = r2
            try:
                lista2.remove(x)
            except:
                pass

    def fcalc15(x):
        i = (1 - dic["n"])
        i = i * dic["r1"]
        i = i / dic["n"]
        r2 = (0.4 * dic["rbbmin"]) / (dic["n"] * dic["vbb"])
        dic["r2"] = r2
        try:
            lista2.remove(x)
        except:
            pass

    def OqueVoceQuer():
        print("o que voocê quer saber?")
        dataR1 = input()
        dataR1 = dataR1.lower()
        dataR1 = dataR1.split()
        for r in dataR1:
            for i in lista:
              if i == r:
                  lista2.append(r) 
        if lista2 == check:
            print("Nenhuma Variavel encontrada")

        
    def seusDados():
        print("Quais dados você tem?")
        for i in lista:
            dataR1 = input("{} = ".format(i))
            if not dataR1:
                continue
            else:
                try:
                    dataR1 = int(dataR1)
                except:
                    dataR1 = float(dataR1)
                dic[i] = dataR1
                
        if dic == checkd:
            print("Nenhuma Variavel encontrada")
        print("Tipo de R2:")
        print("1 - normal")
        print("2 - 2646 ou 2647")
        print("3 - 1671 ou 2160")
        r2type = input()
        dic['r2t'] = r2type

    def separarCalculo():
    ##cada for desse analisa os dados que você ja tem
    ##e os alocas em uma list de verificação
        set1 = []
        set2 = []
        set3 = []
        set4 = []
        set5 = []
        set6 = []
        set7 = []
        set8 = []
        set9 = []
        set10 = []
        set11 = []
        set12 = []
        set13 = []
        set14 = []
        set15 = []

        for i in dic:
            if i in calc1:
                set1.append(i)
    
        for i in dic:
            if i in calc2:
                set2.append(i)
    
        for i in dic:
            if i in calc3:
                set3.append(i)
    
        for i in dic:
            if i in calc4:
                set4.append(i)
            
        for i in dic:
            if i in calc5:
                set5.append(i)

        for i in dic:
            if i in calc6:
                set6.append(i)

        for i in dic:
            if i in calc7:
                set7.append(i)

        for i in dic:
            if i in calc8:
                set8.append(i)

        for i in dic:
            if i in calc9:
                set9.append(i)

        for i in dic:
            if i in calc10:
                set10.append(i)
        
        for i in dic:
            if i in calc11:
                set11.append(i)
        
        for i in dic:
            if i in calc12:
                set12.append(i)
        
        for i in dic:
            if i in calc13:
                set13.append(i)
        
        for i in dic:
            if i in calc14:
                set14.append(i)
        
        for i in dic:
            if i in calc15:
                set15.append(i)
#verifica os calculos que precisam de apenas uma variavel para serem feitos

##### Calc1
        x = []
        if len(set1)+1 == len(calc1):
            x = calc1
            for i in set1:
                x.remove(i)
            fcalc1(x[0])
##### Calc2
        x = []
        if len(set2)+1 == len(calc2):
            x = calc2
            for i in set2:
                x.remove(i)
            fcalc2(x[0])
##### Calc3
        x = []
        if len(set3)+1 == len(calc3):
            x = calc3
            for i in set3:
                x.remove(i)
            fcalc3(x[0])
##### Calc4
        x = []
        if len(set4)+1 == len(calc4):
            x = calc4
            for i in set4:
                x.remove(i)
            fcalc4(x[0])
##### Calc5
        x = []
        if len(set5)+1 == len(calc5):
            x = calc5
            for i in set5:
                x.remove(i)
            fcalc5(x[0])
##### Calc6
        x = []
        if len(set6)+1 == len(calc6):
            x = calc6
            for i in set6:
                x.remove(i)
            fcalc6(x[0])
##### Calc7
        x = []
        if len(set7)+1 == len(calc7):
            x = calc7
            for i in set7:
                x.remove(i)
            fcalc7(x[0])
##### Calc8
        x = []
        if len(set8)+1 == len(calc8):
            x = calc8
            for i in set8:
                x.remove(i)
            fcalc8(x[0])
##### Calc9
        x = []
        if len(set9)+1 == len(calc9):
            x = calc9
            for i in set9:
                x.remove(i)
            fcalc9(x[0])
##### Calc10 R2 
        if dic['r2t'] == '1':
            if len(set10)+1 == len(calc10):
                x = calc10
                for i in set10:
                    x.remove(i)
                fcalc10(x[0])
        
        
        if dic['r2t'] == '2':
            if len(set14)+1 == len(calc14):
                x = calc14
                for i in set14:
                    x.remove(i)
                fcalc14(x[0])
            
##### Calc11
        x = []
        if len(set11)+1 == len(calc11):
            x = calc11
            for i in set11:
                x.remove(i)
            fcalc11(x[0])

##### Calc12
        x = []
        if len(set12)+1 == len(calc12):
            x = calc12
            for i in set12:
                x.remove(i)
            fcalc12(x[0])

##### Calc13
        x = []
        if len(set13)+1 == len(calc13):
            x = calc13
            for i in set13:
                x.remove(i)
            fcalc13(x[0])

        if dic['r2t'] == '3':
            if len(set15)+1 == len(calc15):
                x = calc15
                for i in set15:
                    x.remove(i)
                fcalc15(x[0])
    seusDados()
    OqueVoceQuer()
    while lista2 != check:
        separarCalculo()
    for i in dic:
        print(i," = ",dic[i])
    