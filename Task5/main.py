print("""
 $$$$$$\            $$\                     $$\            $$\                         
$$  __$$\           $$ |                    $$ |           $$ |                        
$$ /  \__| $$$$$$\  $$ | $$$$$$$\ $$\   $$\ $$ | $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  
$$ |       \____$$\ $$ |$$  _____|$$ |  $$ |$$ | \____$$\\_$$  _|  $$  __$$\ $$  __$$\ 
$$ |       $$$$$$$ |$$ |$$ /      $$ |  $$ |$$ | $$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|
$$ |  $$\ $$  __$$ |$$ |$$ |      $$ |  $$ |$$ |$$  __$$ | $$ |$$\ $$ |  $$ |$$ |      
\$$$$$$  |\$$$$$$$ |$$ |\$$$$$$$\ \$$$$$$  |$$ |\$$$$$$$ | \$$$$  |\$$$$$$  |$$ |      
 \______/  \_______|\__| \_______| \______/ \__| \_______|  \____/  \______/ \__|      
      
"𝓘 𝓭𝓸𝓷'𝓽 𝓻𝓮𝓪𝓵𝓵𝔂 𝓵𝓲𝓴𝓮 𝓶𝓪𝓽𝓱, 𝓫𝓾𝓽 𝓘 𝓵𝓲𝓴𝓮 𝓽𝓸 𝓬𝓸𝓾𝓷𝓽 𝓮𝓿𝓮𝓻𝔂 𝓶𝓲𝓷𝓾𝓽𝓮𝓼 𝔀𝓲𝓽𝓱 𝔂𝓸𝓾"
""")

def menu():
    print("""Menu : 
        1. Kali
        2. Bagi
        3. Tambah
        4. Kurang
        5. Keluar
          """)


def kali(a,b):
    return a * b

def bagi(a,b):
    return a / b

def tambah(a,b):
    return a + b

def kurang(a,b):
    return a - b



menu()
while True:
    choice = input("Masukkan pilihan(1-5): ")
    if choice in ('1','2','3','4','5'):
        if choice == '5':
            print("Terima kasih telah menggunakan program ini - Jovaneah")
            break
        try:
            num1 = float(input("Masukkan angka pertama : "))
            num2 = float(input("Masukkan angka kedua   : "))
        except ValueError:
            print("Inputanmu tidak valid")
            continue
        
        if choice == '1':
            print(f"{num1} x {num2} = {kali(num1,num2)}")
        elif choice == '2':
            print(f"{num1} : {num2} = {bagi(num1,num2)}")
        elif choice == '3':
            print(f"{num1} + {num2} = {tambah(num1,num2)}")
        elif choice == '4':
            print(f"{num1} - {num2} = {kurang(num1,num2)}")
