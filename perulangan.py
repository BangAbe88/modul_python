import abe
def main():
    t = str(input("Masukkan Text = "))
    n = int(input("Masukkan Jumlah perulangan = "))

    hasil = abe.perulangan(t, n)

    print(hasil, t)

if __name__=="__main__":
    main()
