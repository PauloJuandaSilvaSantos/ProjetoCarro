from Carro import Carro
from Hibrido import Hibrido




def main():


 carro1 = Carro("azul",1999,"f44")

 carro2 = Hibrido("preto", 2000, "f45")
 carro1.acelerar()
 carro1.freiar()



 carro2.CarregarBateria()
 carro2.freiar()
 carro2.acelerar()





if (__name__=="__main__"):
    main()
