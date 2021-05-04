#creando servidor, flask permite crear el servidor
#importando librerías y métodos para la creación y desarrollo de la aplicación
from flask import Flask
from flask import jsonify
from flask import request
#forma que tienen las aplicaciones para manejar seguridad
from flask_cors import CORS
from Persona import Persona
from Admin import Admin
from Doctor import Doctor
from Medicamentos import Medicamento
from Cita import Cita
from Factura import Factura
from Receta import Receta
from Compra import Compra
import json


#Listas
Pacientes = []
Enfermeras = []
Doctores = []
Medicamentos = []
contador = 0
Citas = []
Facturas = []
Recetas = []
Compras = []
admin = Admin('Carlos', 'Jiménez', 'admin', '1234')
Aplicacion = Flask(__name__)
CORS(Aplicacion)


"""#Definiendo el url al que quiero ingresar y un método
@Aplicacion.route('/', methods = ['GET'])
def rutaInicial():
    print("Hola alumnos")
    return("Hola mundo")


@Aplicacion.route('/', methods = ['POST'])
def rutaPos():
    print("Hola desde un Post")
    persona = {"Mensaje": "Se hizo el POST correctamente"}
    return(jsonify(persona))"""

########################################################################################################
############################### MÉTODOS PARA OBTENER TODA LA INFO DE UN USUARIO ########################

#Método para información paciente
@Aplicacion.route('/Pacientes', methods = ['GET'])
def ObtenerPaciente():
    global Pacientes 
    Datos = []
    for persona in Pacientes:

        cpaciente = {
            'Nombre' : persona.getNombre(),
            'Apellido' : persona.getApellido(),
            'Fecha' : persona.getFecha(),
            'Sexo' : persona.getFecha(),
            'Usuario' : persona.getUsuario(),
            'Contraseña' : persona.getContra(),
            'Teléfono' : persona.getTel()
                   }
        Datos.append(cpaciente)
    return(jsonify(Datos))

#Método para información enfermera
@Aplicacion.route('/Enfermeras', methods = ['GET'])
def ObtenerEnfermera():
    global Enfermeras 
    Datos = []
    for persona in Enfermeras:

        cenfermera = {
            'Nombre' : persona.getNombre(),
            'Apellido' : persona.getApellido(),
            'Fecha' : persona.getFecha(),
            'Sexo' : persona.getFecha(),
            'Usuario' : persona.getUsuario(),
            'Contraseña' : persona.getContra(),
            'Teléfono' : persona.getTel()
                   }
        Datos.append(cenfermera)
    return(jsonify(Datos))

#Método para información doctor
@Aplicacion.route('/Doctores', methods = ['GET'])
def ObtenerDoctor():
    global Doctores
    Datos = []
    for Doctor in Doctores:

        cdoctor = {
            'Nombre' : Doctor.getNombre(),
            'Apellido' : Doctor.getApellido(),
            'Fecha' : Doctor.getFecha(),
            'Sexo' : Doctor.getFecha(),
            'Usuario' : Doctor.getUsuario(),
            'Contraseña' : Doctor.getContra(),
            'Especialidad' : Doctor.getSpecialty(),
            'Teléfono' : Doctor.getTel()
                   }
        Datos.append(cdoctor)
    return(jsonify(Datos))

##########################################################################################################
######################################## MÉTODO PARA LAS TABLAS ##########################################

#Método para tabla paciente
@Aplicacion.route('/ObtenerPacientes', methods = ['GET'])
def ObtenerPacientes():
    global Pacientes 
    Datos = []
    for persona in Pacientes:

        cpaciente = {
            'Nombre' : persona.getNombre(),
            'Apellido' : persona.getApellido(),
            'Fecha' : persona.getFecha(),
            'Sexo' : persona.getSexo(),
            'Usuario' : persona.getUsuario(),
            'Contraseña' : persona.getContra(),
            'Teléfono' : persona.getTel()
                   }
        Datos.append(cpaciente)
    return(jsonify(Datos))

