# 🧠 AutoTask v2.0 — Automação de Cadastro com Selenium

Automatizador de cadastro de produtos no site de testes da Hashtag Treinamentos usando Python + Selenium.
Desenvolvido com foco em aprendizado, testes e boas práticas.

> 🔄 Esta é a **versão 2.0**, completamente reformulada, mais estável e escalável.

---

## 🚀 O que há de novo na v2.0?

| 💡 Melhorias           | Descrição                                                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| ⌨️ Envio com ENTER     | Substituímos o clique no botão `submit` pelo envio da tecla `ENTER`, reduzindo erros de elemento ausente.               |
| 🕵️‍♂️ WebDriverWait       | Adição de `esperar_elemento()` com `WebDriverWait` para garantir que os campos estejam visíveis antes do preenchimento. |
| 🧼 Tratamento de `NaN` | Agora campos vazios (como observações) são tratados e não causam preenchimento incorreto com “nan”.                     |
| 🧪 Código modularizado | Separação clara por módulos: leitura de CSV, login, navegador, preenchimento e utilidades.                              |
| 🧯 Fluxo mais estável  | Redução de falhas inesperadas, execução mais fluida e menor necessidade de delays arbitrários.                          |

---

## 📁 Estrutura do Projeto

```
AutoTask/
├── main.py                   # Arquivo principal
├── README.md                 # Documentação
├── requirements.txt          # Bibliotecas necessárias
├── .gitignore                # Arquivos ignorados no Git
├── pegar_posicao.py         # Auxiliar para debug de posição na tela
│
├── assets/                  # Imagens usadas para login com PyAutoGUI (caso necessário)
│   ├── botao_logar.png
│   └── campo_email.png
│
├── modules/                 # Código modularizado
│   ├── abrir_navegador.py
│   ├── fazer_login.py
│   ├── leitura_csv.py
│   ├── preenchimento_form.py
│   └── utils.py
│
└── src/
    └── data/
        └── produtos.csv     # Fonte de dados para cadastro
```

---

## 🧠 Funcionalidades

- Abertura automática do navegador
- Login automático com email e senha
- Leitura de arquivo .csv com os produtos
- Preenchimento de formulário com espera dinâmica
- Envio usando Enter, sem clicar no botão
- Modularização e escalabilidade

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Selenium 4](https://pypi.org/project/selenium/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)
- Pandas
- Google Chrome + ChromeDriver

---

## 🧪 Como Usar

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/AutoTask.git
cd AutoTask
```

2. **Instale as dependências**

```bash
pip install -r requirements.txt
```

3. **Adicione seus produtos no arquivo**

```bash
src/data/produtos.csv
```

> ⚠️ Certifique-se que os nomes das colunas estejam corretos: codigo, marca, tipo, categoria, preco_unitario, custo, obs. 5. **Execute o projeto**

```bash
python main.py
```

---

## 📋 Exemplo de CSV aceito

| codigo | marca  | tipo     | categoria | preco_unitario | custo  | obs            |
| ------ | ------ | -------- | --------- | -------------- | ------ | -------------- |
| 001    | Nike   | Tênis    | Calçados  | 199.99         | 120.00 | Modelo novo    |
| 002    | Adidas | Camiseta | Roupas    | 89.90          | 40.00  |                |
| 003    | Mizuno | Jaqueta  | Roupas    | 299.90         | 180.00 | À prova d'água |

---

## ✅ Requisitos

- Python 3.10+
- Navegador Chrome instalado
- Bibliotecas:
  - selenium
  - pandas
  -webdriver-manager

pandas

---

## 📌 Detalhes Técnicos

- **submit via ENTER**:
  O envio do formulário é feito com `Keys.ENTER`, evitando o erro `no such element: submit`.

- **esperar_elemento**:
  Função utilitária que aguarda a visibilidade do campo antes do preenchimento, evitando `ElementNotInteractableException`.

- **tratamento de nulos**:
  Campos com `NaN` do pandas são convertidos para `""` antes de preencher, garantindo que nada indevido vá pro formulário.

---

## 🙋‍♂️ Autor

Desenvolvido com 💻 por [Matheus Raimundo Santos](https://www.linkedin.com/in/odevmath/)

---

## 🏷️ Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
