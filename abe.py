import math
def grade(nilai):
        if nilai<50:
            return("Nilai Anda E"+" __Maaf, anda tidak lulus mohon coba kembali")
        elif nilai>=50 and nilai<=59:
            return("Nilai Anda D"+" __Maaf, anda masih belum lulus mohon coba kembali")
        elif nilai>=60 and nilai<=74:
            return("Nilai Anda C"+" __Alhamdulillah, anda lulus dengan nilai cukup")
        elif nilai>=75 and nilai<=84:
            return("Nilai Anda B"+" __Alhamdulillah, anda lulus dengan nilai bagus")
        elif nilai>=85 and nilai<=100:
            return("Nilai Anda A"+" __Alhamdulillah, anda lulus dengan nilai Keren..!")
        else:
            return("Maaf Nilai anda tidak dapat kami eksekusi"+"\n__________________Karena Anda Melakukan banyak kesalahan.________ \nTerimaKasih")
def ucapan(nama):
    return 'Halo salam kenal '+ nama
def perulangan(t, n):
    nilai = 0
    while (nilai < n):
        print (t, [nilai+1])
        nilai = nilai +1
    
