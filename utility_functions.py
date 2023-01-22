from Crypto.Hash import SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto import Random

def openFile(fileName, mode):
    try:
        file = open(fileName, mode)
        content = file.read()
        # print(content)
        file.close()
        return content  # retorna o conteúdo completo do arquivo

    except:
        print('Erro na abertura do arquivo: ' + fileName)
        return

def generateFile(fileName, content, mode):
    with open(fileName, mode) as file:
        file.write(content)
        file.close()
    
def exportPrivateKey(privateKey):
    with open('private_key.pem','wb') as file:
        file.write(privateKey.export_key(format='PEM'))
        file.close()

def exportPublicKey(publicKey):
    with open('public_key.pem','wb') as file:
        file.write(publicKey.export_key(format='PEM'))
        file.close()

def generateKey():
    random_seed = Random.new().read

    keyPair = RSA.generate(1024, random_seed)
    publicKey = keyPair.publickey()

    exportPrivateKey(keyPair)
    exportPublicKey(publicKey)

    print("\nPAR DE CHAVES GERADO COM SUCESSO! (Verifique os arquivos de saída)\n")

def digitalSigner():
    fileNameClearText = input("Digite o nome do arquivo que contém o texto claro: ")
    clearText = openFile(fileNameClearText, 'r')

    fileNamePrivateKey = input("Digite o nome do arquivo que contém a chave privada (.pem): ")
    filePrivateKey = open(fileNamePrivateKey,'rb')
    keyPair = RSA.import_key(filePrivateKey.read())

    signer = pkcs1_15.new(keyPair) # Cria objeto de assinatura no Padrão RSA "PKCS#1" versão (1.5)

    hashA = hashAlgorithm(clearText)

    digitalSignText = signer.sign(hashA)

    fileNameDigitalSign = input("Digite o nome do arquivo que sairá com a assinatura: ")
    generateFile(fileNameDigitalSign, digitalSignText, "wb")

    # print("Digital signature:\n" + repr(digitalSignText)+"\n")
    print("\nARQUIVO ASSINADO E GERADO COM SUCESSO! (Verifique o arquivo de saída)\n")

def hashText(SHAversion, clearText):
    hash_hex = SHAversion.new(clearText.encode()).hexdigest()
    # print("Hash em hexadecimal:" + repr(hash_hex) + "\n")
    hash = SHAversion.new(hash_hex.encode())

    return hash

def hashAlgorithm(clearText):
    option = 1
    while(True):
        print("\nMENU de Versões do SHA: \n")
        print("\nFamília SHA-2:\n")
        print(" 1 - SHA-224\n 2 - SHA-256\n 3 - SHA-384\n 4 - SHA-512\n")
        print("Família SHA-3:\n")
        print(" 5 - SHA3-224\n 6 - SHA3-256\n 7 - SHA3-384\n 8 - SHA3-512\n")

        option = input("Digite o número correspondente à opção do SHA: ")

        if option == "1":
            hash = hashText(SHA224, clearText)
            break
        elif option == "2":
            hash = hashText(SHA256, clearText)
            break
        elif option == "3":
            hash = hashText(SHA384, clearText)
            break
        elif option == "4":
            hash = hashText(SHA512, clearText)
            break
        elif option == "5":
            hash = hashText(SHA3_224, clearText)
            break
        elif option == "6":
            hash = hashText(SHA3_256, clearText)
            break
        elif option == "7":
            hash = hashText(SHA3_384, clearText)
            break
        elif option == "8":
            hash = hashText(SHA3_512, clearText)
            break
        else:
            print("Opção inválida!")

    return hash

def verifyDigitalSign():
    fileNameClearText = input("Digite o nome do arquivo que contém o texto claro: ")
    clearText = openFile(fileNameClearText, 'r')

    fileNameDigitalSign = input("Digite o nome do arquivo que contém a assinatura: ")
    digitalSignFile = openFile(fileNameDigitalSign, "rb")
    # print("Digital signature:\n" + repr(digitalSignFile)+"\n")

    fileNamePublicKey = input("Digite o nome do arquivo que contém a chave pública (.pem): ")
    publicKeyFile = open(fileNamePublicKey, 'rb')
    publicKey = RSA.import_key(publicKeyFile.read())

    hashB = hashAlgorithm(clearText)

    verifier = pkcs1_15.new(publicKey) # Cria objeto de assinatura no Padrão RSA "PKCS#1" versão (1.5)
    try:
        verifier.verify(hashB, digitalSignFile)
        print("ASSINATURA VÁLIDA!")
    except:
        print("ASSINATURA INVÁLIDA!")