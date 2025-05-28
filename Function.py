def reverse_per_kata(kalimat):
    """
    Membalik setiap kata dalam kalimat tanpa mengubah urutan kata.
    
    Args:
        kalimat (str): Kalimat yang akan diproses
        
    Returns:
        str: Kalimat dengan setiap kata dibalik
    """
    kata_kata = kalimat.split()
    kata_terbalik = [kata[::-1] for kata in kata_kata]
    return ' '.join(kata_terbalik)

def urutkan_kalimat(kalimat, urutan):
    """
    Mengurutkan kata dalam kalimat berdasarkan indeks yang diberikan.
    Indeks dimulai dari 1 (bukan 0).
    
    Args:
        kalimat (str): Kalimat yang akan diurutkan
        urutan (list): Daftar indeks baru untuk kata-kata
        
    Returns:
        str: Kalimat yang telah diurutkan
    """
    kata_kata = kalimat.split()
    try:
        kalimat_terurut = [kata_kata[i-1] for i in urutan]
    except IndexError:
        return "Error: Indeks melebihi jumlah kata"
    return ' '.join(kalimat_terurut)

def ganti_vokal(kalimat, opsi):
    """
    Mengganti huruf vokal dengan simbol tertentu berdasarkan opsi.
    
    Args:
        kalimat (str): Kalimat yang akan diproses
        opsi (int): 1 untuk vokal kecil, 2 untuk vokal kapital
        
    Returns:
        str: Kalimat dengan vokal yang telah diganti
    """
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
    print("1. Reverse per kata:")
    print(reverse_per_kata("AKU CINTA KAMU"))  # Output: "UKA ATNIC UMAK"
    
    #urutkan_kalimat
    print("\n2. Urutkan kalimat:")
    print(urutkan_kalimat("HARI INI SEDANG BELAJAR PYTHON", [5, 1, 4, 3, 2]))  # Output: "PYTHON HARI BELAJAR SEDANG INI"
    
    #ganti_vokal
    print("\n3. Ganti vokal:")
    print("Opsi 1:", ganti_vokal("Aku Cinta Kamu", 1))  # Output: "Ak|_| C1nt4 K4m|_|"
    print("Opsi 2:", ganti_vokal("Aku Cinta Kamu", 2))  # Output: "4ku Cinta Kamu"
    
    #tambahan untuk error handling
    print("\n4. Test tambahan:")
    print("Indeks melebihi:", urutkan_kalimat("HARI INI", [3, 1, 2]))
    print("Kalimat kosong:", reverse_per_kata(""))
    print("Opsi tidak valid:", ganti_vokal("Aku", 3))