<img
  src="./static/img/b-logo.png"
  alt="Account Keeper"
  style="width: 100%"
/>

Proteja seu império digital com o **Account Keeper**, sua fortaleza de senhas pessoal. Construído para ser totalmente offline, este aplicativo desktop assegura que seus dados mais sensíveis fiquem armazenados exclusivamente na sua máquina, longe de qualquer vulnerabilidade da web.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)

![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bulma](https://img.shields.io/badge/bulma-00D0B1?style=for-the-badge&logo=bulma&logoColor=white)

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)

## 🖥️ Preparação do Ambiente

O ambiente ideal para a execução do sistema pode variar conforme as necessidades de cada pessoa. No geral, recomenda-se o uso de um computador ou notebook dedicado exclusivamente a essa finalidade ou, alternativamente, uma unidade de armazenamento dedicada, como um pendrive ou HD. Em qualquer caso, mantenha o dispositivo protegido contra quaisquer mãos que não sejam as suas.

## 🛠️ Instalação e Execução

Este projeto foi desenvolvido em **Python 3.12**. Certifique-se de ter essa versão instalada para garantir a compatibilidade.

Todos os comandos a seguir devem ser executados a partir da raiz do projeto.

### Sistemas Windows 🪟

O script de inicialização `run.bat` automatiza todo o processo, desde a criação do ambiente virtual até a execução do programa. Execute o seguinte comando no seu terminal e uma nova janela para a aplicação será aberta automaticamente:

```bash
run.bat
```

### Sistemas Linux 🐧, macOS 🍎 e Unix 🐚

Para estes sistemas, o script `run.sh` também se encarrega de todo o processo, criando o ambiente virtual e iniciando um servidor local.

Primeiro, conceda a permissão de execução ao script (você só precisa fazer isso uma única vez):

```bash
chmod +x ./run.sh
```

Em seguida, execute o script:

```bash
./run.sh
```

Após a execução, o servidor será iniciado. Você poderá acessá-lo em seu navegador no endereço `http://127.0.0.1:5000`.

Caso queira alterar a porta padrão (5000), crie um arquivo `.env` com base no `.env.example` e defina o valor da variável `PORT` com o número desejado (entre 1024 e 49151).

## 🧪 Cobertura de Testes

O projeto possui uma suíte de testes unitários para garantir a estabilidade e o correto funcionamento dos módulos de conta (_account_) e usuário (_user_). Para executá-lo, utilize o comando:

```bash
pytest
```

A execução dos testes cria um arquivo de banco de dados temporário no diretório `test/`, com o nome baseado na data atual. Para realizar a limpeza do ambiente, basta remover os arquivos `.sqlite3` gerados neste diretório.

## 🤝 Doação

Gostou do projeto e gostaria de apoiar financeiramente? Você pode contribuir via **PayPal** ou através do **Pix** — é só clicar em uma das opções abaixo:

[![PayPal](https://img.shields.io/badge/PayPal-Donate-1040C1?labelColor=121661&style=for-the-badge&logo=paypal&link=https://www.paypal.com/donate/?hosted_button_id=2P9HPGUP7Z43S)](https://www.paypal.com/donate/?hosted_button_id=2P9HPGUP7Z43S)
&nbsp;
[![Pix](https://img.shields.io/badge/Pix-Doar-FBB88A?labelColor=F26722&style=for-the-badge&logo=pix&logoColor=ffffff&link=https://tipa.ai/davidsantana06)](https://tipa.ai/davidsantana06)

Este e outros projetos disponíveis no meu perfil foram desenvolvidos de forma independente. Qualquer apoio para manter este propósito é mais do que bem-vindo! 💪

## ⚖️ Licença

Este repositório é licenciado sob a **Licença MIT**, permitindo o uso e a modificação do código conforme desejado. As imagens utilizadas neste projeto pertencem a diferentes fontes e estão sujeitas a outros tipos de licença.