#Método para tabla doctores
@Aplicacion.route('/ObtenerDoctores', methods = ['GET'])
def ObtenerDoctores():
    global Doctores 
    Datos = []
    for Doctor in Doctores:

        cdoctor = {
            'Nombre' : Doctor.getNombre(),
            'Apellido' : Doctor.getApellido(),
            'Fecha': Doctor.getFecha(),
            'Sexo' : Doctor.getSexo(),
            'Usuario' : Doctor.getUsuario(),
            'Contraseña' : Doctor.getContra(),
            'Especialidad' : Doctor.getSpecialty()
                   }
        Datos.append(cdoctor)
    return(jsonify(Datos))

#Método para tabla enfermeras
@Aplicacion.route('/ObtenerEnfermeras', methods = ['GET'])
def ObtenerEnfermeras():
    global Enfermeras 
    Datos = []
    for Persona in Enfermeras:

        cenfermera = {
            'Nombre' : Persona.getNombre(),
            'Apellido' : Persona.getApellido(),
            'Fecha' : Persona.getFecha(),
            'Sexo' : Persona.getSexo(),
            'Usuario' : Persona.getUsuario(),
            'Contraseña' : Persona.getContra(),
            'Teléfono' : Persona.getTel()
                   }
        Datos.append(cenfermera)
    return(jsonify(Datos))

#Método para tabla medicamentos
@Aplicacion.route('/ObtenerMedicamentos', methods = ['GET'])
def ObtenerMedicamentos():
    global Medicamentos
    Datos = []
    for Medicamento in Medicamentos:

        cenmed = {
            'Código' : Medicamento.getCode(),
            'Nombre' : Medicamento.getNombre(),
            'Precio' : Medicamento.getPrecio(),
            'Descripción' : Medicamento.getDescripcion(),
            'Cantidad' : Medicamento.getCantidad()
                   }
        Datos.append(cenmed)
    return(jsonify(Datos))

#Método para tabla citas pendientes
@Aplicacion.route('/ObtenerCitas', methods = ['GET'])
def ObtenerCitasP():
    global Citas
    Datos = []
    for Cita in Citas:
        if(Cita.getEstado() == 'Pendiente'):
            cita = {
                'Fecha' : Cita.getFecha(),
                'Hora' : Cita.getHora(),
                'Motivo' : Cita.getMotivo(),
                'Paciente' : Cita.getId()
                   }
            Datos.append(cita)
    return(jsonify(Datos))

    #Método para tabla citas aceptadas
@Aplicacion.route('/ObtenerCitasA', methods = ['GET'])
def ObtenerCitasA():
    global Citas
    Datos = []
    for Cita in Citas:
        if(Cita.getEstado() == 'Aceptada'):
            cita = {
                'Fecha' : Cita.getFecha(),
                'Hora' : Cita.getHora(),
                'Motivo' : Cita.getMotivo(),
                'Paciente' : Cita.getId()
                   }
            Datos.append(cita)
    return(jsonify(Datos))

#########################################################################################################
########################################### MÉTODOS PARA RECIBIR PARÁMETRO ##############################

#Método para recibir solo un usuario, entonces se le pone parámetro
@Aplicacion.route('/Paciente/<string:usuario>', methods = ['GET'])
def ObtenerUsuarioP(usuario):
    global Pacientes 
    for persona in Pacientes:

        if persona.getUsuario() == usuario:
            cpaciente = {
            'Nombre' : persona.getNombre(),
            'Apellido' : persona.getApellido(),
            'Fecha' : persona.getFecha(),
            'Sexo' : persona.getSexo(),
            'Contrasena' : persona.getContra(),
            'Telefono' : persona.getTel()
                   }
            return(jsonify(cpaciente))
            
    salida = {'Mensaje' : 'No existe ese usuario'}
    return(jsonify(salida))

