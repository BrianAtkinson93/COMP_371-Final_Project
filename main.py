import os
import sys
import sqlite3

# Module Imports
from PyQt5.QtGui import QFont, QPalette, QColor, QPixmap, QBrush
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow, QGridLayout, QWidget, QVBoxLayout, QHBoxLayout, \
    QStackedLayout, QMenuBar, QMenu, QFrame, QComboBox, QLineEdit
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

# Local Imports
from stubs.encryption import *


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self, key):
        super().__init__()

        self.connection = sqlite3.Connection("reservations.db")
        self.key = key

        # Set the title for the window
        self.setWindowTitle("Login Page")
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)

        self.page_index = 0

        # Set the size of the window
        self.setFixedSize(400, 300)

        self.frame_student_id = QFrame(self)
        self.frame_license_plate = QFrame(self)
        # self.frame_email = QFrame(self)

        self.cmbo_box_user_type = QComboBox(self)
        self.label_student_id = QLabel("Student ID:", self)
        self.label_pswd = QLabel("Password", self)
        self.edit_license_plate = QLineEdit(self.frame_license_plate)

        # self.edit_email = QLineEdit(self.frame_email)
        self.frame_pswd = QFrame(self)
        self.line_edit_student_id = QLineEdit(self.frame_student_id)
        self.lbl_license_plate = QLabel("License Plate No:", self)

        # self.lbl_email = QLabel("Email", self)
        self.line_edit_pswd = QLineEdit(self.frame_pswd)

        self.btn_submit = QPushButton("Submit", self)
        self.btn_submit.clicked.connect(self.check_submission)
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
        palet.setBrush(QPalette.Background, QBrush(QPixmap("images/ufv-abbotsford-campus-fraser-valley.jpg")))

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
        # label_icon.setPixmap(QPixmap("images/license_plate.png").scaled(40, 40, Qt.KeepAspectRatio, Qt.SmoothTransformation))
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
        self.btn_submit.clicked.connect(self.check_submission)

    def login_as_user(self, id_=None, password_=None):

        if id_ is None:
            print('Please provide a valid student id', file=sys.stderr)
            sys.exit(os.EX_IOERR)
        elif password_ is None:
            print('Please provide a valid password', file=sys.stderr)
            sys.exit(os.EX_IOERR)

        elif None not in (id_, password_):
            self.cursor = self.connection.execute(
                f"SELECT student_no, password FROM students WHERE student_no = {id_};")
            list = self.cursor.fetchall()
            if len(list) > 1:
                print(f'Error with database, please contact your distributor', file=sys.stderr)
                sys.exit(os.EX_DATAERR)
            else:
                for entry in list:
                    check_uname = entry[0]
                    check_pwd = entry[1]

        boolean = self.validate_credentials(password_, check_pwd)

        if boolean:
            pass

        return

    def register_user(self):
        pass

    def registration_form(self):
        self.frame_license_plate.show()
        self.lbl_license_plate.show()
        self.setFixedSize(400, 440)

        # Full name --> frame and label
        self.frame_license_plate.setFrameShape(QFrame.StyledPanel)
        self.frame_license_plate.setFixedWidth(280)
        self.frame_license_plate.setFixedHeight(28)
        self.lbl_license_plate.move(60, 170)
        self.frame_license_plate.move(60, 196)
        image_license_plate = QLabel(self.frame_license_plate)
        image_license_plate.setPixmap(QPixmap("images/license_plate.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                                 Qt.SmoothTransformation))
        image_license_plate.move(10, 4)
        self.edit_license_plate.setFrame(False)
        self.edit_license_plate.setTextMargins(8, 0, 4, 1)
        self.edit_license_plate.setFixedWidth(238)
        self.edit_license_plate.setFixedHeight(26)
        self.edit_license_plate.move(40, 1)

        # Move login form
        self.label_student_id.move(60, 225)
        self.frame_student_id.move(60, 250)

        self.label_pswd.move(60, 275)
        self.frame_pswd.move(60, 300)

        self.btn_submit.move(60, 350)
        self.btn_cancel.move(205, 350)
        self.btn_submit.clicked.connect(self.check_submission)

    def check_submission(self):
        # page 0 == login
        if self.page_index == 0:
            usr, pwd = self.get_login_details()
            self.login_as_user(usr, pwd)

        # page 1 == register
        elif self.page_index == 1:
            pass

        # page 3 == reservation
        elif self.page_index == 2:
            pass

        # handle a failure
        else:
            pass

    def on_combobox_togl(self, index):
        if index == 1:
            # print("Registration")
            self.page_index = 1
            self.registration_form()
        else:
            # print("Login")
            self.page_index = 0
            self.login_form()

    def login_form(self):
        # self.frame_email.hide()
        self.frame_license_plate.hide()
        # self.lbl_email.hide()
        self.lbl_license_plate.hide()
        self.setFixedSize(400, 380)
        self.label_student_id.move(60, 170)

        self.frame_student_id.setFrameShape(QFrame.StyledPanel)
        self.frame_student_id.setFixedWidth(280)
        self.frame_student_id.setFixedHeight(28)
        self.frame_student_id.move(60, 196)
        #
        image_username = QLabel(self.frame_student_id)
        image_username.setPixmap(QPixmap("images/username.png").scaled(20, 20, Qt.KeepAspectRatio,
                                                                       Qt.SmoothTransformation))
        image_username.move(10, 4)
        self.line_edit_student_id.setFrame(False)
        self.line_edit_student_id.setTextMargins(8, 0, 4, 1)
        self.line_edit_student_id.setFixedWidth(238)
        self.line_edit_student_id.setFixedHeight(26)
        self.line_edit_student_id.move(40, 1)
        self.label_pswd.move(60, 224)

        self.frame_pswd.setFrameShape(QFrame.StyledPanel)
        self.frame_pswd.setFixedWidth(280)
        self.frame_pswd.setFixedHeight(28)
        self.frame_pswd.move(60, 250)

        img_pswd = QLabel(self.frame_pswd)
        img_pswd.setPixmap(QPixmap("images/password.png").scaled(20, 20, Qt.KeepAspectRatio,
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
        username = str(self.line_edit_student_id.text())
        password = str(self.line_edit_pswd.text())
        return [username, password]

    def check_user_type(self):
        return str(self.cmbo_box_user_type.currentText())

    def get_register_details(self):
        email = str(self.edit_email.text())
        full_name = str(self.edit_license_plate.text())
        password = str(self.line_edit_pswd.text())
        username = str(self.line_edit_student_id.text())
        return [username, password, email, full_name]

    def display_msg(self, title: str, msg: str):
        QMessageBox.about(self, title, msg)

    def validate_credentials(self, g_pwd, check_against_pwd):

        decrypted = decrypt(self.key, check_against_pwd)
        given_pwd = bytes(g_pwd, "utf-8")

        print(f'decrypted: {decrypted}, {type(decrypted)}')
        print(f'given_pwd: {given_pwd}, {type(given_pwd)}')

        if not given_pwd == decrypted:
            print('Failed Login Attempt', file=sys.stderr)
            sys.exit(os.EX_DATAERR)

        else:
            print(f'Credentials Validated...')

        return True


if __name__ == "__main__":
    key = base64.urlsafe_b64encode(bytes('UniversityOfTheFraserValley2022=', encoding="utf-8"))

    app = QApplication(sys.argv)

    mainwindow = MainWindow(key)
    mainwindow.show()

    sys.exit(app.exec_())
