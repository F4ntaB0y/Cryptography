import hashlib

def md5_dari_teks(teks):
    hasil = hashlib.md5(teks.encode()).hexdigest()
    return hasil

def main():
    print("=== MD5 Generator dari Teks ===")
    teks = input("Masukkan teks: ")
    hash_md5 = md5_dari_teks(teks)
    print(f"MD5 dari teks tersebut adalah:\n{hash_md5}")

if __name__ == "__main__":
    main()