#Método para información enfermera
@Aplicacion.route('/Enfermeras/<string:usuario>', methods = ['GET'])
def ObtenerUsuarioE(usuario):
    global Enfermeras 
    for persona in Enfermeras:

        if persona.getUsuario() == usuario:
            cenfermera = {
            'Nombre' : persona.getNombre(),
            'Apellido' : persona.getApellido(),
            'Fecha' : persona.getFecha(),
            'Sexo' : persona.getSexo(),
            'Usuario' : persona.getUsuario(),
            'Contrasena' : persona.getContra(),
            'Telefono' : persona.getTel()
                   }
            return(jsonify(cenfermera))
    salida = {'Mensaje' : 'No existe ese usuario'}
    return(jsonify(salida))

#Método para información doctor
@Aplicacion.route('/Doctores/<string:usuario>', methods = ['GET'])
def ObtenerUsuarioD(usuario):
    global Doctores
    for Doctor in Doctores:

        if Doctor.getUsuario() == usuario:
            cdoctor = {
            'Nombre' : Doctor.getNombre(),
            'Apellido' : Doctor.getApellido(),
            'Fecha' : Doctor.getFecha(),
            'Sexo' : Doctor.getSexo(),
            'Usuario' : Doctor.getUsuario(),
            'Contrasena' : Doctor.getContra(),
            'Especialidad' : Doctor.getSpecialty(),
            'Telefono' : Doctor.getTel()
                   }
            return(jsonify(cdoctor))
    salida = {'Mensaje' : 'No existe ese usuario'}
    return(jsonify(salida))

#Método para información medicamento
@Aplicacion.route('/Medicamentos/<string:code>', methods = ['GET'])
def ObtenerCodM(code):
    global Medicamentos
    for Medicamento in Medicamentos:

        if Medicamento.getCode() == code:
            cmed = {
            'Nombre' : Medicamento.getNombre(),
            'Precio' : Medicamento.getPrecio(),
            'Descripción' : Medicamento.getDescripcion(),
            'Cantidad' : Medicamento.getCantidad(),
            'Código' : Medicamento.getCode()
                   }
            return(jsonify(cmed))
    salida = {'Mensaje' : 'No existe ese usuario'}
    return(jsonify(salida))

#Método para recibir usuario 
@Aplicacion.route('/Comprobar/<string:usuario>', methods = ['GET'])
def EncontrarEstado(usuario):
    global Citas
    for Cita in Citas:
        if Cita.getId() == usuario:
            Estado = {
            'Estado' : Cita.getEstado()
                   }
            return(jsonify(Estado))
    salida = {'Estado' : 'No tiene citas creadas'}
    return(jsonify(salida))

#Método para obtener la compra

@Aplicacion.route('/Compra/<string:id>', methods=['GET'])
def ObtenerCompra(id):
    global Compras
    for Compra in Compras:
        if(Compra.getId() == id):
            Medicina = Compra.getMedicamentos()
            objeto = {
                'Compra': Compra.getId(),
                'Medicina': Medicina
            }
    return(jsonify(objeto))


#########################################################################################################
########################################### MÉTODOS PARA CREAR USUARIO ##################################

#Método para agregar pacientes
@Aplicacion.route('/NuevoPaciente', methods = ['POST'])
def AgregarPaciente():
    global Pacientes
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    fecha = request.json['fecha']
    sexo = request.json['sexo']
    usuario = request.json['usuario']
    contrasena = request.json['contrasena']
    telefono = request.json['telefono']
    if(len(contrasena) >= 8):
        nuevopaciente = Persona(nombre, apellido, fecha, sexo, usuario, contrasena, telefono)
        Pacientes.append(nuevopaciente)
        for i in range(len(Pacientes)):
            print(Pacientes[i].getNombre())
        return jsonify({'Mensaje':'Usuario creado con éxito.'})
    else:
        return jsonify({'Mensaje':'La contraseña debe contener más de 8 caracteres'})


