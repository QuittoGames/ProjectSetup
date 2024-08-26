from config import FILES_PROGETS, FILE_EXTENSIONS, DIRETORIO, MESAGE_SCRIPT,TOOLS_CODE_BASE
import os
import platform
from time import sleep

Code_Base_On = True

def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def Start(Code_Base_On):
    clear_screen()
    Folder_Name = input("Digite o nome da pasta: ").strip()
    extetioin = input("Digite a extensão do seu projeto (por exemplo, .py): ").strip()

    if extetioin == ".config" or extetioin == ".c":
        Config_Admin()
        return
    
    if extetioin not in FILE_EXTENSIONS:
        print("Extensão não reconhecida!")
        Start(Code_Base_On)
        return  # Adiciona return para evitar execução adicional após a chamada recursiva

    if extetioin != ".py":
        Code_Base_On = False

    path = os.path.join(DIRETORIO, Folder_Name)
    
    # Cria o diretório se não existir
    os.makedirs(path, exist_ok=True)
    
    # Cria os arquivos dentro do diretório
    for file in FILES_PROGETS:
        file_path = os.path.join(path, f"{file}{extetioin}")
        
        with open(file_path, 'w', encoding='utf-8') as arquivo:
            print(f"File: {file, extetioin}")
            if file == "tool" and Code_Base_On:
                arquivo.write(TOOLS_CODE_BASE)
            arquivo.write(MESAGE_SCRIPT)
    
    print(f"Todos os arquivos foram criados com sucesso no diretório '{path}'.")

def Config_Admin():
    clear_screen()
    def Codes_Bases():
        def Add_In_Code_Base(code):
            TOOLS_CODE_BASE + code 

        print(f"Code Base tool.py: {TOOLS_CODE_BASE}")
        print("1. Add in Code Base")
        print("2. Remove in Code Base")
        c = input("Digite Sua Escolha: ")
        if c == "1":
            code = input("Digite Seu Code: ")
            Add_In_Code_Base(code=code)
        elif c == "2":
            Code_Base_On = False
            Config_Admin()
            return
        else:
            print("Comando Nao Pdoe Ser Idetificado! ")
            sleep(1)
            Codes_Bases()
            return

    def Mesage_Code():
        clear_screen()
        print("1. Mudar Mensage Code")
        c = input("Digite Sua Escolha: ")
        if c.lower() == "1":
            new_mensage_code = input("Digite Seu Novo Mensage Code: ")
            MESAGE_SCRIPT = new_mensage_code
            print("Code Aleterado Com Susseso!")
            sleep(1)
            Config_Admin()
            return
        else:
            print("Comando Nao Indetificado! ")
            sleep(1)
            Config_Admin()
            return
            
    
    def Diretory_Manege(DIRETORIO):
        clear_screen()
        print(f"Diretorio: {DIRETORIO}")
        print("1. Alterar Diretorio")
        c = input("Digite Sua Opiçao: ")
        if c == "1":
            new_Diretory = input("Digite Seu Diretorio: ").strip()
            DIRETORIO = new_Diretory
            print("Diretorio Aleterado Com Susseso!")
            sleep(1)
            Config_Admin()
            return
        else:
            print("Comando Nao Pode Ser Indetificado! ")
            sleep(1)
            Diretory_Manege()
            return
        
    def Files_Mange():
        def Add_File():
            name_file = input("Digite O Nome Do Arquivo: ")
            FILES_PROGETS.append(name_file)
            print("File Adicionado Com Susseso!")
            sleep(1)
            Files_Mange()
            return
        
        def Remove_File():
            name_file = input("Digite O Nome Do Arquivo: ")
            FILES_PROGETS.pop(name_file)
            print("File Removido Com Susseso!")
            sleep(1)
            Files_Mange()
            return
        
        clear_screen()
        print(f"Files: {FILES_PROGETS}")
        print("1. Add File")
        print("2. Remove Files")
        c = input("Digite Sua Opiçao: ")
        if c == "1":
            Add_File()
        elif c == "2":
            Remove_File()
        elif c == "":
            Config_Admin()
        else:
            print("Comando Nao Pode Ser Indetificado! ")
            sleep(1)
            Files_Mange()
            return 
        
    clear_screen()
    print("Config")
    print("1. Codes Bases")
    print("2. Mensage Code")
    print("3. Diretorio")
    print("4. Files")
    print("5. Return To Script")

    command = input("Digite Sua Opiçao: ")

    if command == "1":
        Codes_Bases()
    elif command == "2":
        Mesage_Code()
    elif command == "3":
        Diretory_Manege(DIRETORIO= DIRETORIO)
    elif command == "4":
        Files_Mange()
    elif command == "5":
        Start(Code_Base_On=Code_Base_On)
        return
    else:
        print("Comando Nao pode ser idetificado!")
        Config_Admin()
        return
    

if __name__ == "__main__":
    Start(Code_Base_On=Code_Base_On)
