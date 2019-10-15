import math
def grade1(nilai):
        if nilai<50:
            print("Nilai Anda E"+" __Maaf, anda tidak lulus mohon coba kembali")
        elif nilai>=50 and nilai<=59:
            print("Nilai Anda D"+" __Maaf, anda masih belum lulus mohon coba kembali")
        elif nilai>=60 and nilai<=74:
            print("Nilai Anda C"+" __Alhamdulillah, anda lulus dengan nilai cukup")
        elif nilai>=75 and nilai<=84:
            print("Nilai Anda B"+" __Alhamdulillah, anda lulus dengan nilai bagus")
        elif nilai>=85 and nilai<=100:
            print("Nilai Anda A"+" __Alhamdulillah, anda lulus dengan nilai Keren..!")
        else:
            print("Maaf Nilai anda tidak dapat kami eksekusi"+"\n__________________Karena Anda Melakukan banyak kesalahan.________ \nTerimaKasih")
