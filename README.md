<img
  src="./resource/static/img/b-logo.png"
  alt="Account Keeper"
  style="width: 100%"
/>

**Account Keeper** é um aplicativo desktop totalmente offline, desenvolvido para oferecer segurança e praticidade no gerenciamento de contas e senhas. Inspirado na Antiga Roma, sua interface traz ilustrações e referências históricas, proporcionando uma experiência imersiva.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)

![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bulma](https://img.shields.io/badge/bulma-00D0B1?style=for-the-badge&logo=bulma&logoColor=white)

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### 🖥️ Preparação do Ambiente

O ambiente ideal para a execução do sistema pode variar conforme as necessidades de cada pessoa. No geral, recomenda-se o uso de um computador ou notebook dedicado exclusivamente a essa finalidade ou, alternativamente, uma unidade de armazenamento dedicada, como um pendrive ou HD. Em qualquer caso, mantenha o dispositivo protegido contra quaisquer mãos que não sejam as suas.

### 🛠️ Instalação e Execução

A aplicação foi desenvolvida em **Python 3.12**, recomendando-se o uso dessa versão para garantir compatibilidade. Para instalar as dependências e executar, utilize os comandos abaixo no diretório raiz do projeto:

```bash
pip install -r requirements.txt
python -m app
```

### 🧪 Cobertura de Testes

Foram desenvolvidos testes unitários para validar os serviços oferecidos pelos módulos de conta (_account_) e usuário (_user_). Para executá-los, utilize o seguinte comando:

```bash
pytest
```

Durante a execução, um arquivo de banco de dados será criado no diretório `test/`, nomeado conforme a data e hora de início, seguido da extensão `.sqlite3`.

### ⚖️ Licença

Este repositório é licenciado sob a **Licença MIT**, permitindo o uso e a modificação do código conforme desejado. As imagens utilizadas neste projeto pertencem a diferentes fontes e estão sujeitas a outros tipos de licença.
