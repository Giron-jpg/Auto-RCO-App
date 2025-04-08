import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QMessageBox,
                             QPushButton, QVBoxLayout, QWidget)


class GestorNotasEscolares(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        # Configurar a janela principal
        self.setWindowTitle("Gestor de Notas Escolares")
        self.setFixedSize(400, 350)

        # Widget central e layout
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        layout = QVBoxLayout()
        widget_central.setLayout(layout)

        # Título
        titulo = QLabel("Gestor de Notas Escolares")
        titulo.setFont(QFont("Arial", 16, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        # Botões
        botoes = [
            "Cadastrar Turma",
            "Importar Alunos do Site",
            "Lançar Notas",
            "Exportar para PDF",
            "Sair"
        ]

        self.botoes_dict = {}

        for texto_botao in botoes:
            botao = QPushButton(texto_botao)
            botao.setMinimumHeight(50)
            botao.setFont(QFont("Arial", 11))
            # Conectar cada botão à função correspondente
            botao.clicked.connect(lambda checked, b=texto_botao: self.acao_botao(b))
            layout.addWidget(botao)
            self.botoes_dict[texto_botao] = botao

        # Adicionar algum espaçamento ao layout
        layout.setSpacing(10)
        layout.setContentsMargins(30, 20, 30, 20)

    def acao_botao(self, texto_botao):
        if texto_botao == "Sair":
            self.close()
        else:
            QMessageBox.information(self, f"Função: {texto_botao}",
                                    f"Você clicou no botão: {texto_botao}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Definir estilo global (opcional)
    app.setStyle("Fusion")
    janela = GestorNotasEscolares()
    janela.show()
    sys.exit(app.exec_())