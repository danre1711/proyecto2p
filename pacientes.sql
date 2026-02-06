CREATE DATABASE SAP
GO

CREATE TABLE pacientes (
    cedula VARCHAR(10) PRIMARY KEY,
    nombre TEXT,
    apellido TEXT,
    sexo TEXT,
    fecha DATE,
    edad TEXT,
    especialidad TEXT,
    tipo_urgencia TEXT,
    hora TEXT,
    totalpagar REAL
);