import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import mysql.connector

# Establecer la conexión con la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='usuarios'
)

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Crear una tabla (si no existe)
cursor.execute('''CREATE TABLE IF NOT EXISTS resultados (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    puntaje INT, 
                    resultados VARCHAR(50)
                )''')

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

cursor.execute("SELECT COALESCE(MAX(id), 0) FROM usuarios.resultados")
ultima_id = cursor.fetchone()[0]

# Incrementar la última ID para crear la siguiente
nueva_id = ultima_id + 1

enfermedad_guardada=0 #en que enfermedad va

Valores_enfe =  [0, 0, 0,0, 0, 0,0, 0, 0,0, 0, 0,0]
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("1084x700")
        self._frame = None
        self.crear_interfaz()

    def crear_interfaz(self):
        # Cargar la imagen de fondo
        imagen_fondo = Image.open("fondov1.png")
        imagen_fondo = imagen_fondo.resize((1084, 700))
        self.foto_fondo = ImageTk.PhotoImage(imagen_fondo)

        # Mostrar la imagen de fondo en un Label
        label_fondo = tk.Label(self, image=self.foto_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        # Vista 1
        estilo_boton = {
            'font': ('Arial', 20),
            'fg': 'white',
            'bg': '#2b2895',
            'width': 10,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }

        boton = tk.Button(self, text="Iniciar", **estilo_boton, command=self.abrir_ventana)
        boton.place(x=480, y=450)

    def abrir_ventana(self):
        self.switch_frame(VentanaSecundaria)

    def switch_frame(self, frame_class):
        nuevo_frame = frame_class(self)
        nuevo_frame.place(x=0, y=0, relwidth=1, relheight=1)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = nuevo_frame

class VentanaSecundaria(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.crear_interfaz()

    def crear_interfaz(self):
        # Cargar la imagen de fondo de la ventana secundaria
        imagen_fondo_secundaria = Image.open("fondov2.png")
        imagen_fondo_secundaria = imagen_fondo_secundaria.resize((1084, 700))
        self.foto_fondo_secundaria = ImageTk.PhotoImage(imagen_fondo_secundaria)

        # Mostrar la imagen de fondo en un Label
        label_fondo_secundaria = tk.Label(self, image=self.foto_fondo_secundaria)
        label_fondo_secundaria.place(x=0, y=0, relwidth=1, relheight=1)

        # Resto de los elementos de la ventana secundaria...
        # Vista 2
        estilo_boton = {
            'font': ('Arial', 20),
            'fg': 'white',
            'bg': '#2b2895',
            'width': 10,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }

        boton = tk.Button(self, text="Comenzar", **estilo_boton, command=self.abrir_ventana)
        boton.place(x=460, y=380)

    def abrir_ventana(self):
        self.switch_frame(VentanaEnfermedad)

    def switch_frame(self, frame_class):
        nuevo_frame = frame_class(self)
        nuevo_frame.place(x=0, y=0, relwidth=1, relheight=1)
        
        self._frame = nuevo_frame


class VentanaEnfermedad(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.crear_interfaz()

    def crear_interfaz(self):
        # Cargar la imagen de fondo de la ventana secundaria
        imagen_fondo_secundaria = Image.open("fondov3.png")
        imagen_fondo_secundaria = imagen_fondo_secundaria.resize((1084, 700))
        self.foto_fondo_secundaria = ImageTk.PhotoImage(imagen_fondo_secundaria)

        # Mostrar la imagen de fondo en un Label
        label_fondo_secundaria = tk.Label(self, image=self.foto_fondo_secundaria)
        label_fondo_secundaria.place(x=0, y=0, relwidth=1, relheight=1)

        # Resto de los elementos de la ventana Enfermedad...

        #estilos
        estilo_boton2 = {
            'font': ('Arial', 15),
            'fg': 'white',
            'bg': '#00a4ba',
            'width': 15,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }

        ###botones
        boton_D1 = tk.Button(self, text="Dolor de cabeza", **estilo_boton2, command=self.ir_cabeza)
        boton_D1.place(x=270, y=100)
        boton_D2 = tk.Button(self, text="Golpes", **estilo_boton2, command=self.ir_Golpes)
        boton_D2.place(x=270, y=150)
        boton_D3 = tk.Button(self, text="Dolor de estomago", **estilo_boton2, command=self.ir_estomago)
        boton_D3.place(x=270, y=200)
        boton_D4 = tk.Button(self, text="Diarrea", **estilo_boton2, command=self.ir_diarrea)
        boton_D4.place(x=270, y=250)
        boton_D5 = tk.Button(self, text="Dificultad para respirar", **estilo_boton2, command=self.ir_respirar)
        boton_D5.place(x=270, y=300)
        boton_D6 = tk.Button(self, text="Hemorragias", **estilo_boton2, command=self.ir_hemo)
        boton_D6.place(x=270, y=350)
        boton_D7 = tk.Button(self, text="Quemaduras", **estilo_boton2, command=self.ir_quema)
        boton_D7.place(x=270, y=400)
        boton_D8 = tk.Button(self, text="Mareos", **estilo_boton2, command=self.ir_mareos)
        boton_D8.place(x=270, y=450)
        ##### LOS QUE tienen sí y no}
        boton_D9 = tk.Button(self, text="Nauseas", **estilo_boton2, command=self.ir_nauseas)
        boton_D9.place(x=550, y=100)
        boton_D10 = tk.Button(self, text="Escalofrios", **estilo_boton2, command=self.ir_esca)
        boton_D10.place(x=550, y=150)
        boton_D11= tk.Button(self, text="Vomito", **estilo_boton2, command=self.ir_vomi)
        boton_D11.place(x=550, y=200)
        boton_D12 = tk.Button(self, text="Piel, uñas, labios, ojos de color azul, gris o amarilla", **estilo_boton2, command=self.ir_amari)
        boton_D12.place(x=550, y=250)
        boton_D13 = tk.Button(self, text="Síntomas de alergias", **estilo_boton2, command=self.ir_aler)
        boton_D13.place(x=550, y=300)

        # Vista 3
        estilo_boton = {
            'font': ('Arial', 20),
            'fg': 'white',
            'bg': '#2b2895',
            'width': 10,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }

        boton = tk.Button(self, text="Finalizar", **estilo_boton, command=self.abrir_final)
        boton.place(x=750, y=530)
        

        ##### definiciones
    def ir_cabeza(self):
        global enfermedad_guardada
        enfermedad_guardada=1
        self.switch_frame(VentanaGravedad)
    def ir_Golpes(self):
        global enfermedad_guardada
        enfermedad_guardada=2
        self.switch_frame(VentanaGravedad)
    def ir_estomago(self):
        global enfermedad_guardada
        enfermedad_guardada=3
        self.switch_frame(VentanaGravedad)
    def ir_diarrea(self):
        global enfermedad_guardada
        enfermedad_guardada=4
        self.switch_frame(VentanaGravedad)
    def ir_respirar(self):
        global enfermedad_guardada
        enfermedad_guardada=5
        self.switch_frame(VentanaGravedad)
    def ir_hemo(self):
        global enfermedad_guardada
        enfermedad_guardada=6
        self.switch_frame(VentanaGravedad)
    def ir_quema(self):
        global enfermedad_guardada
        enfermedad_guardada=7
        self.switch_frame(VentanaGravedad)
    def ir_mareos(self):
        global enfermedad_guardada
        enfermedad_guardada=8
        self.switch_frame(VentanaGravedad)
    #sí y no
    def ir_nauseas(self):
        global enfermedad_guardada
        enfermedad_guardada=9
        self.switch_frame(VentanaGravedad)
    def ir_esca(self):
        global enfermedad_guardada
        enfermedad_guardada=10
        self.switch_frame(VentanaGravedad)
    def ir_vomi(self):
        global enfermedad_guardada
        enfermedad_guardada=11
        self.switch_frame(VentanaGravedad)
    def ir_amari(self):
        global enfermedad_guardada
        enfermedad_guardada=12
        self.switch_frame(VentanaGravedad)
    def ir_aler(self):
        global enfermedad_guardada
        enfermedad_guardada=13
        self.switch_frame(VentanaGravedad)



    def abrir_final(self):
        self.switch_frame(VentanaFinal)

    def switch_frame(self, frame_class):
        nuevo_frame = frame_class(self)
        nuevo_frame.place(x=0, y=0, relwidth=1, relheight=1)
        
        self._frame = nuevo_frame

class VentanaGravedad(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.crear_interfaz()

    def crear_interfaz(self):
        # Cargar la imagen de fondo de la ventana secundaria
        imagen_fondo_secundaria = Image.open("fondov4.png")
        imagen_fondo_secundaria = imagen_fondo_secundaria.resize((1084, 700))
        self.foto_fondo_secundaria = ImageTk.PhotoImage(imagen_fondo_secundaria)

        # Mostrar la imagen de fondo en un Label
        label_fondo_secundaria = tk.Label(self, image=self.foto_fondo_secundaria)
        label_fondo_secundaria.place(x=0, y=0, relwidth=1, relheight=1)

        # Resto de los elementos de la ventana secundaria...
        # Vista 4
        estilo_boton = {
            'font': ('Arial', 20),
            'fg': 'white',
            'bg': '#2b2895',
            'width': 10,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }

        global enfermedad_guardada
        if enfermedad_guardada >=9:
            self.boton_volver1 = tk.Button(self, text="Sí", **estilo_boton, command=self.ir_si)
            self.boton_volver1.place(x=300, y=300)
            self.boton_volver2 = tk.Button(self, text="No", **estilo_boton, command=self.ir_no)
            self.boton_volver2.place(x=600, y=300)

        else:
            self.boton_volver1 = tk.Button(self, text="Ningun Dolor", **estilo_boton, command=self.ir_no)
            self.boton_volver1.place(x=200, y=300)
            self.boton_volver2 = tk.Button(self, text="Dolor Leve", **estilo_boton, command=self.ir_si)
            self.boton_volver2.place(x=430, y=300)
            self.boton_volver3 = tk.Button(self, text="Dolor Grave", **estilo_boton, command=self.ir_grave)
            self.boton_volver3.place(x=650, y=300)
   
    
    def ir_si(self):
        global enfermedad_guardada
        global Valores_enfe
        Valores_enfe[enfermedad_guardada-1] = 1
        print(Valores_enfe)
        self.switch_frame(VentanaEnfermedad)
    def ir_no(self):
        global enfermedad_guardada
        global Valores_enfe
        Valores_enfe[enfermedad_guardada-1] = 0
        print(Valores_enfe)
        self.switch_frame(VentanaEnfermedad)

    def ir_grave(self):
        global enfermedad_guardada
        global Valores_enfe
        Valores_enfe[enfermedad_guardada-1] = 2
        print(Valores_enfe)
        self.switch_frame(VentanaEnfermedad)


    def switch_frame(self, frame_class):
        nuevo_frame = frame_class(self)
        nuevo_frame.place(x=0, y=0, relwidth=1, relheight=1)
        self._frame = nuevo_frame


class VentanaFinal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.master = parent
        self.crear_interfaz()

    def crear_interfaz(self):
        # Cargar la imagen de fondo de la ventana secundaria
        
        

        # Resto de los elementos de la ventana secundaria...
        global enfermedad_guardada
        global Valores_enfe
        suma=0
        for i in range(0,13):
            aux= Valores_enfe[i]
            suma= suma+ aux

        print(suma)
        resut="no"
        mi_array = []

        cursor.execute("SELECT COALESCE(MAX(id), 0) FROM usuarios.parametros")
        ultima_id2 = cursor.fetchone()[0]
# Utilizar un bucle for para llenar el array
        for i in range(1, 5):  # Rango de 1 a 5 (inclusive)
            
            if i==1:
                consulta = "SELECT bpm FROM usuarios.parametros WHERE id = %s"
            elif i==2:
                consulta = "SELECT fr FROM usuarios.parametros WHERE id = %s"
            elif i==3:
                consulta = "SELECT spo FROM usuarios.parametros WHERE id = %s"
            elif i==4:
                consulta = "SELECT temp FROM usuarios.parametros WHERE id = %s"


        # Ejecutar la consulta con el valor de la variable
            #cursor.execute(consulta, (datos[i],nueva_id,))
            cursor.execute(consulta, (ultima_id2,))

    # Obtener el resultado de la consulta
            mi_array.append(cursor.fetchone())

        print(mi_array)
        
        
       
        if suma <=5:
            imagen_fondo_secundaria = Image.open("resul1.png") 
            resut="Sin urgencia"
        elif suma >=6 and suma <=8:
            imagen_fondo_secundaria = Image.open("resul2.png")
            resut="Precaucion"
        else:
            imagen_fondo_secundaria = Image.open("resul3.png") 
            resut="Peligro"

        #guardando datos en la base de datos
        sql = "INSERT INTO resultados (id, puntaje,resultado) VALUES (%s, %s, %s)"
        val = (nueva_id, suma, resut)
        cursor.execute(sql, val)
        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión con la base de datos
        conexion.close()
        
        imagen_fondo_secundaria = imagen_fondo_secundaria.resize((1084, 700))
        self.foto_fondo_secundaria = ImageTk.PhotoImage(imagen_fondo_secundaria)

        # Mostrar la imagen de fondo en un Label
        label_fondo_secundaria = tk.Label(self, image=self.foto_fondo_secundaria)
        label_fondo_secundaria.place(x=0, y=0, relwidth=1, relheight=1)
       

        
    
    
        # Vista 2
        estilo_boton = {
            'font': ('Arial', 20),
            'fg': 'white',
            'bg': '#2b2895',
            'width': 10,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }
        estilo_eti = {
            'font': ('Arial', 20),
            'fg': 'black',
            'bg': 'white',
            'width': 5,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }
        estilo_eti2 = {
            'font': ('Arial', 15),
            'fg': 'black',
            'bg': 'white',
            'width': 13,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }
        etiqueta = tk.Label(self, text="Frec. Cardiaca",**estilo_eti2)
        etiqueta.place(x=215, y=600)
        etiqueta = tk.Label(self, text=mi_array[0],**estilo_eti)
        etiqueta.place(x=250, y=630)
        etiqueta = tk.Label(self, text="Frec. respiratoria",**estilo_eti2)
        etiqueta.place(x=380, y=600)
        etiqueta = tk.Label(self, text=mi_array[1],**estilo_eti)
        etiqueta.place(x=400, y=630)
        etiqueta = tk.Label(self, text="Temperatura",**estilo_eti2)
        etiqueta.place(x=550, y=600)
        etiqueta = tk.Label(self, text=mi_array[2],**estilo_eti)
        etiqueta.place(x=580, y=630)
        etiqueta = tk.Label(self, text="Sat. oxigeno",**estilo_eti2)
        etiqueta.place(x=720, y=600)
        etiqueta = tk.Label(self, text=mi_array[3],**estilo_eti)
        etiqueta.place(x=750, y=630)
        

        boton = tk.Button(self, text="Terminar", **estilo_boton, command=self.abrir_ventana)
        boton.place(x=900, y=600)

    def abrir_ventana(self):
        restart_program()


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
