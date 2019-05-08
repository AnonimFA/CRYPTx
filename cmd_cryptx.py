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

version = "1.1.2"

cls = lambda: os.system("cls")

def ex():
    print("\n" + "[*] Exit...")
    exit()

def main_print():
    cls()
    print(r'''
#######################################
#    ____________  ______  ______     #
#   / ____/ __ \ \/ / __ \/_  __/  __ #
#  / /   / /_/ /\  / /_/ / / / | |/_/ #
# / /___/ _, _/ / / ____/ / / _>  <   #
# \____/_/ |_| /_/_/     /_/ /_/|_|   #
#                 v1.1.2 by AnonimFA  #
#######################################''')

def animate_en():
    print("")
    while done == False:
        sys.stdout.write("\r[~] Encrypting    ")
        time.sleep(0.3)
        sys.stdout.write("\r[~] Encrypting .")
        time.sleep(0.3)
        sys.stdout.write("\r[~] Encrypting ..")
        time.sleep(0.3)
        sys.stdout.write("\r[~] Encrypting ...")
        time.sleep(0.3)
    sys.stdout.write("\r[+] Encrypt compleated!" + "\n")

def animate_de():
    print("")
    while done == False:
        sys.stdout.write("\r[~] Decrypting    ")
        time.sleep(0.3)
        sys.stdout.write("\r[~] Decrypting .")
        time.sleep(0.3)
        sys.stdout.write("\r[~] Decrypting ..")
        time.sleep(0.3)
        sys.stdout.write("\r[~] Decrypting ...")
        time.sleep(0.3)
    sys.stdout.write("\r[+] Decrypt compleated!" + "\n")

def cheak():
    print("\n" + "[*] Checking for updates...")
    update = requests.get("https://raw.githubusercontent.com/AnonimFA/CRYPTx/master/version", timeout = 5)
    update = update.text.split(' ')[1]
    update = update.strip()

    if version != update:
        ans = str(input("\n" + "[+] The new version is avaliable! Update now? (y/n): "))

        if ans == "y":
            print("\n" + "[*] Updating...")
            subp.check_output(["git", "reset", "--hard", "origin/master"])
            subp.check_output(["git", "pull"])
            print("\n" + "[+] Update compleated! Now installed version: " + update)
            ex()

        elif ans == "n":
            print("\n" + "[-] Update canceled!")
            time.sleep(3)
        else:
            print("\n" + "[~] Skipping...")
            time.sleep(3)
    else:
        print("\n" + "[+] Updates not found.")
        time.sleep(3)

try:
    main_print()
    print("\n" + "[*] Checking internet connection...")
    try:
        requests.get("https://www.google.ru/", timeout = 5)
        cheak()
    except requests.ConnectionError:
        print("\n" + "[!] Error! No internet connection!")
        time.sleep(3)

    while True:

        main_print()
        print('''
    [1] Use BASE64
    [2] Use AES (safe)
    [3] Exit
    [4] Info''' + "\n")

        do = input("[*] Enter number of action: ")

        if do == "1":

            while True:
                main_print()
                print('''
    [1] BASE64 encryption
    [2] BASE64 decryption
    [3] Exit''' + "\n")

                do_base64 = input("[*] Enter number of action: ")

                if do_base64 == "1":

                    while True:
                        file = input("\n" + "[*] Enter path/name of file to crypt: ")
                        filename, file_extension = os.path.splitext(file)

                        if file_extension == ".base64":
                            print("\n" + "[!] Error! This file allready crypted!")
                            continue

                        try:
                            with open(file, 'rb') as f:
                                cont = f.read()
                                f.close()
                                break

                        except FileNotFoundError:
                            print("\n" + "[!] This file is not exist!")
                            continue

                        except IsADirectoryError:
                            print("\n" + "[!] Error! " + file + " is a directory!")
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
                        file = input("\n" + "[*] Enter path/name of file to decrypt: ")

                        filename, file_extension = os.path.splitext(file)

                        try:
                            with open(file, 'rb') as f:
                                cont = f.read()
                                f.close()

                                if file_extension != ".base64":
                                    print("\n" + "[!] Error! This file is not crypted!")
                                    continue

                        except FileNotFoundError:
                            print("\n" + "[!] This file is not exist!")
                            continue

                        except IsADirectoryError:
                            print("\n" + "[!] Error! " + file + " is a directory!")
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
                print('''
    [1] AES encryption
    [2] AES decryption
    [3] Exit''' + "\n")

                do_aes = input("[*] Enter number of action: ")

                if do_aes == "1":

                    while True:

                        file = input("\n" + "[*] Enter path/name of file to crypt: ")
                        filename, file_extension = os.path.splitext(file)

                        try:
                            with open(file, 'rb') as f:
                                test = f.read()
                                f.close()

                                if file_extension == ".aes":
                                    print("\n" + "[!] Error! This file allredy crypted!")
                                    continue

                        except FileNotFoundError:
                            print("\n" + "[!] This file is not exist!")
                            continue

                        except IsADirectoryError:
                            print("\n" + "[!] Error! " + file + " is a directory!")
                            continue

                        password = input("\n" + "[*] Enter the password: ")
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

                        file = input("\n" + "[*] Enter path/name of file to decrypt: ")
                        filename, file_extension = os.path.splitext(file)

                        try:
                            with open(file, 'rb') as f:
                                test = f.read()
                                f.close()

                                if file_extension != ".aes":
                                    print("\n" + "[!] Error! This file is not crypted!")
                                    continue

                        except FileNotFoundError:
                            print("\n" + "[!] This file is not exist!")
                            continue

                        except IsADirectoryError:
                            print("\n" + "[!] Error! " + file + " is a directory!")
                            continue

                        while True:

                            password = input("\n" + "[*] Enter the password: ")
                            bufSize = 64*1024

                            try:
                                pyAesCrypt.decryptFile(str(file), str(filename), str(password), bufSize)
                            except ValueError:
                                print("\n" + "[!] Error! Incorrect password!")
                                continue

                            done = False
                            t = threading.Thread(target=animate_de)
                            t.start()
                            time.sleep(5)
                            done = True
                            time.sleep(5)
                            break
                        break

                elif do_aes == "3":
                    break

        elif do == "3":
            ex()

        elif do == "4":
            print('''
Powered by AnonimFA
    https://github.com/AnonimFA
- CRYPTx v1.1.2
- Any news:
    *No changed
    *Now CRYPTx have adaptation for Windows Command Line Interpreter
''')
            time.sleep(10)
            continue

except KeyboardInterrupt:
    print("\n\n" + "[!] Error! Keyboard interrupt!")
    exit()
