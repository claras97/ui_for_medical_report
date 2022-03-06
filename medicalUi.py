import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import printer

INFO_XPOS	= 20
INFO_YPOS	= 20
INFO_INTER	= 35
INFO_HEIGHT	= 25

class medUi(QMainWindow):
	def __init__(self, parent=None):
		super(medUi, self).__init__(parent)
		self.resize(500, 490)
		self.setWindowTitle('Formulário do relatório médico')

		self.nameLabel = QLabel(self)
		self.nameLabel.setText('Nome')
		self.nameLabel.setGeometry(QRect(INFO_XPOS, INFO_YPOS, 40, INFO_HEIGHT))
		self.nameEdit = QLineEdit(self)
		self.nameEdit.setGeometry(QRect(70, INFO_YPOS, 300, INFO_HEIGHT))

		self.ageLabel = QLabel(self)
		self.ageLabel.setText('Idade')
		self.ageLabel.setGeometry(QRect(INFO_XPOS, INFO_YPOS+INFO_INTER*1, 40, INFO_HEIGHT))
		self.ageEdit = QLineEdit(self)
		self.ageEdit.setGeometry(QRect(70, INFO_YPOS+INFO_INTER*1, 50, INFO_HEIGHT))

		self.doctorLabel = QLabel(self)
		self.doctorLabel.setText('Médico requisitante')
		self.doctorLabel.setGeometry(QRect(INFO_XPOS, INFO_YPOS+INFO_INTER*2, 150, INFO_HEIGHT))
		self.doctorEdit = QLineEdit(self)
		self.doctorEdit.setGeometry(QRect(165, INFO_YPOS+INFO_INTER*2, 300, INFO_HEIGHT))

		self.indicationLabel = QLabel(self)
		self.indicationLabel.setText('Indicação')
		self.indicationLabel.setGeometry(QRect(INFO_XPOS, INFO_YPOS+INFO_INTER*3, 70, INFO_HEIGHT))
		self.indicationEdit = QLineEdit(self)
		self.indicationEdit.setGeometry(QRect(100, INFO_YPOS+INFO_INTER*3, 215, INFO_HEIGHT))

		self.medicationLabel = QLabel(self)
		self.medicationLabel.setText('Medicação')
		self.medicationLabel.setGeometry(QRect(INFO_XPOS, INFO_YPOS+INFO_INTER*4, 80, INFO_HEIGHT))
		self.medicationEdit = QLineEdit(self)
		self.medicationEdit.setGeometry(QRect(100, INFO_YPOS+INFO_INTER*4, 215, INFO_HEIGHT))

		self.tensionLabel = QLabel(self)
		self.tensionLabel.setText('Valores tensionais médios')
		self.tensionLabel.setGeometry(QRect(INFO_XPOS, INFO_YPOS+INFO_INTER*6, 200, INFO_HEIGHT))
		self.tensionSistLabel = QLabel(self)
		self.tensionSistLabel.setText('Sistólico')
		self.tensionSistLabel.setGeometry(QRect(211, INFO_YPOS+INFO_INTER*5.3, 90, INFO_HEIGHT))
		self.tensionSistEdit = QLineEdit(self)
		self.tensionSistEdit.setGeometry(QRect(205, INFO_YPOS+INFO_INTER*6, 68, INFO_HEIGHT))
		self.tensionDiasLabel = QLabel(self)
		self.tensionDiasLabel.setText('Diastólico')
		self.tensionDiasLabel.setGeometry(QRect(288, INFO_YPOS+INFO_INTER*5.3, 90, INFO_HEIGHT))
		self.tensionDiasEdit = QLineEdit(self)
		self.tensionDiasEdit.setGeometry(QRect(288, INFO_YPOS+INFO_INTER*6, 68, INFO_HEIGHT))

		self.regHighLabel = QLabel(self)
		self.regHighLabel.setText('Registos mais altos:')
		self.regHighLabel.setGeometry(QRect(INFO_XPOS, INFO_YPOS+INFO_INTER*7, 200, INFO_HEIGHT))
		self.regDayLabel = QLabel(self)
		self.regDayLabel.setText('- no período diurno')
		self.regDayLabel.setGeometry(QRect(INFO_XPOS*2.5, INFO_YPOS+INFO_INTER*7.7, 200, INFO_HEIGHT))
		self.regDaySistEdit = QLineEdit(self)
		self.regDaySistEdit.setGeometry(QRect(205, INFO_YPOS+INFO_INTER*7.7, 68, INFO_HEIGHT))
		self.regDayDiasEdit = QLineEdit(self)
		self.regDayDiasEdit.setGeometry(QRect(288, INFO_YPOS+INFO_INTER*7.7, 68, INFO_HEIGHT))
		self.regNightLabel = QLabel(self)
		self.regNightLabel.setText('- no período noturno')
		self.regNightLabel.setGeometry(QRect(INFO_XPOS*2.5, INFO_YPOS+INFO_INTER*8.5, 200, INFO_HEIGHT))
		self.regNightSistEdit = QLineEdit(self)
		self.regNightSistEdit.setGeometry(QRect(205, INFO_YPOS+INFO_INTER*8.5, 68, INFO_HEIGHT))
		self.regNightDiasEdit = QLineEdit(self)
		self.regNightDiasEdit.setGeometry(QRect(288, INFO_YPOS+INFO_INTER*8.5, 68, INFO_HEIGHT))

		self.variationLabel = QLabel(self)
		self.variationLabel.setText('% variação')
		self.variationLabel.setGeometry(QRect(INFO_XPOS, INFO_YPOS+INFO_INTER*9.5, 200, INFO_HEIGHT))
		self.variationEdit = QLineEdit(self)
		self.variationEdit.setGeometry(QRect(100, INFO_YPOS+INFO_INTER*9.5, 40, INFO_HEIGHT))

		self.sintomsLabel = QLabel(self)
		self.sintomsLabel.setText('Sintomas')
		self.sintomsLabel.setGeometry(QRect(INFO_XPOS, INFO_YPOS+INFO_INTER*10.5, 200, INFO_HEIGHT))
		self.sintomsEdit = QCheckBox(self)
		self.sintomsEdit.setGeometry(QRect(90, INFO_YPOS+INFO_INTER*10.18, 50, 50))

		self.resetButton = QPushButton(self)
		self.resetButton.setText('Limpar')
		self.resetButton.setGeometry(QRect(INFO_XPOS, INFO_YPOS+INFO_INTER*12, 60, 25))
		self.resetButton.clicked.connect(self.nameEdit.clear)
		self.resetButton.clicked.connect(self.ageEdit.clear)
		self.resetButton.clicked.connect(self.doctorEdit.clear)
		self.resetButton.clicked.connect(self.indicationEdit.clear)
		self.resetButton.clicked.connect(self.medicationEdit.clear)
		self.resetButton.clicked.connect(self.tensionSistEdit.clear)
		self.resetButton.clicked.connect(self.tensionDiasEdit.clear)
		self.resetButton.clicked.connect(self.regDaySistEdit.clear)
		self.resetButton.clicked.connect(self.regDayDiasEdit.clear)
		self.resetButton.clicked.connect(self.regNightSistEdit.clear)
		self.resetButton.clicked.connect(self.regNightDiasEdit.clear)
		self.resetButton.clicked.connect(self.variationEdit.clear)

		self.printButton = QPushButton(self)
		self.printButton.setText('Guardar')
		self.printButton.setGeometry(QRect(INFO_XPOS+70, INFO_YPOS+INFO_INTER*12, 60, 25))
		self.printButton.clicked.connect(self.printClicked)

	def printClicked(self):
		dialog = QDialog(self)
		dialog.setWindowTitle('Informação')
		dialog.resize(373, 50)
		dialogLabel = QLabel(dialog)
		dialogLabel.move(10, 15)
		ret = True
		dialogFile = QFileDialog(self)
		if self.nameEdit.text() == '' or self.ageEdit.text() == '' or self.doctorEdit.text() == '' or self.indicationEdit.text() == '' or self.medicationEdit.text() == '' or self.tensionSistEdit.text() == '' or self.tensionDiasEdit.text() == '' or self.regDaySistEdit.text() == '' or self.regDayDiasEdit.text() == '' or self.regNightSistEdit.text() == '' or self.regNightDiasEdit.text() == '' or self.variationEdit.text() == '':
			dialogLabel.setText('ERRO: Todos os parâmetros devem ser preenchidos.')
			dialog.show()
		else:
			filepath = dialogFile.getSaveFileName(self, 'Escolha a localização do ficheiro', 'relatorio_medico.docx')[0]
			ret = printer.ink(self.nameEdit.text(), int(self.ageEdit.text()), self.doctorEdit.text(), self.indicationEdit.text(), self.medicationEdit.text(), float(self.tensionSistEdit.text()), float(self.tensionDiasEdit.text()), float(self.regDaySistEdit.text()), float(self.regDayDiasEdit.text()), float(self.regNightSistEdit.text()), float(self.regNightDiasEdit.text()), float(self.variationEdit.text()), self.sintomsEdit.isChecked(), filepath)
			if ret:
				dialog.resize(257, 50)
				dialogLabel.setText('OK: Relatório gerado com sucesso!')
			else:
				dialogLabel.setText('ERRO: Não foi possível imprimir o relatório.')
			dialog.show()
	

def main():
	app = QApplication(sys.argv)
	ui = medUi()
	ui.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()

