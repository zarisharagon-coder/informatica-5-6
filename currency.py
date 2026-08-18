def main():
    pesos = int(input("How much do u have left in pesos??"))
    soles = int(input("How much do u have left in soles??"))
    reais= int(input("How much do u have left in reais??"))
    d=  (((pesos*0.0054)+(soles*5.07)+(reais*3.28))/17)
    print("Dollars:", d)
    pmx= (d* 17.06)
    print( "Pesos Mx:", pmx)
if __name__ =="__main__":
    main()

