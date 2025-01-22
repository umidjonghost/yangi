
#
# import os
#
# file_path = "example.txt"
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"fayl {file_path} ochirildi")
#
# else:
#     print("fayl mavjud emas")


import os

dir_path = "manzil"
if os.path.exists(dir_path) and os.path.isdir(dir_path):
    os.rmdir(dir_path)  ## bosh direktoriyani ochiradi
    print(f"Direktoriya {dir_path} ochirildi. ")
else:
    print("Direktoriyaning mavjud emasligi yoki bosh emasligi. ")