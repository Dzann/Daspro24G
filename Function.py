def reverse_per_kata(kalimat):
    kata_kata = kalimat.split()
    kata_terbalik = [kata[::-1] for kata in kata_kata]
    return ' '.join(kata_terbalik)

def urutkan_kalimat(kalimat, urutan):
    kata_kata = kalimat.split()
    try:
        kalimat_terurut = [kata_kata[i-1] for i in urutan]
    except IndexError:
        return "Error: Indeks melebihi jumlah kata"
    return ' '.join(kalimat_terurut)

def ganti_vokal(kalimat, opsi):
    vokal_kecil = {'a': '4', 'i': '1', 'u': '|_|', 'e': '3', 'o': '0'}
    vokal_kapital = {'A': '4', 'I': '1', 'U': '|_|', 'E': '3', 'O': '0'}
    
    hasil = []
    for karakter in kalimat:
        if opsi == 1 and karakter in vokal_kecil:
            hasil.append(vokal_kecil[karakter])
        elif opsi == 2 and karakter in vokal_kapital:
            hasil.append(vokal_kapital[karakter])
        else:
            hasil.append(karakter)
    return ''.join(hasil)

# Menguji Function
if __name__ == "__main__":
    #reverse_per_kata
    print(reverse_per_kata("AKU CINTA KAMU"))  # Output: "UKA ATNIC UMAK"
    
    #urutkan_kalimat
    print(urutkan_kalimat("HARI INI SEDANG BELAJAR PYTHON", [5, 1, 4, 3, 2]))  # Output: "PYTHON HARI BELAJAR SEDANG INI"
    
    #ganti_vokal
    print("Opsi 1:", ganti_vokal("Aku Cinta Kamu", 1))  # Output: "Ak|_| C1nt4 K4m|_|"
    print("Opsi 2:", ganti_vokal("Aku Cinta Kamu", 2))  # Output: "4ku Cinta Kamu"