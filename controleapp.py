
"""
ControleApp

Autor: João Guilherme Sauer Schlichting
GitHub: https://github.com/sauerlock/controleApp
Linkedin: https://www.linkedin.com/in/jo%C3%A3o-guilherme-sauer-schlichting-716767a1/

Data de criação: 01/10/2024
Descrição: Este código implementa uma aplicação PyQt5 para gerenciamento de especialidades e avaliações.

Licença: MIT License
Contato: joaosauer@outlook.com
"""



from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QTableWidget,
    QTableWidgetItem, QLineEdit, QComboBox, QFormLayout, QFileDialog, QMessageBox,
    QGroupBox, QHBoxLayout, QVBoxLayout, QLineEdit, QHeaderView
)
from PyQt5.QtCore import Qt
import sys
from datetime import datetime
import json
import matplotlib.pyplot as plt
import pandas as pd


import json
from datetime import datetime

class DataManager:
    def __init__(self):
        
        self.file_path = "dados.json"
        self.dados = {
            "especialidades": [
                "Geral", "Psicologia", "Fonoaudiologia", "Terapia Ocupacional", 
                "Fisioterapia", "Psicopedagogia"
            ],
            "avaliacoes": {
                "Geral": [
                    "Itens de Manutenção",
                    "DTT",
                    "Checklist",
                    "Primeira Resposta"
                ],
                "Psicologia": [
                    "Avaliação de barreiras", "Caderno Denver",
                    "Avaliação de Preferência indireta", "Anamnese Psico",
                    "VBMAPP gráfico", "Tabela ABC", "Check - List Socially Savvy"
                ],
                "Fonoaudiologia": [
                    "Teste de Reabilitação de Afasia", "Anamnese TEA",
                    "Anamnese de Linguagem", "Anamnese Neurofuncional",
                    "Apraxia da fala", "PECS IV e V", "PROC", "PAD PED",
                    "Caderno Confias", "Confias", "Pafi", "ADL", "MBGR",
                    "AFI", "Hierarquia motora de fala", "PITA", "AMIOFE",
                    "Sistema de observação e análise", "Inventário Fonético",
                    "Desenvolvimento de objetivos motores de fala", "Ecoico"
                ],
                "Terapia Ocupacional": [
                    "Anamnese TO", "Checklist AVD", "Checklist dinais de disfunções",
                    "Avaliação não estruturada de AVD", "Anamnese Bobath infantil",
                    "Anamnese Bobath adulto", "Perfil Sensorial (7 - 35 meses)",
                    "Perfil Sensorial (3 - 14 anos)", "Perfil Sensorial (nascimento até 6 meses)",
                    "Portage", "Seletividade alimentar", "PEDI",
                    "Perfil Sensorial do adulto/adolescente", "AVD vestir calça",
                    "AVD despir calça", "Folha de registro de base - desfralde",
                    "Folha de observações clínicas", "Folha de registro de base - desfralde - identificando frequência",
                    "MIF adulto", "Entrevista de desfralde e uso do vaso sanitário",
                    "Folha de motricidade fina infantil", "Wee Fim (MIF Infantil)",
                    "Folhas de anexo B - avaliação do comportamento alimentar", "SPM",
                    "Sinais que a criança quer ou vai fazer cocô", "Sinais que a criança quer ou vai fazer xixi",
                    "Folha de teste de atenção por cancelamento", "Avaliação de hábitos alimentares",
                    "Anexo 1 - escala labirinto de avaliação do comportamento alimentar", "COPM",
                    "AVD em branco", "AVD e AVP", "Triagem alimentar"
                ],
                "Fisioterapia": [
                    "MFM - 20", "GMFM", "Gaiola Spider", "Avaliação saúde da criança",
                    "Escala equilíbrio pediátrica", "Bateria Psicomotora", "Gráfico de desempenho",
                    "Manobras deficit", "DCDQ", "Best Test", "Berg", "Gás",
                    "ASIA", "Alberta", "Ashworth (tônus)", "Anamnese", "Tônus",
                    "Análise do movimento", "Goniometria", "Reflexos", "FM",
                    "Inspeção", "Sensibilidade", "Locomoção/estabilidade", "Reações posturais",
                    "Roteiro Neuro Adulto", "Questionário de coordenação", "MFIS",
                    "Meta Smart", "Força muscular", "Coordenação"
                ],
                "Psicopedagogia": [
                    "Anamnese Psicopedagogia", "Folha de dados", "Psicomotricidade relacional",
                    "Prova de Conservação", "Teste infantil de nomeação", "IAR",
                    "Teste de cancelamento", "Prova aritmética", "Teste de consciência fonológica",
                    "Teste de discriminação fonológica", "Provas pedagógicas", "Teste contrastivo",
                    "Prova piagetiana", "Trilhas AB", "Trilhas pré escolares",
                    "Registro de atividades Psicopedagogia", "Prontidão para alfabetização"
                ]
            },
            "estoque": {},
            "registros_entrada": [],
            "registros_saida": [],
            "terapeutas": ["Andreia Melo - Terapia Ocupacional",
                            "Andreza Casal - Fonoaudiologia",
                            "Ariadne Bedin Pallu - Terapia Ocupacional",
                            "Arthur Macedo - Psicologia",
                            "Barbara Cristina - Fisioterapia",
                            "Bet\u00e2nia Andrade - Psicopedagogia ",
                            "Bruna Betto - Terapia Ocupacional",
                            "Bruna Barros - Psicologia",
                            "Cacilda Garcia - Terapia Ocupacional",
                            "Carolina Machado - Terapia Ocupacional",
                            "Daniela Midori - Terapia Ocupacional",
                            "Darlene Campos - Psicologia"]
        }
        self.carregar_dados()

    def salvar_dados(self):
        """Salva os dados no arquivo JSON."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.dados, file, indent=4)
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")

    def carregar_dados(self):
        """Carrega os dados do arquivo JSON."""
        try:
            with open(self.file_path, 'r') as file:
                self.dados = json.load(file)
        except FileNotFoundError:
            self.salvar_dados()
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON. Usando dados padrão.")
        except Exception as e:
            print(f"Erro ao carregar os dados: {e}")

    def registrar_entrada(self, especialidade, avaliacao, quantidade):
        """Registra a entrada de uma avaliação no estoque."""
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        if avaliacao not in self.dados["estoque"]:
            self.dados["estoque"][avaliacao] = 0

        self.dados["estoque"][avaliacao] += quantidade
        self.dados["registros_entrada"].append({
            "especialidade": especialidade,
            "avaliacao": avaliacao,
            "quantidade": quantidade,
            "data_entrada": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.salvar_dados()

    def registrar_saida(self, terapeuta, paciente, especialidade, avaliacao, quantidade):
        """Registra a saída de uma avaliação e atualiza o estoque."""
        try:
            if quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero.")
            if avaliacao in self.dados["estoque"] and self.dados["estoque"][avaliacao] >= quantidade:
                self.dados["estoque"][avaliacao] -= quantidade
                self.dados["registros_saida"].append({
                    "terapeuta": terapeuta,
                    "paciente": paciente,
                    "especialidade": especialidade,
                    "avaliacao": avaliacao,
                    "quantidade": quantidade,
                    "data_saida": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                self.salvar_dados()
            else:
                raise ValueError("Estoque insuficiente ou avaliação não encontrada.")
        except Exception as e:
            raise ValueError(f"Erro ao registrar saída: {e}")

    def obter_especialidade_por_avaliacao(self, avaliacao):
        """Retorna a especialidade relacionada a uma avaliação."""
        for especialidade, avaliacoes in self.dados["avaliacoes"].items():
            if avaliacao in avaliacoes:
                return especialidade
        return ""

    def exportar_para_excel(self, caminho_arquivo):
        """Exporta os dados para um arquivo Excel."""
        try:
            import pandas as pd  # Importa pandas aqui para evitar erro se pandas não estiver instalado

            registros_saida = pd.DataFrame(self.dados["registros_saida"])
            registros_entrada = pd.DataFrame(self.dados["registros_entrada"])
            estoque = pd.DataFrame(list(self.dados["estoque"].items()), columns=['Avaliação', 'Quantidade'])

            with pd.ExcelWriter(caminho_arquivo) as writer:
                registros_saida.to_excel(writer, sheet_name='Saídas', index=False)
                registros_entrada.to_excel(writer, sheet_name='Entradas', index=False)
                estoque.to_excel(writer, sheet_name='Estoque', index=False)
        except Exception as e:
            raise ValueError(f"Erro ao exportar para Excel: {e}")

    def gerar_grafico(self, caminho_arquivo):
        """Gera um gráfico de barras das quantidades em estoque."""
        try:
            import matplotlib.pyplot as plt  # Importa matplotlib aqui para evitar erro se matplotlib não estiver instalado

            avaliacoes = list(self.dados["estoque"].keys())
            quantidades = list(self.dados["estoque"].values())

            plt.figure(figsize=(10, 6))
            plt.bar(avaliacoes, quantidades, color='skyblue')
            plt.xlabel('Avaliações')
            plt.ylabel('Quantidade em Estoque')
            plt.title('Quantidade em Estoque por Avaliação')
            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.savefig(caminho_arquivo)
            plt.close()
        except Exception as e:
            raise ValueError(f"Erro ao gerar gráfico: {e}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gestão de Avaliações')
        self.setGeometry(100, 100, 1200, 800)

        self.data_manager = DataManager()

        # Widgets de entrada
        self.input_entrada = QGroupBox("Adicionar Entrada")
        self.input_saida = QGroupBox("Adicionar Saída")

        # Formulários de entrada
        self.form_entrada = QFormLayout()
        self.entrada_especialidade = QComboBox()
        self.entrada_avaliacao = QComboBox()
        self.entrada_quantidade = QLineEdit()
        self.botao_adicionar_entrada = QPushButton("Adicionar Entrada")

        self.form_entrada.addRow("Especialidade:", self.entrada_especialidade)
        self.form_entrada.addRow("Avaliação:", self.entrada_avaliacao)
        self.form_entrada.addRow("Quantidade:", self.entrada_quantidade)
        self.form_entrada.addWidget(self.botao_adicionar_entrada)
        self.input_entrada.setLayout(self.form_entrada)

        # Formulários de saída
        self.form_saida = QFormLayout()
        self.saida_terapeuta = QComboBox()
        self.saida_paciente = QLineEdit()
        self.saida_especialidade = QComboBox()
        self.saida_avaliacao = QComboBox()
        self.saida_quantidade = QLineEdit()
        self.botao_adicionar_saida = QPushButton("Adicionar Saída")

        self.form_saida.addRow("Terapeuta:", self.saida_terapeuta)
        self.form_saida.addRow("Paciente:", self.saida_paciente)
        self.form_saida.addRow("Especialidade:", self.saida_especialidade)
        self.form_saida.addRow("Avaliação:", self.saida_avaliacao)
        self.form_saida.addRow("Quantidade:", self.saida_quantidade)
        self.form_saida.addWidget(self.botao_adicionar_saida)
        self.input_saida.setLayout(self.form_saida)

        # Tabelas
        self.tabela_entrada = QTableWidget()
        self.tabela_saida = QTableWidget()
        self.tabela_estoque = QTableWidget()

        # Configuração das tabelas
        self.configurar_tabela(self.tabela_entrada, ["Especialidade", "Avaliação", "Quantidade", "Data de Entrada"])
        self.configurar_tabela(self.tabela_saida, ["Terapeuta", "Paciente", "Especialidade", "Avaliação", "Quantidade", "Data de Saída"])
        self.configurar_tabela(self.tabela_estoque, ["Avaliação", "Quantidade"])

        # Funções de adicionar e remover terapeuta
        self.botao_adicionar_terapeuta = QPushButton("Adicionar Terapeuta")
        self.botao_remover_terapeuta = QPushButton("Remover Terapeuta")
        self.entrada_terapeuta = QLineEdit()

        # Layouts
        layout_main = QVBoxLayout()

        # Layout para Inputs de Entrada e Saída
        layout_inputs = QHBoxLayout()
        layout_inputs.addWidget(self.input_entrada)
        layout_inputs.addWidget(self.input_saida)

        # Layout para Tabelas (Entrada e Estoque lado a lado)
        layout_tabelas_superior = QHBoxLayout()
        
        layout_entrada = QVBoxLayout()
        layout_entrada.addWidget(QLabel("Tabela de Entrada"))
        layout_entrada.addWidget(self.tabela_entrada)

        layout_estoque = QVBoxLayout()
        layout_estoque.addWidget(QLabel("Tabela de Estoque"))
        layout_estoque.addWidget(self.tabela_estoque)

        layout_tabelas_superior.addLayout(layout_entrada)
        layout_tabelas_superior.addLayout(layout_estoque)

        # Layout para Tabela de Saída abaixo
        layout_tabelas_inferior = QVBoxLayout()
        layout_tabelas_inferior.addWidget(QLabel("Tabela de Saída"))
        layout_tabelas_inferior.addWidget(self.tabela_saida)

        # Layout para Funções de Terapeutas
        layout_terapeutas = QVBoxLayout()
        layout_terapeutas.addWidget(QLabel("Adicionar/Remover Terapeuta"))
        layout_terapeutas.addWidget(self.entrada_terapeuta)
        layout_terapeutas.addWidget(self.botao_adicionar_terapeuta)
        layout_terapeutas.addWidget(self.botao_remover_terapeuta)
        
        # Botão de Exportar Excel
        self.botao_exportar_excel = QPushButton("Exportar para Excel")
        layout_terapeutas.addWidget(self.botao_exportar_excel)

        # Adicionando os layouts ao layout principal
        layout_main.addLayout(layout_inputs)
        layout_main.addLayout(layout_tabelas_superior)
        layout_main.addLayout(layout_tabelas_inferior)
        layout_main.addLayout(layout_terapeutas)

        container = QWidget()
        container.setLayout(layout_main)
        self.setCentralWidget(container)

        # Conectar os botões aos slots
        self.botao_adicionar_entrada.clicked.connect(self.adicionar_entrada)
        self.botao_adicionar_saida.clicked.connect(self.adicionar_saida)
        self.botao_adicionar_terapeuta.clicked.connect(self.adicionar_terapeuta)
        self.botao_remover_terapeuta.clicked.connect(self.remover_terapeuta)
        self.botao_exportar_excel.clicked.connect(self.exportar_excel)

        self.atualizar_tabelas()
        self.carregar_dados_iniciais()

    def exportar_excel(self):
        """Exporta os dados para um arquivo Excel."""
        # Abre um diálogo para escolher o caminho do arquivo
        caminho_arquivo, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo como", "", "Excel Files (*.xlsx);;All Files (*)")
        if caminho_arquivo:
            try:
                # Chama a função de exportação do DataManager
                self.data_manager.exportar_para_excel(caminho_arquivo)
                QMessageBox.information(self, "Sucesso", "Dados exportados para Excel com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao exportar para Excel: {e}")
        

    def configurar_tabela(self, tabela, cabecalhos):
        """Configura as tabelas com os cabeçalhos especificados."""
        tabela.setColumnCount(len(cabecalhos))
        tabela.setHorizontalHeaderLabels(cabecalhos)
        tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        tabela.setSelectionBehavior(QTableWidget.SelectRows)

    def carregar_dados_iniciais(self):
        """Carrega as especialidades, avaliações e terapeutas nos comboboxes."""
        self.entrada_especialidade.addItems(self.data_manager.dados["especialidades"])
        self.saida_especialidade.addItems(self.data_manager.dados["especialidades"])
        self.saida_terapeuta.addItems(self.data_manager.dados["terapeutas"])
        self.atualizar_avaliacoes_entrada()
        self.atualizar_avaliacoes_saida()

        # Conectar o evento de mudança de especialidade
        self.entrada_especialidade.currentIndexChanged.connect(self.atualizar_avaliacoes_entrada)
        self.saida_especialidade.currentIndexChanged.connect(self.atualizar_avaliacoes_saida)

    def atualizar_avaliacoes_entrada(self):
        """Atualiza o combobox de avaliações com base na especialidade selecionada na entrada."""
        especialidade_selecionada = self.entrada_especialidade.currentText()
        self.entrada_avaliacao.clear()
        self.entrada_avaliacao.addItems(self.data_manager.dados["avaliacoes"].get(especialidade_selecionada, []))

    def atualizar_avaliacoes_saida(self):
        """Atualiza o combobox de avaliações com base na especialidade selecionada na saída."""
        especialidade_selecionada = self.saida_especialidade.currentText()
        self.saida_avaliacao.clear()
        self.saida_avaliacao.addItems(self.data_manager.dados["avaliacoes"].get(especialidade_selecionada, []))

    def adicionar_entrada(self):
        """Adiciona uma entrada de avaliação ao estoque."""
        try:
            especialidade = self.entrada_especialidade.currentText()
            avaliacao = self.entrada_avaliacao.currentText()
            quantidade = int(self.entrada_quantidade.text())

            self.data_manager.registrar_entrada(especialidade, avaliacao, quantidade)
            self.atualizar_tabelas()
            QMessageBox.information(self, "Sucesso", "Entrada registrada com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao adicionar entrada: {e}")

    def adicionar_saida(self):
        """Adiciona uma saída de avaliação e atualiza o estoque."""
        try:
            terapeuta = self.saida_terapeuta.currentText()
            paciente = self.saida_paciente.text()
            especialidade = self.saida_especialidade.currentText()
            avaliacao = self.saida_avaliacao.currentText()
            quantidade = int(self.saida_quantidade.text())

            self.data_manager.registrar_saida(terapeuta, paciente, especialidade, avaliacao, quantidade)
            self.atualizar_tabelas()
            QMessageBox.information(self, "Sucesso", "Saída registrada com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao adicionar saída: {e}")

    def atualizar_tabelas(self):
        """Atualiza as tabelas de entrada, saída e estoque com os dados mais recentes."""
        self.atualizar_tabela_entrada()
        self.atualizar_tabela_saida()
        self.atualizar_tabela_estoque()

    def atualizar_tabela_entrada(self):
        """Atualiza a tabela de registros de entrada com os dados mais recentes."""
        self.tabela_entrada.setRowCount(0)  # Limpa a tabela antes de atualizar
        for registro in self.data_manager.dados["registros_entrada"]:
            linha = self.tabela_entrada.rowCount()
            self.tabela_entrada.insertRow(linha)
            
            # Cria itens e centraliza o texto
            especialidade_item = QTableWidgetItem(registro["especialidade"])
            especialidade_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_entrada.setItem(linha, 0, especialidade_item)

            avaliacao_item = QTableWidgetItem(registro["avaliacao"])
            avaliacao_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_entrada.setItem(linha, 1, avaliacao_item)

            quantidade_item = QTableWidgetItem(str(registro["quantidade"]))
            quantidade_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_entrada.setItem(linha, 2, quantidade_item)

            data_item = QTableWidgetItem(registro["data_entrada"])
            data_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_entrada.setItem(linha, 3, data_item)

        # Expande as colunas para ocupar o espaço disponível
        self.tabela_entrada.horizontalHeader().setStretchLastSection(True)
        self.tabela_entrada.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def atualizar_tabela_saida(self):
        """Atualiza a tabela de registros de saída com os dados mais recentes."""
        self.tabela_saida.setRowCount(0)  # Limpa a tabela antes de atualizar
        for registro in self.data_manager.dados["registros_saida"]:
            linha = self.tabela_saida.rowCount()
            self.tabela_saida.insertRow(linha)
            
            # Cria itens e centraliza o texto
            terapeuta_item = QTableWidgetItem(registro["terapeuta"])
            self.tabela_saida.setItem(linha, 0, terapeuta_item)

            paciente_item = QTableWidgetItem(registro["paciente"])
            paciente_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_saida.setItem(linha, 1, paciente_item)

            especialidade_item = QTableWidgetItem(registro["especialidade"])
            especialidade_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_saida.setItem(linha, 2, especialidade_item)

            avaliacao_item = QTableWidgetItem(registro["avaliacao"])
            avaliacao_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_saida.setItem(linha, 3, avaliacao_item)

            quantidade_item = QTableWidgetItem(str(registro["quantidade"]))
            quantidade_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_saida.setItem(linha, 4, quantidade_item)

            data_item = QTableWidgetItem(registro["data_saida"])
            data_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_saida.setItem(linha, 5, data_item)

        # Expande as colunas para ocupar o espaço disponível
        self.tabela_saida.horizontalHeader().setStretchLastSection(True)
        self.tabela_saida.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def atualizar_tabela_estoque(self):
        """Atualiza a tabela de estoque com os dados mais recentes."""
        self.tabela_estoque.setRowCount(0)  # Limpa a tabela antes de atualizar
        for avaliacao, quantidade in self.data_manager.dados["estoque"].items():
            linha = self.tabela_estoque.rowCount()
            self.tabela_estoque.insertRow(linha)
            
            # Cria itens e centraliza o texto
            avaliacao_item = QTableWidgetItem(avaliacao)
            avaliacao_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_estoque.setItem(linha, 0, avaliacao_item)

            quantidade_item = QTableWidgetItem(str(quantidade))
            quantidade_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_estoque.setItem(linha, 1, quantidade_item)

        # Expande as colunas para ocupar o espaço disponível
        self.tabela_estoque.horizontalHeader().setStretchLastSection(True)
        self.tabela_estoque.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
    def adicionar_terapeuta(self):
        """Adiciona um novo terapeuta à lista de terapeutas."""
        terapeuta = self.entrada_terapeuta.text().strip()
        if terapeuta:
            self.data_manager.dados["terapeutas"].append(terapeuta)
            self.data_manager.salvar_dados()
            self.saida_terapeuta.addItem(terapeuta)
            QMessageBox.information(self, "Sucesso", "Terapeuta adicionado com sucesso!")
        else:
            QMessageBox.warning(self, "Atenção", "O nome do terapeuta não pode estar vazio.")

    def remover_terapeuta(self):
        """Remove o terapeuta selecionado da lista de terapeutas."""
        terapeuta = self.saida_terapeuta.currentText()
        if terapeuta:
            self.data_manager.dados["terapeutas"].remove(terapeuta)
            self.data_manager.salvar_dados()
            self.saida_terapeuta.removeItem(self.saida_terapeuta.currentIndex())
            QMessageBox.information(self, "Sucesso", "Terapeuta removido com sucesso!")
        else:
            QMessageBox.warning(self, "Atenção", "Nenhum terapeuta selecionado.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
=======
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QTableWidget,
    QTableWidgetItem, QLineEdit, QComboBox, QFormLayout, QFileDialog, QMessageBox,
    QGroupBox, QHBoxLayout, QVBoxLayout, QLineEdit, QHeaderView
)
from PyQt5.QtCore import Qt
import sys
from datetime import datetime
import json
import matplotlib.pyplot as plt
import pandas as pd


import json
from datetime import datetime

class DataManager:
    def __init__(self):
        
        self.file_path = "dados.json"
        self.dados = {
            "especialidades": [
                "Geral", "Psicologia", "Fonoaudiologia", "Terapia Ocupacional", 
                "Fisioterapia", "Psicopedagogia"
            ],
            "avaliacoes": {
                "Geral": [
                    "Itens de Manutenção",
                    "DTT",
                    "Checklist",
                    "Primeira Resposta"
                ],
                "Psicologia": [
                    "Avaliação de barreiras", "Caderno Denver",
                    "Avaliação de Preferência indireta", "Anamnese Psico",
                    "VBMAPP gráfico", "Tabela ABC", "Check - List Socially Savvy"
                ],
                "Fonoaudiologia": [
                    "Teste de Reabilitação de Afasia", "Anamnese TEA",
                    "Anamnese de Linguagem", "Anamnese Neurofuncional",
                    "Apraxia da fala", "PECS IV e V", "PROC", "PAD PED",
                    "Caderno Confias", "Confias", "Pafi", "ADL", "MBGR",
                    "AFI", "Hierarquia motora de fala", "PITA", "AMIOFE",
                    "Sistema de observação e análise", "Inventário Fonético",
                    "Desenvolvimento de objetivos motores de fala", "Ecoico"
                ],
                "Terapia Ocupacional": [
                    "Anamnese TO", "Checklist AVD", "Checklist dinais de disfunções",
                    "Avaliação não estruturada de AVD", "Anamnese Bobath infantil",
                    "Anamnese Bobath adulto", "Perfil Sensorial (7 - 35 meses)",
                    "Perfil Sensorial (3 - 14 anos)", "Perfil Sensorial (nascimento até 6 meses)",
                    "Portage", "Seletividade alimentar", "PEDI",
                    "Perfil Sensorial do adulto/adolescente", "AVD vestir calça",
                    "AVD despir calça", "Folha de registro de base - desfralde",
                    "Folha de observações clínicas", "Folha de registro de base - desfralde - identificando frequência",
                    "MIF adulto", "Entrevista de desfralde e uso do vaso sanitário",
                    "Folha de motricidade fina infantil", "Wee Fim (MIF Infantil)",
                    "Folhas de anexo B - avaliação do comportamento alimentar", "SPM",
                    "Sinais que a criança quer ou vai fazer cocô", "Sinais que a criança quer ou vai fazer xixi",
                    "Folha de teste de atenção por cancelamento", "Avaliação de hábitos alimentares",
                    "Anexo 1 - escala labirinto de avaliação do comportamento alimentar", "COPM",
                    "AVD em branco", "AVD e AVP", "Triagem alimentar"
                ],
                "Fisioterapia": [
                    "MFM - 20", "GMFM", "Gaiola Spider", "Avaliação saúde da criança",
                    "Escala equilíbrio pediátrica", "Bateria Psicomotora", "Gráfico de desempenho",
                    "Manobras deficit", "DCDQ", "Best Test", "Berg", "Gás",
                    "ASIA", "Alberta", "Ashworth (tônus)", "Anamnese", "Tônus",
                    "Análise do movimento", "Goniometria", "Reflexos", "FM",
                    "Inspeção", "Sensibilidade", "Locomoção/estabilidade", "Reações posturais",
                    "Roteiro Neuro Adulto", "Questionário de coordenação", "MFIS",
                    "Meta Smart", "Força muscular", "Coordenação"
                ],
                "Psicopedagogia": [
                    "Anamnese Psicopedagogia", "Folha de dados", "Psicomotricidade relacional",
                    "Prova de Conservação", "Teste infantil de nomeação", "IAR",
                    "Teste de cancelamento", "Prova aritmética", "Teste de consciência fonológica",
                    "Teste de discriminação fonológica", "Provas pedagógicas", "Teste contrastivo",
                    "Prova piagetiana", "Trilhas AB", "Trilhas pré escolares",
                    "Registro de atividades Psicopedagogia", "Prontidão para alfabetização"
                ]
            },
            "estoque": {},
            "registros_entrada": [],
            "registros_saida": [],
            "terapeutas": ["Andreia Melo - Terapia Ocupacional",
                            "Andreza Casal - Fonoaudiologia",
                            "Ariadne Bedin Pallu - Terapia Ocupacional",
                            "Arthur Macedo - Psicologia",
                            "Barbara Cristina - Fisioterapia",
                            "Bet\u00e2nia Andrade - Psicopedagogia ",
                            "Bruna Betto - Terapia Ocupacional",
                            "Bruna Barros - Psicologia",
                            "Cacilda Garcia - Terapia Ocupacional",
                            "Carolina Machado - Terapia Ocupacional",
                            "Daniela Midori - Terapia Ocupacional",
                            "Darlene Campos - Psicologia"]
        }
        self.carregar_dados()

    def salvar_dados(self):
        """Salva os dados no arquivo JSON."""
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.dados, file, indent=4)
        except Exception as e:
            print(f"Erro ao salvar os dados: {e}")

    def carregar_dados(self):
        """Carrega os dados do arquivo JSON."""
        try:
            with open(self.file_path, 'r') as file:
                self.dados = json.load(file)
        except FileNotFoundError:
            self.salvar_dados()
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo JSON. Usando dados padrão.")
        except Exception as e:
            print(f"Erro ao carregar os dados: {e}")

    def registrar_entrada(self, especialidade, avaliacao, quantidade):
        """Registra a entrada de uma avaliação no estoque."""
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        if avaliacao not in self.dados["estoque"]:
            self.dados["estoque"][avaliacao] = 0

        self.dados["estoque"][avaliacao] += quantidade
        self.dados["registros_entrada"].append({
            "especialidade": especialidade,
            "avaliacao": avaliacao,
            "quantidade": quantidade,
            "data_entrada": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.salvar_dados()

    def registrar_saida(self, terapeuta, paciente, especialidade, avaliacao, quantidade):
        """Registra a saída de uma avaliação e atualiza o estoque."""
        try:
            if quantidade <= 0:
                raise ValueError("A quantidade deve ser maior que zero.")
            if avaliacao in self.dados["estoque"] and self.dados["estoque"][avaliacao] >= quantidade:
                self.dados["estoque"][avaliacao] -= quantidade
                self.dados["registros_saida"].append({
                    "terapeuta": terapeuta,
                    "paciente": paciente,
                    "especialidade": especialidade,
                    "avaliacao": avaliacao,
                    "quantidade": quantidade,
                    "data_saida": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                self.salvar_dados()
            else:
                raise ValueError("Estoque insuficiente ou avaliação não encontrada.")
        except Exception as e:
            raise ValueError(f"Erro ao registrar saída: {e}")

    def obter_especialidade_por_avaliacao(self, avaliacao):
        """Retorna a especialidade relacionada a uma avaliação."""
        for especialidade, avaliacoes in self.dados["avaliacoes"].items():
            if avaliacao in avaliacoes:
                return especialidade
        return ""

    def exportar_para_excel(self, caminho_arquivo):
        """Exporta os dados para um arquivo Excel."""
        try:
            import pandas as pd  # Importa pandas aqui para evitar erro se pandas não estiver instalado

            registros_saida = pd.DataFrame(self.dados["registros_saida"])
            registros_entrada = pd.DataFrame(self.dados["registros_entrada"])
            estoque = pd.DataFrame(list(self.dados["estoque"].items()), columns=['Avaliação', 'Quantidade'])

            with pd.ExcelWriter(caminho_arquivo) as writer:
                registros_saida.to_excel(writer, sheet_name='Saídas', index=False)
                registros_entrada.to_excel(writer, sheet_name='Entradas', index=False)
                estoque.to_excel(writer, sheet_name='Estoque', index=False)
        except Exception as e:
            raise ValueError(f"Erro ao exportar para Excel: {e}")

    def gerar_grafico(self, caminho_arquivo):
        """Gera um gráfico de barras das quantidades em estoque."""
        try:
            import matplotlib.pyplot as plt  # Importa matplotlib aqui para evitar erro se matplotlib não estiver instalado

            avaliacoes = list(self.dados["estoque"].keys())
            quantidades = list(self.dados["estoque"].values())

            plt.figure(figsize=(10, 6))
            plt.bar(avaliacoes, quantidades, color='skyblue')
            plt.xlabel('Avaliações')
            plt.ylabel('Quantidade em Estoque')
            plt.title('Quantidade em Estoque por Avaliação')
            plt.xticks(rotation=90)
            plt.tight_layout()
            plt.savefig(caminho_arquivo)
            plt.close()
        except Exception as e:
            raise ValueError(f"Erro ao gerar gráfico: {e}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gestão de Avaliações')
        self.setGeometry(100, 100, 1200, 800)

        self.data_manager = DataManager()

        # Widgets de entrada
        self.input_entrada = QGroupBox("Adicionar Entrada")
        self.input_saida = QGroupBox("Adicionar Saída")

        # Formulários de entrada
        self.form_entrada = QFormLayout()
        self.entrada_especialidade = QComboBox()
        self.entrada_avaliacao = QComboBox()
        self.entrada_quantidade = QLineEdit()
        self.botao_adicionar_entrada = QPushButton("Adicionar Entrada")

        self.form_entrada.addRow("Especialidade:", self.entrada_especialidade)
        self.form_entrada.addRow("Avaliação:", self.entrada_avaliacao)
        self.form_entrada.addRow("Quantidade:", self.entrada_quantidade)
        self.form_entrada.addWidget(self.botao_adicionar_entrada)
        self.input_entrada.setLayout(self.form_entrada)

        # Formulários de saída
        self.form_saida = QFormLayout()
        self.saida_terapeuta = QComboBox()
        self.saida_paciente = QLineEdit()
        self.saida_especialidade = QComboBox()
        self.saida_avaliacao = QComboBox()
        self.saida_quantidade = QLineEdit()
        self.botao_adicionar_saida = QPushButton("Adicionar Saída")

        self.form_saida.addRow("Terapeuta:", self.saida_terapeuta)
        self.form_saida.addRow("Paciente:", self.saida_paciente)
        self.form_saida.addRow("Especialidade:", self.saida_especialidade)
        self.form_saida.addRow("Avaliação:", self.saida_avaliacao)
        self.form_saida.addRow("Quantidade:", self.saida_quantidade)
        self.form_saida.addWidget(self.botao_adicionar_saida)
        self.input_saida.setLayout(self.form_saida)

        # Tabelas
        self.tabela_entrada = QTableWidget()
        self.tabela_saida = QTableWidget()
        self.tabela_estoque = QTableWidget()

        # Configuração das tabelas
        self.configurar_tabela(self.tabela_entrada, ["Especialidade", "Avaliação", "Quantidade", "Data de Entrada"])
        self.configurar_tabela(self.tabela_saida, ["Terapeuta", "Paciente", "Especialidade", "Avaliação", "Quantidade", "Data de Saída"])
        self.configurar_tabela(self.tabela_estoque, ["Avaliação", "Quantidade"])

        # Funções de adicionar e remover terapeuta
        self.botao_adicionar_terapeuta = QPushButton("Adicionar Terapeuta")
        self.botao_remover_terapeuta = QPushButton("Remover Terapeuta")
        self.entrada_terapeuta = QLineEdit()

        # Layouts
        layout_main = QVBoxLayout()

        # Layout para Inputs de Entrada e Saída
        layout_inputs = QHBoxLayout()
        layout_inputs.addWidget(self.input_entrada)
        layout_inputs.addWidget(self.input_saida)

        # Layout para Tabelas (Entrada e Estoque lado a lado)
        layout_tabelas_superior = QHBoxLayout()
        
        layout_entrada = QVBoxLayout()
        layout_entrada.addWidget(QLabel("Tabela de Entrada"))
        layout_entrada.addWidget(self.tabela_entrada)

        layout_estoque = QVBoxLayout()
        layout_estoque.addWidget(QLabel("Tabela de Estoque"))
        layout_estoque.addWidget(self.tabela_estoque)

        layout_tabelas_superior.addLayout(layout_entrada)
        layout_tabelas_superior.addLayout(layout_estoque)

        # Layout para Tabela de Saída abaixo
        layout_tabelas_inferior = QVBoxLayout()
        layout_tabelas_inferior.addWidget(QLabel("Tabela de Saída"))
        layout_tabelas_inferior.addWidget(self.tabela_saida)

        # Layout para Funções de Terapeutas
        layout_terapeutas = QVBoxLayout()
        layout_terapeutas.addWidget(QLabel("Adicionar/Remover Terapeuta"))
        layout_terapeutas.addWidget(self.entrada_terapeuta)
        layout_terapeutas.addWidget(self.botao_adicionar_terapeuta)
        layout_terapeutas.addWidget(self.botao_remover_terapeuta)
        
        # Botão de Exportar Excel
        self.botao_exportar_excel = QPushButton("Exportar para Excel")
        layout_terapeutas.addWidget(self.botao_exportar_excel)

        # Adicionando os layouts ao layout principal
        layout_main.addLayout(layout_inputs)
        layout_main.addLayout(layout_tabelas_superior)
        layout_main.addLayout(layout_tabelas_inferior)
        layout_main.addLayout(layout_terapeutas)

        container = QWidget()
        container.setLayout(layout_main)
        self.setCentralWidget(container)

        # Conectar os botões aos slots
        self.botao_adicionar_entrada.clicked.connect(self.adicionar_entrada)
        self.botao_adicionar_saida.clicked.connect(self.adicionar_saida)
        self.botao_adicionar_terapeuta.clicked.connect(self.adicionar_terapeuta)
        self.botao_remover_terapeuta.clicked.connect(self.remover_terapeuta)
        self.botao_exportar_excel.clicked.connect(self.exportar_excel)

        self.atualizar_tabelas()
        self.carregar_dados_iniciais()

    def exportar_excel(self):
        """Exporta os dados para um arquivo Excel."""
        # Abre um diálogo para escolher o caminho do arquivo
        caminho_arquivo, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo como", "", "Excel Files (*.xlsx);;All Files (*)")
        if caminho_arquivo:
            try:
                # Chama a função de exportação do DataManager
                self.data_manager.exportar_para_excel(caminho_arquivo)
                QMessageBox.information(self, "Sucesso", "Dados exportados para Excel com sucesso!")
            except Exception as e:
                QMessageBox.critical(self, "Erro", f"Erro ao exportar para Excel: {e}")
        

    def configurar_tabela(self, tabela, cabecalhos):
        """Configura as tabelas com os cabeçalhos especificados."""
        tabela.setColumnCount(len(cabecalhos))
        tabela.setHorizontalHeaderLabels(cabecalhos)
        tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        tabela.setSelectionBehavior(QTableWidget.SelectRows)

    def carregar_dados_iniciais(self):
        """Carrega as especialidades, avaliações e terapeutas nos comboboxes."""
        self.entrada_especialidade.addItems(self.data_manager.dados["especialidades"])
        self.saida_especialidade.addItems(self.data_manager.dados["especialidades"])
        self.saida_terapeuta.addItems(self.data_manager.dados["terapeutas"])
        self.atualizar_avaliacoes_entrada()
        self.atualizar_avaliacoes_saida()

        # Conectar o evento de mudança de especialidade
        self.entrada_especialidade.currentIndexChanged.connect(self.atualizar_avaliacoes_entrada)
        self.saida_especialidade.currentIndexChanged.connect(self.atualizar_avaliacoes_saida)

    def atualizar_avaliacoes_entrada(self):
        """Atualiza o combobox de avaliações com base na especialidade selecionada na entrada."""
        especialidade_selecionada = self.entrada_especialidade.currentText()
        self.entrada_avaliacao.clear()
        self.entrada_avaliacao.addItems(self.data_manager.dados["avaliacoes"].get(especialidade_selecionada, []))

    def atualizar_avaliacoes_saida(self):
        """Atualiza o combobox de avaliações com base na especialidade selecionada na saída."""
        especialidade_selecionada = self.saida_especialidade.currentText()
        self.saida_avaliacao.clear()
        self.saida_avaliacao.addItems(self.data_manager.dados["avaliacoes"].get(especialidade_selecionada, []))

    def adicionar_entrada(self):
        """Adiciona uma entrada de avaliação ao estoque."""
        try:
            especialidade = self.entrada_especialidade.currentText()
            avaliacao = self.entrada_avaliacao.currentText()
            quantidade = int(self.entrada_quantidade.text())

            self.data_manager.registrar_entrada(especialidade, avaliacao, quantidade)
            self.atualizar_tabelas()
            QMessageBox.information(self, "Sucesso", "Entrada registrada com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao adicionar entrada: {e}")

    def adicionar_saida(self):
        """Adiciona uma saída de avaliação e atualiza o estoque."""
        try:
            terapeuta = self.saida_terapeuta.currentText()
            paciente = self.saida_paciente.text()
            especialidade = self.saida_especialidade.currentText()
            avaliacao = self.saida_avaliacao.currentText()
            quantidade = int(self.saida_quantidade.text())

            self.data_manager.registrar_saida(terapeuta, paciente, especialidade, avaliacao, quantidade)
            self.atualizar_tabelas()
            QMessageBox.information(self, "Sucesso", "Saída registrada com sucesso!")
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao adicionar saída: {e}")

    def atualizar_tabelas(self):
        """Atualiza as tabelas de entrada, saída e estoque com os dados mais recentes."""
        self.atualizar_tabela_entrada()
        self.atualizar_tabela_saida()
        self.atualizar_tabela_estoque()

    def atualizar_tabela_entrada(self):
        """Atualiza a tabela de registros de entrada com os dados mais recentes."""
        self.tabela_entrada.setRowCount(0)  # Limpa a tabela antes de atualizar
        for registro in self.data_manager.dados["registros_entrada"]:
            linha = self.tabela_entrada.rowCount()
            self.tabela_entrada.insertRow(linha)
            
            # Cria itens e centraliza o texto
            especialidade_item = QTableWidgetItem(registro["especialidade"])
            especialidade_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_entrada.setItem(linha, 0, especialidade_item)

            avaliacao_item = QTableWidgetItem(registro["avaliacao"])
            avaliacao_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_entrada.setItem(linha, 1, avaliacao_item)

            quantidade_item = QTableWidgetItem(str(registro["quantidade"]))
            quantidade_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_entrada.setItem(linha, 2, quantidade_item)

            data_item = QTableWidgetItem(registro["data_entrada"])
            data_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_entrada.setItem(linha, 3, data_item)

        # Expande as colunas para ocupar o espaço disponível
        self.tabela_entrada.horizontalHeader().setStretchLastSection(True)
        self.tabela_entrada.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def atualizar_tabela_saida(self):
        """Atualiza a tabela de registros de saída com os dados mais recentes."""
        self.tabela_saida.setRowCount(0)  # Limpa a tabela antes de atualizar
        for registro in self.data_manager.dados["registros_saida"]:
            linha = self.tabela_saida.rowCount()
            self.tabela_saida.insertRow(linha)
            
            # Cria itens e centraliza o texto
            terapeuta_item = QTableWidgetItem(registro["terapeuta"])
            self.tabela_saida.setItem(linha, 0, terapeuta_item)

            paciente_item = QTableWidgetItem(registro["paciente"])
            paciente_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_saida.setItem(linha, 1, paciente_item)

            especialidade_item = QTableWidgetItem(registro["especialidade"])
            especialidade_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_saida.setItem(linha, 2, especialidade_item)

            avaliacao_item = QTableWidgetItem(registro["avaliacao"])
            avaliacao_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_saida.setItem(linha, 3, avaliacao_item)

            quantidade_item = QTableWidgetItem(str(registro["quantidade"]))
            quantidade_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_saida.setItem(linha, 4, quantidade_item)

            data_item = QTableWidgetItem(registro["data_saida"])
            data_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_saida.setItem(linha, 5, data_item)

        # Expande as colunas para ocupar o espaço disponível
        self.tabela_saida.horizontalHeader().setStretchLastSection(True)
        self.tabela_saida.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def atualizar_tabela_estoque(self):
        """Atualiza a tabela de estoque com os dados mais recentes."""
        self.tabela_estoque.setRowCount(0)  # Limpa a tabela antes de atualizar
        for avaliacao, quantidade in self.data_manager.dados["estoque"].items():
            linha = self.tabela_estoque.rowCount()
            self.tabela_estoque.insertRow(linha)
            
            # Cria itens e centraliza o texto
            avaliacao_item = QTableWidgetItem(avaliacao)
            avaliacao_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_estoque.setItem(linha, 0, avaliacao_item)

            quantidade_item = QTableWidgetItem(str(quantidade))
            quantidade_item.setTextAlignment(Qt.AlignCenter)  # Centraliza
            self.tabela_estoque.setItem(linha, 1, quantidade_item)

        # Expande as colunas para ocupar o espaço disponível
        self.tabela_estoque.horizontalHeader().setStretchLastSection(True)
        self.tabela_estoque.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
    def adicionar_terapeuta(self):
        """Adiciona um novo terapeuta à lista de terapeutas."""
        terapeuta = self.entrada_terapeuta.text().strip()
        if terapeuta:
            self.data_manager.dados["terapeutas"].append(terapeuta)
            self.data_manager.salvar_dados()
            self.saida_terapeuta.addItem(terapeuta)
            QMessageBox.information(self, "Sucesso", "Terapeuta adicionado com sucesso!")
        else:
            QMessageBox.warning(self, "Atenção", "O nome do terapeuta não pode estar vazio.")

    def remover_terapeuta(self):
        """Remove o terapeuta selecionado da lista de terapeutas."""
        terapeuta = self.saida_terapeuta.currentText()
        if terapeuta:
            self.data_manager.dados["terapeutas"].remove(terapeuta)
            self.data_manager.salvar_dados()
            self.saida_terapeuta.removeItem(self.saida_terapeuta.currentIndex())
            QMessageBox.information(self, "Sucesso", "Terapeuta removido com sucesso!")
        else:
            QMessageBox.warning(self, "Atenção", "Nenhum terapeuta selecionado.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
