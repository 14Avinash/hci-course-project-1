# A rock paper scissors game using the basic QtWidgets

import sys
import PyQt5.QtWidgets as qt_widgets
import PyQt5.QtGui as qt_gui
import PyQt5.QtCore as qt_core
import random as rand

# Font Globals
text_font = qt_gui.QFont("Times", 14)
button_font = qt_gui.QFont("Arial", 12)
computer_score = 0
player_score = 0


class Window(qt_widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.timer = qt_core.QTimer(self)
        self.rps_game = qt_widgets.QLabel(self)
        self.score_computer_text = qt_widgets.QLabel("Computer Score: {0}".format(computer_score), self)
        self.score_player_text = qt_widgets.QLabel("Player Score: {0}".format(player_score), self)
        self.rps_image_computer = qt_widgets.QLabel(self)
        self.rps_image_player = qt_widgets.QLabel(self)
        self.setWindowTitle("Rock, Paper, Scissors!")
        self.setGeometry(350, 150, 550, 500)
        self.user_interface()

    def user_interface(self):
        # Scores
        self.score_computer_text.move(50, 30)
        self.score_player_text.move(350, 30)

        # Fonts
        self.score_computer_text.setFont(text_font)
        self.score_player_text.setFont(text_font)

        # Images
        self.rps_image_computer.setPixmap(qt_gui.QPixmap('./rock_paper_scissors/resources/rock.png'))
        self.rps_image_computer.move(50, 100)
        self.rps_image_player.setPixmap(qt_gui.QPixmap('./rock_paper_scissors/resources/rock.png'))
        self.rps_image_player.move(350, 100)
        self.rps_game.setPixmap(qt_gui.QPixmap('./rock_paper_scissors/resources/game.png'))
        self.rps_game.move(250, 160)

        # Buttons
        btn_start = qt_widgets.QPushButton("Start", self)
        btn_start.setFont(button_font)
        btn_start.move(180, 250)
        btn_stop = qt_widgets.QPushButton("Stop", self)
        btn_stop.setFont(button_font)
        btn_stop.move(290, 250)

        # Timer
        self.timer.setInterval(200)  # Set the interval for our timer to 200 milliseconds
        self.timer.timeout.connect(self.play_game)
        btn_start.clicked.connect(self.start_game_timer)
        btn_stop.clicked.connect(self.stop_game_timer)

        # Show the UI
        self.show()

    def play_game(self):
        # Set the computer and player to random integers based on the timer's interval.
        self.rand_computer = rand.randint(0, 2)
        self.rand_player = rand.randint(0, 2)

        # Set the image for the computer based on the random integer currently being stored.
        if self.rand_computer == 0:
            self.rps_image_computer.setPixmap(qt_gui.QPixmap('./rock_paper_scissors/resources/rock.png'))
        elif self.rand_computer == 1:
            self.rps_image_computer.setPixmap(qt_gui.QPixmap('./rock_paper_scissors/resources/paper.png'))
        else:
            self.rps_image_computer.setPixmap(qt_gui.QPixmap('./rock_paper_scissors/resources/scissors.png'))

        # Set the image for the player based on the random integer currently being stored.
        if self.rand_player == 0:
            self.rps_image_player.setPixmap(qt_gui.QPixmap('./rock_paper_scissors/resources/rock.png'))
        elif self.rand_player == 1:
            self.rps_image_player.setPixmap(qt_gui.QPixmap('./rock_paper_scissors/resources/paper.png'))
        else:
            self.rps_image_player.setPixmap(qt_gui.QPixmap('./rock_paper_scissors/resources/scissors.png'))

    def start_game_timer(self):
        self.timer.start()

    def stop_game_timer(self):
        global computer_score
        global player_score

        # Computer: Rock vs Player: Rock, Paper, Scissors
        if self.rand_computer == 0 and self.rand_player == 0:
            msg_box = qt_widgets.QMessageBox.information(self, "Information", "Draw Game!")
        elif self.rand_computer == 0 and self.rand_player == 1:
            msg_box = qt_widgets.QMessageBox.information(self, "Information", "Player Wins!")
            player_score += 1
            self.score_player_text.setText("Player Score: {0}".format(player_score))
        elif self.rand_computer == 0 and self.rand_player == 2:
            msg_box = qt_widgets.QMessageBox.information(self, "Information", "Computer Wins!")
            computer_score += 1
            self.score_computer_text.setText("Computer Score: {0}".format(computer_score))
        # Computer: Paper vs Player: Rock, Paper, Scissors
        elif self.rand_computer == 1 and self.rand_player == 0:
            msg_box = qt_widgets.QMessageBox.information(self, "Information", "Computer Wins!")
            computer_score += 1
            self.score_computer_text.setText("Computer Score: {0}".format(computer_score))
        elif self.rand_computer == 1 and self.rand_player == 1:
            msg_box = qt_widgets.QMessageBox.information(self, "Information", "Draw Game!")
        elif self.rand_computer == 1 and self.rand_player == 2:
            msg_box = qt_widgets.QMessageBox.information(self, "Information", "Player Wins!")
            player_score += 1
            self.score_player_text.setText("Player Score: {0}".format(player_score))
        # Computer: Scissors vs Player: Rock, Paper, Scissors
        elif self.rand_computer == 2 and self.rand_player == 0:
            msg_box = qt_widgets.QMessageBox.information(self, "Information", "Player Wins!")
            player_score += 1
            self.score_player_text.setText("Player Score: {0}".format(player_score))
        elif self.rand_computer == 2 and self.rand_player == 1:
            msg_box = qt_widgets.QMessageBox.information(self, "Information", "Computer Wins!")
            computer_score += 1
            self.score_computer_text.setText("Computer Score: {0}".format(computer_score))
        else:
            msg_box = qt_widgets.QMessageBox.information(self, "Information", "Draw Game!")

        # Conclude Game Round
        if computer_score == 3:
            msg_box = qt_widgets.QMessageBox.information(self, "Information", "Game Over, Computer Wins!")
            computer_score = 0
            player_score = 0
        elif player_score == 3:
            msg_box = qt_widgets.QMessageBox.information(self, "Information", "Game Over, Player Wins!")
            computer_score = 0
            player_score = 0
            self.score_computer_text.setText("Computer Score: {0}".format(computer_score))
            self.score_player_text.setText("Player Score: {0}".format(player_score))

        self.timer.stop()
