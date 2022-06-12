#Coded by Connec - THT - Green Team

import subprocess
import optparse
import re
import os
from termcolor import colored
import time

os.system("apt-get install figlet | apt-get install toilet")
os.system("clear")
os.system("figlet THTMacChanger | toilet --gay -f term")
os.system("toilet MacChanger - Coded By Connec V1.0 --gay -f term")
time.sleep(2.5)


def user_inputs():
    optparse_object = optparse.OptionParser()
    optparse_object.add_option("-i","--interface",dest="interface",help="İnterface to change.")
    optparse_object.add_option("-m", "--mac", dest="mac_adress", help="Mac adress to change.")
    return optparse_object.parse_args()

def mac_changer(interface,mac_adress):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_adress])
    subprocess.call(["ifconfig", interface, "up"])

def mac_control(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))

    if (new_mac):
        return new_mac.group(0)
    else:
        return None

print(colored("THT Mac Changer Programina Hos Geldiniz! Mac Adresiniz Değiştiriliyor...","blue"))
time.sleep(2)

(user_input, arguments) = user_inputs()
mac_changer(user_input.interface,user_input.mac_adress)
final_mac = mac_control(str(user_input.interface))

if (final_mac == user_input.mac_adress):
    print(colored(f"""Mac adresiniz değişmiştir. 
Yeni mac adresiniz: {final_mac}""","blue"))
else:
    print("Error!")







