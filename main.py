import os
import sys
import sqlite3

from PyQt5.QtGui import QFont, QPalette, QColor, QPixmap, QBrush
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, \
    QStackedLayout, QMenuBar, QMenu, QFrame, QComboBox, QLineEdit
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.connection = sqlite3.Connection("reservations.db")
        self.cursor = self.connection.execute("SELECT * FROM parking_spot")
        print("{: >8} | {: >8} |".format(f'Stall:', f'Lot:'))

        for row in self.cursor:
            print("{: >8} | {: >8} |".format(*row))

        # Set the title for the window
        self.setWindowTitle("Login Page")
        # self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

        # Set the size of the window
        self.setFixedSize(400, 300)

        self.frame_username = QFrame(self)
        self.frame_full_name = QFrame(self)
        # self.frame_email = QFrame(self)
        self.cmbo_box_user_type = QComboBox(self)

        self.label_username = QLabel("Student ID:", self)
        self.label_pswd = QLabel("Password", self)
        self.edit_full_name = QLineEdit(self.frame_full_name)
        # self.edit_email = QLineEdit(self.frame_email)
        self.frame_pswd = QFrame(self)
        self.line_edit_username = QLineEdit(self.frame_username)
        self.lbl_full_name = QLabel("License Plate No:", self)
        self.lbl_email = QLabel("Email", self)
        self.line_edit_pswd = QLineEdit(self.frame_pswd)

        self.btn_submit = QPushButton("Submit", self)
        # self.btn_submit.clicked.connect(self.check_submission)
        self.btn_cancel = QPushButton("Cancel", self)
        self.btn_cancel.clicked.connect(self.close)
        self.line_edit_pswd.setFrame(False)
        self.app_header()
        self.create_forms()

    def __repr__(self):
        return 'Login(Qt Window)'

    def app_header(self):
        palet = QPalette()
        # palet.setColor(QPalette.Background, QColor(10, 80, 30))
        palet.setBrush(QPalette.Background, QBrush(QPixmap("ufv-abbotsford-campus-fraser-valley.jpg")))

        # QFrame preserves a space of your size in the main window
        frame = QFrame(self)
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setAutoFillBackground(True)
        frame.setPalette(palet)
        frame.setFixedWidth(400)
        frame.setFixedHeight(84)
        frame.move(0, 0)
        #
        label_icon = QLabel(frame)
        label_icon.setFixedWidth(60)
        label_icon.setFixedHeight(60)
        label_icon.setPixmap(QPixmap("").scaled(40, 40, Qt.KeepAspectRatio,Qt.SmoothTransformation))
        label_icon.move(37, 22)

        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)

        lable_title = QLabel("University of the Fraser Valley", frame)

        lable_title.setStyleSheet("background-color: rgba(255,255,255,0.5);"
                                  "font: bold 25px;"
                                  "color: black;"
                                  "")

        lable_title.setFont(title_font)
        lable_title.move(20, 20)
        #
        description_font = QFont()
        description_font.setPointSize(9)

        description_label = QLabel("Electric Vehicle Reservation", frame)
        description_label.setStyleSheet("background-color: rgba(255,255,255,0.5);"
                                        "color: black;"
                                        "font: bold 15px;")

        description_label.setFont(description_font)
        description_label.move(50, 50)

    def create_forms(self):
        self.login_form()
        label_user_type = QLabel("Register or Login", self)
        label_user_type.resize(400, 20)
        label_user_type.move(60, 110)
        self.cmbo_box_user_type.addItems(["Login", "Register"])
        self.cmbo_box_user_type.setCurrentIndex(0)
        self.cmbo_box_user_type.setFixedWidth(280)
        self.cmbo_box_user_type.setFixedHeight(26)
        self.cmbo_box_user_type.move(60, 136)
        self.cmbo_box_user_type.currentIndexChanged.connect(self.on_combobox_togl)
        # self.btn_submit.clicked.connect(self.check_submission)

    def login_as_user(self):
        pass

    def register_user(self):
        pass

    def registration_form(self):
        # self.frame_email.show()
        self.frame_full_name.show()
        # self.lbl_email.show()
        self.lbl_full_name.show()
        self.setFixedSize(400, 440)

        # Full name --> frame and label
        self.frame_full_name.setFrameShape(QFrame.StyledPanel)
        self.frame_full_name.setFixedWidth(280)
        self.frame_full_name.setFixedHeight(28)
        self.lbl_full_name.move(60, 170)
        self.frame_full_name.move(60, 196)
        image_username = QLabel(self.frame_full_name)
        image_username.setPixmap(QPixmap("username.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                Qt.SmoothTransformation))
        image_username.move(10, 4)
        self.edit_full_name.setFrame(False)
        self.edit_full_name.setTextMargins(8, 0, 4, 1)
        self.edit_full_name.setFixedWidth(238)
        self.edit_full_name.setFixedHeight(26)
        self.edit_full_name.move(40, 1)

        # Email --> frame and label
        # self.frame_email.setFrameShape(QFrame.StyledPanel)
        # self.frame_email.setFixedWidth(280)
        # self.frame_email.setFixedHeight(28)
        # self.lbl_email.move(60, 224)
        # self.frame_email.move(60, 250)
        # image_email = QLabel(self.frame_email)
        # image_email.setPixmap(QPixmap("email.png").scaled(20, 20, Qt.KeepAspectRatio,
        #                                                   Qt.SmoothTransformation))
        # image_email.move(10, 4)
        # self.edit_email.setFrame(False)
        # self.edit_email.setTextMargins(8, 0, 4, 1)
        # self.edit_email.setFixedWidth(238)
        # self.edit_email.setFixedHeight(26)
        # self.edit_email.move(40, 1)

        # Move login form
        self.label_username.move(60, 225)
        self.frame_username.move(60, 250)

        self.label_pswd.move(60, 275)
        self.frame_pswd.move(60, 300)

        self.btn_submit.move(60, 350)
        self.btn_cancel.move(205, 350)
        # self.btn_submit.clicked.connect(self.check_submission)

    def on_combobox_togl(self, index):
        if index == 1:
            print("Registration")
            self.registration_form()
        else:
            print("Login")
            self.login_form()

    def login_form(self):
        # self.frame_email.hide()
        self.frame_full_name.hide()
        self.lbl_email.hide()
        self.lbl_full_name.hide()
        self.setFixedSize(400, 380)
        self.label_username.move(60, 170)

        self.frame_username.setFrameShape(QFrame.StyledPanel)
        self.frame_username.setFixedWidth(280)
        self.frame_username.setFixedHeight(28)
        self.frame_username.move(60, 196)
        #
        image_username = QLabel(self.frame_username)
        image_username.setPixmap(QPixmap("username.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                Qt.SmoothTransformation))
        image_username.move(10, 4)
        self.line_edit_username.setFrame(False)
        self.line_edit_username.setTextMargins(8, 0, 4, 1)
        self.line_edit_username.setFixedWidth(238)
        self.line_edit_username.setFixedHeight(26)
        self.line_edit_username.move(40, 1)
        self.label_pswd.move(60, 224)

        self.frame_pswd.setFrameShape(QFrame.StyledPanel)
        self.frame_pswd.setFixedWidth(280)
        self.frame_pswd.setFixedHeight(28)
        self.frame_pswd.move(60, 250)

        img_pswd = QLabel(self.frame_pswd)
        img_pswd.setPixmap(QPixmap("password.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                          Qt.SmoothTransformation))
        img_pswd.move(10, 4)

        self.line_edit_pswd.setEchoMode(QLineEdit.Password)
        self.line_edit_pswd.setTextMargins(8, 0, 4, 1)
        self.line_edit_pswd.setFixedWidth(238)
        self.line_edit_pswd.setFixedHeight(26)
        self.line_edit_pswd.move(40, 1)

        self.btn_submit.setFixedWidth(135)
        self.btn_submit.setFixedHeight(28)
        self.btn_submit.move(60, 286)

        self.btn_cancel.setFixedWidth(135)
        self.btn_cancel.setFixedHeight(28)
        self.btn_cancel.move(205, 286)

    def get_login_details(self):
        username = str(self.line_edit_username.text())
        password = str(self.line_edit_pswd.text())
        return [username, password]

    def check_user_type(self):
        return str(self.cmbo_box_user_type.currentText())

    def get_register_details(self):
        email = str(self.edit_email.text())
        full_name = str(self.edit_full_name.text())
        password = str(self.line_edit_pswd.text())
        username = str(self.line_edit_username.text())
        return [username, password, email, full_name]

    def display_msg(self, title: str, msg: str):
        QMessageBox.about(self, title, msg)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    mainwindow = MainWindow()
    mainwindow.show()

    sys.exit(app.exec_())
