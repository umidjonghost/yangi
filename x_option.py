try:
    with open("example.txt", "x")  as file:
        file.write("Fayl yangi malumot bn yaratildi.")
except FileExistsError:
    print("fayl allaqachon mavjud")