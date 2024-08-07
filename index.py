from config import FILES_PROGETS, FILE_EXTENSIONS, DIRETORIO, MESAGE_SCRIPT
import os

def Start():
    Folder_Name = input("Digite o nome da pasta: ")
    extetioin = input("Digite a extensão do seu projeto (por exemplo, .py): ")
    
    if extetioin not in FILE_EXTENSIONS:
        print("Extensão não reconhecida!")
        Start()
        return  # Adiciona return para evitar execução adicional após a chamada recursiva

    path = os.path.join(DIRETORIO, Folder_Name)
    
    # Cria o diretório se não existir
    os.makedirs(path, exist_ok=True)
    
    # Cria os arquivos dentro do diretório
    for file in FILES_PROGETS:
        file_path = os.path.join(path, f"{file}{extetioin}")
        
        with open(file_path, 'w', encoding='utf-8') as arquivo:
            print(f"File: {file, extetioin}")
            arquivo.write(MESAGE_SCRIPT)
    
    print(f"Todos os arquivos foram criados com sucesso no diretório '{path}'.")

if __name__ == "__main__":
    Start()
