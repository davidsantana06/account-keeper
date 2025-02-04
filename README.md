<img src="./resource/static/img/b-logo.png" alt="Account Keeper" style="width: 100%">

<b>Account Keeper</b> é um aplicativo desktop totalmente offline, desenvolvido para oferecer segurança e praticidade no gerenciamento de contas e senhas. Inspirado na Antiga Roma, sua interface traz ilustrações e referências históricas, proporcionando uma experiência imersiva.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bulma](https://img.shields.io/badge/bulma-00D0B1?style=for-the-badge&logo=bulma&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### 🖥️ Preparação do Ambiente

O ambiente ideal para a execução do sistema pode variar conforme as necessidades de cada pessoa. No geral, recomenda-se o uso de um computador ou notebook dedicado exclusivamente a essa finalidade ou, alternativamente, uma unidade de armazenamento dedicada, como um pendrive ou HD. Em qualquer caso, mantenha o dispositivo protegido contra quaisquer mãos que não sejam as suas.

Caso utilize uma unidade de armazenamento dedicada e queira protegê-la com senha, você pode usar o [**🔗 VeraCrypt**](https://www.veracrypt.fr/code/VeraCrypt/), um software que cria volumes criptografados, disponível para Windows, Linux e Mac.

### 🛠️ Instalação e Execução

A aplicação foi desenvolvida em **Python 3.12**, sendo recomendada a utilização dessa versão para garantir compatibilidade.

#### 1️⃣ Clonar o Repositório

Será necessário adquirir uma cópia local do código-fonte, que pode ser obtida com o seguinte comando:

```bash
git clone https://github.com/davidsantana06/account-keeper
```

#### 2️⃣ Instalar as Dependências

No diretório da aplicação, instale as dependências utilizando o `pip`:

```bash
pip install -r requirements.txt
```

#### 3️⃣ Executar

Após concluir as etapas anteriores, você poderá inicializar a aplicação com o comando:

```bash
python -m app
```

### 🔄 Migrações

Se você estiver utilizando a aplicação e deseja atualizá-la sem perder seus dados, será necessário aplicar as migrações do banco de dados. Para isso, execute o seguinte comando:

```bash
flask db upgrade
```

Após a conclusão, basta iniciar a aplicação novamente.

### ⚖️ Licença

Este repositório é licenciado sob a **Licença MIT**, permitindo o uso e a modificação do código conforme desejado. As imagens utilizadas neste projeto pertencem a diferentes fontes e estão sujeitas a outros tipos de licença.
