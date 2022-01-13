import subprocess


def veryfyImage():

    subprocess.run(["openssl", "dgst", "-verify", "pubkeyUSER-A.pem",
                    "-signature", "signiture.bin", "RSAhiddenOutVerify.txt"])

    print('\nThis file was definitely sent from USER-A: BOB')
# openssl dgst -verify pubkeyA.pem -signature signiture.bin RSAhiddenOutVerify.txt
