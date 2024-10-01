from dataclasses import dataclass
from time import sleep
import os
import platform

@dataclass
class tool():
    def Install_Django():
        try:
            if platform.system() == "Windows": 
                os.system("py -m pip install Django")
                return True
            else:
                os.system("python -m pip install Django")
                return True
        except:
            print("Nao Foi Possivel Intalar Ou Atalizar O Django")
            sleep(2)
            return False
    
    def Verify_OS():
        return platform.system()