#Método para agregar doctores
@Aplicacion.route('/NuevoDoctor', methods = ['POST'])
def AgregarDoctor():
    global Doctores
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    fecha = request.json['fecha']
    sexo = request.json['sexo']
    usuario = request.json['usuario']
    contrasena = request.json['contrasena']
    especialidad = request.json['especialidad']
    telefono = request.json['telefono']
    NuevoDoctor = Doctor(nombre, apellido, fecha, sexo, usuario, contrasena, especialidad, telefono)
    Doctores.append(NuevoDoctor)
    for i in range(len(Doctores)):
        print(Doctores[i].getNombre())
    return jsonify({'Mensaje':'Usuario creado con éxito.'})

#Método para agregar enfermeras
@Aplicacion.route('/NuevaEnfermera', methods = ['POST'])
def AgregarEnfermera():
    global Enfermeras
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    fecha = request.json['fecha']
    sexo = request.json['sexo']
    usuario = request.json['usuario']
    contrasena = request.json['contrasena']
    telefono = request.json['telefono']
    NuevaEnfermera = Persona(nombre, apellido, fecha, sexo, usuario, contrasena, telefono)
    Enfermeras.append(NuevaEnfermera)
    for i in range(len(Enfermeras)):
        print(Enfermeras[i].getNombre())
    return jsonify({'Mensaje':'Usuario creado con éxito.'})

#Método para agregar medicamentos
@Aplicacion.route('/NuevoMedicamento', methods = ['POST'])
def AgregarMedicina():
    global Medicamentos
    global contador
    código = contador
    nombre = request.json['nombre']
    precio = request.json['precio']
    descripción = request.json['descripción']
    cantidad = request.json['cantidad']
    NuevoMedicamento = Medicamento(código, nombre, precio, descripción, cantidad)
    Medicamentos.append(NuevoMedicamento)
    contador +=1
    for i in range(len(Medicamentos)):
        print(Medicamentos[i].getNombre())
    return jsonify({'Mensaje':'Medicamento creado con éxito.'})

#Método para crear citas
@Aplicacion.route('/NuevaCita', methods = ['POST'])
def CrearCita():
    global Citas
    fecha = request.json['fecha']
    hora = request.json['hora']
    motivo = request.json['motivo']
    estado = request.json['estado']
    usuario = request.json['usuario']
    for i in range(len(Citas)):
        if (Citas[i].getId() == usuario):
            if (Citas[i].getEstado() == 'Pendiente'):
                return jsonify({'Mensaje':'No puede crear una cita, tiene una cita pendiente.'})
            if (Citas[i].getEstado() == 'Aceptada'):
                return jsonify({'Mensaje':'No puede crear una cita, tiene una cita aceptada.'})
            if (Citas[i].getEstado() == 'Aceptada' or Citas[i].getEstado() == 'Rechazada'):
                NuevaCita = Cita(usuario, fecha, hora, motivo, estado, '')
                Citas.append(NuevaCita)
                return jsonify({'Mensaje':'Cita creada con éxito.'})
    NuevaCita = Cita(usuario, fecha, hora, motivo, estado, '')
    Citas.append(NuevaCita)
    return jsonify({'Mensaje':'Cita creada con éxito.'})

    #Método para facturas
@Aplicacion.route('/NuevaFactura', methods = ['POST'])
def CrearFacura():
    global Facturas
    fecha = request.json['fecha']
    nombre = request.json['nombre']
    doctor = request.json['doctor']
    precio = request.json['precio']
    costoop = request.json['costoop']
    costoin = request.json['costoin']
    total = request.json['total']
    NuevaFactura = Factura(fecha, nombre, doctor, precio, costoop, costoin, total)
    Citas.append(NuevaFactura)
    return jsonify({'Mensaje':'Factura creada con éxito.'})

