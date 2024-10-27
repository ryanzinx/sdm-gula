def konversi_gula_ke_nasi(gram_gula):
    """
    Mengkonversi gram gula ke sendok makan nasi berdasarkan kandungan karbohidrat
    - 1 gram gula = 1 gram karbohidrat
    - 1 sendok makan nasi = 4 gram karbohidrat
    """
    # Gula murni, sehingga 1 gram gula = 1 gram karbohidrat
    karbohidrat_gula = gram_gula
    
    # 1 sendok makan nasi mengandung 4 gram karbohidrat
    karbohidrat_per_sendok_nasi = 4
    
    # Hitung berapa sendok makan nasi yang setara kandungan karbohidratnya
    sendok_makan_nasi = karbohidrat_gula / karbohidrat_per_sendok_nasi
    return sendok_makan_nasi

def main():
    print("Program Konversi Kandungan Karbohidrat Gula ke Nasi")
    print("================================================")
    print("Catatan:")
    print("- 1 gram gula = 1 gram karbohidrat")
    print("- 1 sendok makan nasi = 4 gram karbohidrat")
    
    while True:
        try:
            gula_gram = float(input("\nMasukkan jumlah gram gula (0 untuk keluar): "))
            
            if gula_gram == 0:
                print("Terima kasih telah menggunakan program ini!")
                break
                
            if gula_gram < 0:
                print("Masukkan nilai positif!")
                continue
                
            sendok_makan_nasi = konversi_gula_ke_nasi(gula_gram)
            print(f"\n{gula_gram:.1f} gram gula mengandung {gula_gram:.1f} gram karbohidrat")
            print(f"Setara dengan {sendok_makan_nasi:.1f} sendok makan nasi")
            
        except ValueError:
            print("Masukkan angka yang valid!")

if __name__ == "__main__":
    main()