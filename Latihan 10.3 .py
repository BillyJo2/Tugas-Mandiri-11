nama_file = input("Masukkan nama file: ")
try:
    file = open(nama_file, 'r')
except:
    print("File tidak ditemukan")
    quit()


histogram_email = {}


for baris in file:
    if baris.startswith('From '):
        email = baris.split()[1]
        histogram_email[email] = histogram_email.get(email, 0) + 1


file.close()


print(histogram_email)