#Método para recetas
@Aplicacion.route('/NuevaReceta', methods = ['POST'])
def CrearReceta():
    global Recetas
    fecha = request.json['fecha']
    nombre = request.json['nombre']
    padecimiento = request.json['padecimiento']
    descripción = request.json['descripción']
    NuevaReceta = Receta(fecha, nombre, padecimiento, descripción)
    Citas.append(NuevaReceta)
    return jsonify({'Mensaje':'Receta creada con éxito.'})

#Método para crear un compra
@Aplicacion.route('/Compra', methods=['POST'])
def CrearCompra():
    global Compras
    id = request.json['id']
    medicina = request.json['medicinas']
    nuevo = Compra(id,medicina)
    Compras.append(nuevo)
    return jsonify({'Mensaje':'Compra guardada con éxito.'})

#########################################################################################################
########################################### MÉTODOS PARA ACTUALIZAR INFO ################################

#Método para actualizar info paciente
@Aplicacion.route('/Pacientes/<string:usuario>', methods = ['PUT'])
def ActualizarPaciente(usuario):
    global Pacientes
    contra = request.json['contrasena']
    for i in range(len(Pacientes)):
        if usuario == Pacientes[i].getUsuario():
            if(len(contra) >= 8):
                Pacientes[i].setNombre(request.json['nombre'])
                Pacientes[i].setApellido(request.json['apellido'])
                Pacientes[i].setFecha(request.json['fecha'])
                Pacientes[i].setContra(request.json['contrasena'])
                return jsonify({'Mensaje':'Información actualizada exitosamente.'})
            return jsonify({'Mensaje':'La contraseña debe tener al menos 8 caracteres.'})
    return jsonify({'Mensaje':'No se encontró la información del usuario.'})

#Método para actualizar info enfermera
@Aplicacion.route('/Enfermeras/<string:usuario>', methods = ['PUT'])
def ActualizarEnfermera(usuario):
    global Enfermeras
    contra = request.json['contrasena']
    for i in range(len(Enfermeras)):
        if usuario == Enfermeras[i].getUsuario():
            if(len(contra) >= 8):
                Enfermeras[i].setNombre(request.json['nombre'])
                Enfermeras[i].setApellido(request.json['apellido'])
                Enfermeras[i].setFecha(request.json['fecha'])
                Enfermeras[i].setContra(request.json['contrasena'])
                return jsonify({'Mensaje':'Información actualizada exitosamente.'})
            return jsonify({'Mensaje':'La contraseña debe tener al menos 8 caracteres.'})
    return jsonify({'Mensaje':'No se encontró la información del usuario.'})

#Método para actualizar info doctor
@Aplicacion.route('/Doctores/<string:usuario>', methods = ['PUT'])
def ActualizarDoctor(usuario):
    global Doctores
    for i in range(len(Doctores)):
        if usuario == Doctores[i].getUsuario():
            Doctores[i].setNombre(request.json['nombre'])
            Doctores[i].setApellido(request.json['apellido'])
            Doctores[i].setFecha(request.json['fecha'])
            Doctores[i].setContra(request.json['contrasena'])
            Doctores[i].setSpecialty(request.json['especialidad'])
            return jsonify({'Mensaje':'Información actualizada exitosamente.'})
    return jsonify({'Mensaje':'No se encontró la información del usuario.'})

#Método para actualizar info medicina
@Aplicacion.route('/Medicamentos/<string:code>', methods = ['PUT'])
def ActualizarMedicina(code):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if code == Medicamentos[i].getCode():
            Medicamentos[i].setNombre(request.json['nombre'])
            Medicamentos[i].setPrecio(request.json['precio'])
            Medicamentos[i].setDescripcion(request.json['descripción'])
            Medicamentos[i].setCantidad(request.json['cantidad'])
            return jsonify({'Mensaje':'Información actualizada exitosamente.'})
    return jsonify({'Mensaje':'No se encontró la información del Medicamento.'})

    #Método para actualizar estado de la cita
