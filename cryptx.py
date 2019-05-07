import os
import sys
import base64
import time
import sys
import itertools
import threading
import requests
import subprocess as subp
import pyAesCrypt

R = '\033[91m'
G = '\033[92m'
B = '\033[94m'
C = '\033[96m'
W = '\033[97m'
Y = '\033[93m'
M = '\033[95m'
G = '\033[90m'

version = "1.1.0"

cls = lambda: os.system("clear")

def ex():
    print("\n" + Y + "[*] Exit...")
    exit()

def main_print():
    cls()
    print(W + r'''
#######################################
#    ____________  ______  ______     #
#   / ____/ __ \ \/ / __ \/_  __/  __ #
#  / /   / /_/ /\  / /_/ / / / | |/_/ #
# / /___/ _, _/ / / ____/ / / _>  <   #
# \____/_/ |_| /_/_/     /_/ /_/|_|   #
#                 v1.1.0 by AnonimFA  #
#######################################''')

def animate_en():
    print("")
    while done == False:
        sys.stdout.write(B + "\r[~] Encrypting    " + W)
        time.sleep(0.3)
        sys.stdout.write(B + "\r[~] Encrypting ." + W)
        time.sleep(0.3)
        sys.stdout.write(B + "\r[~] Encrypting .." + W)
        time.sleep(0.3)
        sys.stdout.write(B + "\r[~] Encrypting ..." + W)
        time.sleep(0.3)
    sys.stdout.write(Y + "\r[+] Encrypt compleated!" + W + "\n")

def animate_de():
    print("")
    while done == False:
        sys.stdout.write(B + "\r[~] Decrypting    " + W)
        time.sleep(0.3)
        sys.stdout.write(B + "\r[~] Decrypting ." + W)
        time.sleep(0.3)
        sys.stdout.write(B + "\r[~] Decrypting .." + W)
        time.sleep(0.3)
        sys.stdout.write(B + "\r[~] Decrypting ..." + W)
        time.sleep(0.3)
    sys.stdout.write(Y + "\r[+] Decrypt compleated!" + W + "\n")

def cheak():
    print("\n" + Y + "[*] Checking for updates...")
    update = requests.get("https://raw.githubusercontent.com/AnonimFA/CRYPTx/master/version", timeout = 5)
    update = update.text.split(' ')[1]
    update = update.strip()

    if version != update:
        ans = str(input("\n" + Y + "[+] The new version is avaliable! Update now? (y/n): " + W))

        if ans == "y":
            print("\n" + Y + "[*] Updating...")
            subp.check_output(["git", "reset", "--hard", "origin/master"])
            subp.check_output(["git", "pull"])
            print("\n" + G + "[+] Update compleated! Now installed version: " + W + update)
            ex()

        elif ans == "n":
            print("\n" + R + "[-] Update canceled!")
            time.sleep(3)
        else:
            print("\n" + B + "[~] Skipping...")
            time.sleep(3)
    else:
        print("\n" + W + "[+] Updates not found.")
        time.sleep(3)

