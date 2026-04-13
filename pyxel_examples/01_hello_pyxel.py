import pyxel


class App:
<<<<<<< HEAD
    def init__(self):
        pyxel.init(160, 120, title="Hello Pyxel")
=======
    def __init__(self):
        pyxel.init(160, 120, title="caca")
>>>>>>> 16cdb6c8996f93a03dffadbaad340090e87a9f34
        pyxel.images[0].load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        print("Caca")

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)


App()