@Aplicacion.route('/Cita/<string:usuario>', methods = ['PUT'])
def ActualizarEstado(usuario):
    global Citas
    for i in range(len(Citas)):
        if usuario == Citas[i].getId():
            Citas[i].setEstado(request.json['Estado'])
            return jsonify({'Mensaje':'Información actualizada exitosamente.'})
    return jsonify({'Mensaje':'No se encontró una cita asignada a este usuario.'})


#Método para actualizar estado de la cita
@Aplicacion.route('/CitaA/<string:usuario>', methods = ['PUT'])
def ActualizarEyD(usuario):
    global Citas
    for i in range(len(Citas)):
        if usuario == Citas[i].getId():
            Citas[i].setEstado(request.json['Estado'])
            Citas[i].setDoctor(request.json['Doctor'])
            return jsonify({'Mensaje':'Información actualizada exitosamente.'})
    return jsonify({'Mensaje':'No se encontró una cita asignada a este usuario.'})

#########################################################################################################
########################################### MÉTODOS PARA EL LOGIN #######################################

#Método para buscar usuario
@Aplicacion.route('/Login', methods = ['POST'])
def Login():
    global Pacientes
    usuario = request.json['usuario']
    contrasena = request.json['contrasena']
    for i in range(len(Pacientes)):
        if usuario == Pacientes[i].getUsuario() and contrasena == Pacientes[i].getContra():
            return jsonify({'Tipo': 1})
    for i in range(len(Doctores)):
        if usuario == Doctores[i].getUsuario() and contrasena == Doctores[i].getContra():
            return jsonify({'Tipo': 2})
    for i in range(len(Enfermeras)):
        if usuario == Enfermeras[i].getUsuario() and contrasena == Enfermeras[i].getContra():
            return jsonify({'Tipo': 3})
    if usuario == admin.getUsuario() and contrasena == admin.getContra():
        return jsonify({'Tipo': 4})
    return jsonify({'Mensaje':'Contraseña y/o usuario incorrectos.'})

####################################################################################################################
######################################## MÉTODOS PARA ELIMINAR #####################################################

#Eliminar usuario paciente
@Aplicacion.route('/Pacientes/<string:usuario>', methods = ['DELETE'])
def EliminarPaciente(usuario):
    global Pacientes
    for i in range(len(Pacientes)):
        if usuario == Pacientes[i].getUsuario():
            del Pacientes[i]
            print('eliminado')
            return jsonify({'Mensaje':'Usuario eliminado con éxito.'})     
    return jsonify({'Mensaje':'Usuario no encontrado.'})

#Eliminar usuario enfermera
@Aplicacion.route('/Enfermeras/<string:usuario>', methods = ['DELETE'])
def EliminarEnfermera(usuario):
    print(usuario)
    global Enfermeras
    for i in range(len(Enfermeras)):
        if usuario == Enfermeras[i].getUsuario():
            del Enfermeras[i]
            print('eliminado')
            return jsonify({'Mensaje':'Usuario eliminado con éxito.'})     
    return jsonify({'Mensaje':'Usuario no encontrado.'})

#Eliminar usuario doctor
@Aplicacion.route('/Doctores/<string:usuario>', methods = ['DELETE'])
def EliminarDoctores(usuario):
    global Doctores
    for i in range(len(Doctores)):
        if usuario == Doctores[i].getUsuario():
            del Doctores[i]
            print('eliminado')
            return jsonify({'Mensaje':'Usuario eliminado con éxito.'})     
    return jsonify({'Mensaje':'Usuario no encontrado.'})

#Eliminar usuario medicamento
@Aplicacion.route('/Medicamentos/<string:code>', methods = ['DELETE'])
def EliminarMedicamento(code):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if code == Medicamentos[i].getCode():
            del Medicamentos[i]
            print('eliminado')
            return jsonify({'Mensaje':'Usuario eliminado con éxito.'})     
    return jsonify({'Mensaje':'Usuario no encontrado.'})



#Levantar la aplicación
if __name__ == "__main__":
    Aplicacion.run(host = "0.0.0.0", port=3000, debug = True)