try:
    main_print()
    print("\n" + Y + "[*] Checking internet connection...")
    try:
        requests.get("https://www.google.ru/", timeout = 5)
        cheak()
    except requests.ConnectionError:
        print("\n" + R + "[!] Error! No internet connection!")
        time.sleep(3)

    while True:

        main_print()
        print(Y + '''
    [1] Use BASE64
    [2] Use AES ''' + W + '''(safe)''' + Y + '''
    [3] Exit
    [4] Info''' + "\n")

        do = input(Y + "[*] Enter number of action: " + W)

        if do == "1":

            while True:
                main_print()
                print(Y + '''
    [1] BASE64 encryption
    [2] BASE64 decryption
    [3] Exit''' + "\n")

                do_base64 = input(Y + "[*] Enter number of action: " + W)

                if do_base64 == "1":

                    while True:
                        file = input("\n" + Y + "[*] Enter path/name of file to crypt: " + W)
                        filename, file_extension = os.path.splitext(file)

                        if file_extension == ".base64":
                            print("\n" + R + "[!] Error! This file allready crypted!")
                            continue

                        try:
                            with open(file, 'rb') as f:
                                cont = f.read()
                                f.close()
                                break

                        except FileNotFoundError:
                            print("\n" + R + "[!] This file is not exist!")
                            continue

                        except IsADirectoryError:
                            print("\n" + R + "[!] Error! " + file + " is a directory!")
                            continue

                    done = False
                    t = threading.Thread(target=animate_en)
                    t.start()

                    enc = base64.b64encode(cont)
                    time.sleep(5)

                    done = True

                    with open(file + ".base64", 'wb') as f:
                        f.write(enc)
                        f.close()

                    time.sleep(5)

                elif do_base64 == "2":

                    while True:
                        file = input("\n" + Y + "[*] Enter path/name of file to decrypt: " + W)

                        filename, file_extension = os.path.splitext(file)

                        try:
                            with open(file, 'rb') as f:
                                cont = f.read()
                                f.close()

                                if file_extension != ".base64":
                                    print("\n" + R + "[!] Error! This file is not crypted!")
                                    continue

                        except FileNotFoundError:
                            print("\n" + R + "[!] This file is not exist!")
                            continue

                        except IsADirectoryError:
                            print("\n" + R + "[!] Error! " + file + " is a directory!")
                            continue

                        done = False
                        t = threading.Thread(target=animate_de)
                        t.start()

                        dec = base64.b64decode(cont)
                        time.sleep(5)

                        done = True

                        parts = file.rsplit('.', 1)
                        res = parts[0]

                        with open(res, 'wb') as f:
                            f.write(dec)
                            f.close()

                        time.sleep(5)

                elif do_base64 == "3":
                    break

        elif do == "2":
            while True:

                main_print()
                print(Y + '''
    [1] AES encryption
    [2] AES decryption
    [3] Exit''' + "\n")

                do_aes = input(Y + "[*] Enter number of action: " + W)

                if do_aes == "1":

                    while True:

                        file = input("\n" + Y + "[*] Enter path/name of file to crypt: " + W)
                        filename, file_extension = os.path.splitext(file)

                        try:
                            with open(file, 'rb') as f:
                                test = f.read()
                                f.close()

                                if file_extension == ".aes":
                                    print("\n" + R + "[!] Error! This file allredy crypted!")
                                    continue

                        except FileNotFoundError:
                            print("\n" + R + "[!] This file is not exist!")
                            continue

                        except IsADirectoryError:
                            print("\n" + R + "[!] Error! " + file + " is a directory!")
                            continue

                        password = input("\n" + Y + "[*] Enter the password: " + W)
                        bufSize = 64*1024

                        done = False
                        t = threading.Thread(target=animate_en)
                        t.start()

                        pyAesCrypt.encryptFile(str(file), str(file) + ".aes", str(password), bufSize)

                        time.sleep(5)

                        done = True
                        time.sleep(5)
                        break

                elif do_aes == "2":

                    while True:

                        file = input("\n" + Y + "[*] Enter path/name of file to decrypt: " + W)
                        filename, file_extension = os.path.splitext(file)

                        try:
                            with open(file, 'rb') as f:
                                test = f.read()
                                f.close()

                                if file_extension != ".aes":
                                    print("\n" + R + "[!] Error! This file is not crypted!")
                                    continue

                        except FileNotFoundError:
                            print("\n" + R + "[!] This file is not exist!")
                            continue

                        except IsADirectoryError:
                            print("\n" + R + "[!] Error! " + file + " is a directory!")
                            continue

                        while True:

                            password = input("\n" + Y + "[*] Enter the password: " + W)
                            bufSize = 64*1024

                            try:
                                pyAesCrypt.decryptFile(str(file), str(filename), str(password), bufSize)
                            except ValueError:
                                print("\n" + R + "[!] Error! Incorrect password!")
                                continue

                            done = False
                            t = threading.Thread(target=animate_de)
                            t.start()

                            done = True
                            time.sleep(5)
                            break
                        break

                elif do_aes == "3":
                    break

        elif do == "3":
            ex()

        elif do == "4":
            print(W + '''
Powered by AnonimFA
    https://github.com/AnonimFA
- CRYPTx v1.1.0
- Any news:
    *Added AES crypting
    *Fixed some bugs
    *Crypted file allready exist error deleted

''')
            continue

except KeyboardInterrupt:
    print("\n\n" + R + "[!] Error! Keyboard interrupt!")
    exit()
