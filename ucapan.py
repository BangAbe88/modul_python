import abe
import time
def main():
    nama=input("Masukkan nama anda = ")
    cetak=abe.ucapan(nama)

    #inisialisali waktu
    waktu=time.gmtime()
    a=time.localtime()
    hr=a.tm_hour
    mn=a.tm_min
    sc=a.tm_sec
    print(cetak, 'Sekarang Pukul', '{}:{}:{}'.format(hr,mn,sc))

if __name__=="__main__":
    main()
