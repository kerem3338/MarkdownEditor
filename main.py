"""
Lisans 2021 © Zoda
"""
from tkinter import *
import markdown
from tkhtmlview import HTMLLabel

root = Tk()
root.title(f"{' '*50}Markdown Editör")
root.geometry("500x500")

def save():
	export_win = Toplevel()
	export_win.geometry("200x100")
	export_win.title("Kaydet")

	l1 = Label(export_win, text="Çıktı Dosyası adı")
	l1.pack()
	dosya_adi = Entry(export_win)
	dosya_adi.pack()

	def cikti():
		with open(dosya_adi.get(), "w") as cikti_dosyasi:
			cikti_dosyasi.write(kod.get("1.0",END))
	onayla=Button(export_win, text="Tamam", command=cikti)
	onayla.pack(side=BOTTOM)
def html_export():
	export_win = Toplevel()
	export_win.geometry("200x100")
	export_win.title("Export To Html File")

	l1 = Label(export_win, text="Çıktı Dosyası adı")
	l1.pack()
	dosya_adi = Entry(export_win)
	dosya_adi.pack()

	def cikti():
		with open(dosya_adi.get(), "w") as cikti_dosyasi:
			cikti_dosyasi.write(markdown.markdown(kod.get("1.0",END)))
	onayla=Button(export_win, text="Tamam", command=cikti)
	onayla.pack(side=BOTTOM)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Html Çıktısı al", command=html_export)
filemenu.add_command(label="Kaydet", command=save)
filemenu.add_command(label="Çıkış", command=sys.exit)
menubar.add_cascade(label="Dosya", menu=filemenu) 
def run():
	code=markdown.markdown(kod.get("1.0",END))

	run_window = Toplevel()
	run_window.title("Output Window")
	code = HTMLLabel(run_window, html=code)
	code.pack(pady=20, padx=20)
	run_window.mainloop()


kod = Text(root,height=25, width=52)
kod.pack()


calistir = Button(text="Çalıştır", command=run)
calistir.pack()

root.config(menu=menubar)
root.mainloop()