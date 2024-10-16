# ControleApp

ControleApp é uma aplicação desktop desenvolvida em Python com a biblioteca PyQt5. Seu propósito é gerenciar e registrar dados de especialidades e avaliações de profissionais de saúde. A aplicação inclui funcionalidades para visualização de dados, exportação e geração de gráficos, além de várias opções de manipulação de arquivos e dados.

## Requisitos

## Para rodar o projeto, é necessário ter as seguintes dependências instaladas:

- Python 3.x
- PyQt5
- Matplotlib
- Pandas

## Você pode instalar todas as dependências via `pip` com o seguinte comando:
pip install PyQt5 matplotlib pandas

Gerar o Executável
Para gerar um executável da aplicação (sem a necessidade de Python instalado para o usuário final), você pode utilizar o PyInstaller. Siga os passos abaixo:

## Certifique-se de ter o PyInstaller instalado:

pip install pyinstaller
No diretório do projeto, execute o seguinte comando para gerar o executável:
pyinstaller --onefile --windowed controleapp.py

O argumento --onefile garante que tudo seja compactado em um único executável.
O argumento --windowed (ou -w) oculta o terminal ao iniciar o aplicativo (importante para aplicações com interface gráfica).
O executável será gerado na pasta dist. Você pode distribuí-lo como um arquivo independente para outras pessoas, sem que elas precisem instalar Python.

# Funcionalidades Principais
Gerenciamento de Especialidades e Avaliações: Registra e exibe especialidades e suas avaliações correspondentes. As especialidades incluem Geral, Psicologia, Fonoaudiologia, Terapia Ocupacional, Fisioterapia, e Psicopedagogia.

Interface Gráfica com PyQt5: A interface permite a interação amigável com as funcionalidades do sistema, incluindo a inserção e visualização de dados através de formulários e tabelas.

Exportação para Excel: A aplicação permite exportar os dados registrados para um arquivo Excel.

Geração de Gráficos: Utilizando a biblioteca matplotlib, o sistema gera gráficos para visualização de tendências e dados registrados.

Gerenciamento de Arquivos JSON: O sistema carrega e salva os dados localmente em arquivos JSON, o que facilita a persistência e manipulação offline dos dados.

# Estrutura do Projeto
### controleapp.py: Arquivo principal contendo toda a lógica da aplicação e a interface gráfica.

### dados.json: Arquivo JSON onde os dados inseridos na aplicação são salvos.

## Execução sem gerar o executavel
Clone o repositório para a sua máquina local:
git clone https://github.com/seu-usuario/controleapp.git

cd controleapp
## Execute o arquivo principal da aplicação:
python controleapp.py
## Isso abrirá a interface gráfica do ControleApp.

