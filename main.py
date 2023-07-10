
def fazla_tekrarlayan(metin):
    # Metni küçük harflere dönüştürmek
    metin = metin.lower()

    # Noktalama işaretlerini kaldırmak
    noktalama_isaretleri = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for karakter in metin:
        if karakter in noktalama_isaretleri:
            metin = metin.replace(karakter, "")

    # Metni kelimelere ayırmak
    kelimeler = metin.split()

    # Kelimeleri saymak
    kelime_sayilari = {}
    for kelime in kelimeler:
        if kelime in kelime_sayilari:
            kelime_sayilari[kelime] += 1
        else:
            kelime_sayilari[kelime] = 1

    # En sık kullanılan kelimeyi bulmak
    en_sik_kelime = ""
    en_sik_kelime_sayisi = 0
    for kelime, sayi in kelime_sayilari.items():
        if sayi > en_sik_kelime_sayisi:
            en_sik_kelime = kelime
            en_sik_kelime_sayisi = sayi

    return en_sik_kelime,en_sik_kelime_sayisi

# Örnek bir metin
metin =input("bir metin gir: ")
# En sık kullanılan kelimeyi bulmak için fonksiyonu çağırmak
en_sik_kelime,en_sik_kelime_sayisi = fazla_tekrarlayan(metin)
print("En sık kullanılan kelime:", en_sik_kelime)
print("Bu kelime", en_sik_kelime_sayisi, "defa kullanılmış.")