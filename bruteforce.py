'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile, BadZipFile

# Use a method to attempt to extract the zip file with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except(RuntimeError, BadZipFile):
        return False


    



def main():
    print("[+] Beginning bruteforce ")
    attempts = 0
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
                        for line in f:
                            password = line.strip()
                            attempts += 1

                            if attempts % 1000 == 0:
                                print(f"[*] tried {attempts} passwords")
                            if  attempt_extract(zf, password):
                                 print(f"\n [+] Password Found: {password.decode()}")
                                 print(f"\n [+] Tried {attempts} attempts")
                                 return
    
                                 

                            

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()