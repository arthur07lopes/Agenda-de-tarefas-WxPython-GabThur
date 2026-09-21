# Programa agendador de tarefas em WXPython
# Utiliza uma lista com label "Lista de tarefas", armazenando as tarefas atualmente salvas. Após, um botão verde escrito "Adicionar tarefa" e um botão vermelho escrito "remover tarefa", seguidos de um botão "Sair".

import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(400, 300))
        self.init_UI()

    def init_UI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # Label "Lista de tarefas"
        self.lbl_tarefas = wx.StaticText(panel, label="Lista de tarefas")
        vbox.Add(self.lbl_tarefas, flag=wx.ALL | wx.CENTER, border=10)

        # Lista de tarefas
        self.lista_tarefas = wx.ListCtrl(panel, style=wx.LC_REPORT | wx.LC_SINGLE_SEL | wx.BORDER_SUNKEN)
        vbox.Add(self.lista_tarefas, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Botão "Adicionar tarefa"
        self.btn_adicionar_tarefa = wx.Button(panel, label="Adicionar tarefa")
        self.btn_adicionar_tarefa.SetBackgroundColour(wx.Colour(0, 255, 0))  # Verde
        self.btn_adicionar_tarefa.Bind(wx.EVT_BUTTON, self.on_adicionar_tarefa)
        vbox.Add(self.btn_adicionar_tarefa, flag=wx.ALL | wx.CENTER, border=10)

        # Botão "Remover tarefa"
        self.btn_remover_tarefa = wx.Button(panel, label="Remover tarefa")
        self.btn_remover_tarefa.SetBackgroundColour(wx.Colour(255, 0, 0))  # Vermelho
        self.btn_remover_tarefa.Bind(wx.EVT_BUTTON, self.on_remover_tarefa)
        vbox.Add(self.btn_remover_tarefa, flag=wx.ALL | wx.CENTER, border=10)

        # Botão "Sair"
        self.btn_sair = wx.Button(panel, label="Sair")
        self.btn_sair.Bind(wx.EVT_BUTTON, self.Close)
        vbox.Add(self.btn_sair, flag=wx.ALL | wx.CENTER, border=10)

        panel.SetSizer(vbox)
        self.Centre()

    def on_adicionar_tarefa(self, event):
        pass

def on_remover_tarefa(self, event):
        pass

app = wx.App()
frame = MainFrame(None, "Agendador de tarefas")
frame.Show()
app.MainLoop()