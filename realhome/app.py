from vulk import BaseApp
from vulk import ui


class App(BaseApp):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = ui.UI()
        menubar = ui.MenuBar()
        menubar.add("Fichier").add("Edit")
        self.ui.add(menubar)

    def start(self):
        super().start()

    def end(self):
        pass

    def resize(self):
        super().resize()
        self.ui.resize(self.context)

    def render(self, delta):
        self.context.clear_final_image([0, 0, 0.2, 1])
        sem = self.ui.render(delta)
        self.context.swap([sem])
