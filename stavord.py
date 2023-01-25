import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk



class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Øv stave ord")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.file_chooser = Gtk.FileChooserButton("hent en fil", Gtk.FileChooserAction.OPEN)
        self.file_chooser.connect("file-set", self.on_file_chooser_file_set)
        self.box.add(self.file_chooser)

        self.entry = Gtk.Entry()
        self.entry.connect("activate", self.on_entry_activate)
        self.box.add(self.entry)

        self.result_label = Gtk.Label()
        self.box.add(self.result_label)

    def on_file_chooser_file_set(self, widget):
        file_path = self.file_chooser.get_filename()
        with open(file_path, 'r') as f:
            text = f.read()
            self.wordlist = text.split()

    def on_entry_activate(self, widget):
        search_word = self.entry.get_text()
        if search_word in self.wordlist:
            self.result_label.set_text("Stavet Rigtig")
        else:
            self.result_label.set_text("Øv, Prøv igen")
            

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

