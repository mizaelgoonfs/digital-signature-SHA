# Assinatura Digital com SHA

Implementação de um programa de assinatura digital com o algoritmo de hash - [SHA](https://pt.wikipedia.org/wiki/Secure_Hash_Algorithms). O programa permite criar um par de chaves no padrão [OpenSSL](https://pt.wikipedia.org/wiki/OpenSSL) com o algoritmo [RSA](https://pt.wikipedia.org/wiki/RSA_(sistema_criptogr%C3%A1fico)); permite assinar um arquivo texto com a versão do algoritmo SHA desejada dentre as opções disponíves. Por fim, também é possível verificar se a assinatura de um arquivo é válida ou não.

Desenvolvido utilizando a linguagem Python.

## Guia para execução

#### 0. Antes de tudo, faça a instalação da biblioteca `pycryptodome`:

  ~~~

  > pip install pycryptodome

  ~~~

#### 1. Na pasta principal, cole seu arquivo de teste com o texto claro de entrada. No atual repositório, o arquivo de teste é o `text.txt`.
<br>

#### 2. Execute o programa principal com `python main.py`.

* O arquivo `main.py` contém o MENU principal do programa.
* O arquivo `utility_functions.py` contém as funções de assinatura, hash, verificação, dentre outras auxiliares.
<br>

#### 3. Ao escolher a opção 1 do MENU principal:

* O programa gera um par de chaves e gera os respectivos arquivos, com a extensão .pem: `private_key.pem` e `public_key.pem`.
<br>

#### 4. Ao escolher a opção 2 do MENU principal:

* O programa pede que o usuário insira no teclado o nome do arquivo de entrada que contém o texto claro (*incluindo a extensão*);
* Logo após, o programa pede que o usuário digite o nome do arquivo que contém a chave privada (*incluindo a extensão .pem*);
* No próximo passo, o programa pede que o usuário escolha a opção correspondente à versão do SHA disponível;
* Por fim, o programa solicita ao usuário o nome do arquivo que será gerado com a assinatura (*pode incluir extensão ou não, a critério do usuário*).
<br>

#### 5. Ao escolher a opção 3 do MENU principal:

* O programa pede que o usuário insira no teclado o nome do arquivo de entrada que contém o texto claro (*incluindo a extensão*);
* Logo após, o programa pede que o usuário insira o nome do arquivo que está assinado (*incluindo a extensão, se houver*);
* Em seguida, o programa pede que o usuário digite o nome do arquivo que contém a chave pública (*incluindo a extensão .pem*);
* No próximo passo, o programa pede que o usuário escolha a opção correspondente à versão do SHA disponível (*e que foi utilizada no momento da assinatura do arquivo assinado em questão*);
* Por fim, o programa informa: **ASSINATURA VÁLIDA** ou **INVÁLIDA!**.
<br>
