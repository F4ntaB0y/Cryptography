import hashlib

def md5_dari_file(nama_file):
    md5 = hashlib.md5()
    try:
        with open(nama_file, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5.update(chunk)
        return md5.hexdigest()
    except FileNotFoundError:
        print("❌ File tidak ditemukan.")
        return None

def main():
    print("=== MD5 Generator dari File ===")
    file_path = input("Masukkan path ke file: ")
    hash_md5 = md5_dari_file(file_path)
    if hash_md5:
        print(f"MD5 dari file adalah:\n{hash_md5}")

if __name__ == "__main__":
    main()
