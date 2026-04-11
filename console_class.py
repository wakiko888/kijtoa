#ajouter "self.console = console(posX console initial, posY console initial, tailleX console initial, tailleY console initial, taille_ecran_x, taille_ecran_y)" au début de __init__
#ajouter "self.console.print_text("texte", 7 <- nombre correspondant a la couleur de 1 a 16)", dans update chaque fois que on veut ajouter du texte a la console
#ajouter "self.console.print_logs()" dans draw pour draw tout le texte ajouter

import pyxel

class console():
    def __init__(self, postion_console_x, postion_console_y, taille_console_x, taille_console_y, taille_ecran_x, taille_ecran_y):
        self.logs = []
        self.color_logs = []
        self.Xpos = postion_console_x
        self.Ypos = postion_console_y
        self.Xsize = taille_console_x
        self.Ysize = taille_console_y
        self.screen_x = taille_ecran_x
        self.screen_y = taille_ecran_y

    def print_text(self, text, col):
        self.espace_dispo = self.screen_y - self.Ypos
        self.max_lines = self.espace_dispo // 6
        self.logs.append(text)
        self.color_logs.append(col)
        if len(self.logs) >= self.max_lines:
            self.logs.pop(0)
            self.color_logs.pop(0)

    def print_logs(self):
        count = 0
        while count < len(self.logs):
            pyxel.text(self.Xpos, count*6 + self.Ypos, self.logs[count], self.color_logs[count])
            count += 1