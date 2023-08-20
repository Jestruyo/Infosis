USE Infosis;
INSERT INTO USUARIOS (PRIMER_NOMBRE, SEGUNDO_NOMBRE, PRIMER_APELLIDO, SEGUNDO_APELLIDO, EDAD, SEXO, GRUPO, PRIVILEGIO_SERVICIO, TELEFONO_1, TELEFONO_2, CORREO, DIRECCION)
VALUES ('Jesus', 'David', 'Trujillo', 'Teheran', 31, 'M', 4, 6, 3003758315, null, 'jesusdavidtrujilloteheran@gmail.com', 'Carrera 6f # 76 - 22');

-- Query para insertar datos en la tabla usuarios.
USE Infosis;
INSERT INTO USUARIOS (PRIMER_NOMBRE, SEGUNDO_NOMBRE, PRIMER_APELLIDO, SEGUNDO_APELLIDO, EDAD, SEXO, GRUPO, PRIVILEGIO_SERVICIO, TELEFONO_1, TELEFONO_2, CORREO, DIRECCION)
VALUES
  ('Yovanni', 'Daniel', 'Meza', 'Perez', 32, 'M', NULL, 2, '3009875432', NULL, 'mezaj@gmail.com', 'Carrera 44 # 32 -56');

-- Query para insertar varios campos en la tabla grupos.
USE Infosis;
INSERT INTO GRUPOS (SUPER_GRUPO, SIERVO_GRUPO) VALUES (11,13);

-- Query para insertar un dato en la tabla grupos.
INSERT INTO GRUPOS (TIPO) VALUES ('Anciano');

-- Query para eliminar un campo especifico de la tabla usuarios por el id.
DELETE FROM USUARIOS WHERE ID = 1;

-- Query para borrar todos los datos de la tabla usuarios.
TRUNCATE TABLE USUARIOS;

-- Query para resetear el autoincremento de la tabla usuarios.
ALTER TABLE USUARIOS AUTO_INCREMENT = 1;

-- Query para crear la tabla usuarios.
USE Infosis;
CREATE TABLE USUARIOS (
ID INT PRIMARY KEY AUTO_INCREMENT,
PRIMER_NOMBRE VARCHAR(50) NOT NULL,
SEGUNDO_NOMBRE VARCHAR(50),
PRIMER_APELLIDO VARCHAR(70) NOT NULL,
SEGUNDO_APELLIDO VARCHAR(70),
EDAD INT(100) NOT NULL,
SEXO VARCHAR(10) NOT NULL,
GRUPO INT(20) NOT NULL,
PRIVILEGIO_SERVICIO INT(10),
TELEFONO_1 INT(50) NOT NULL,
TELEFONO_2 INT(50),
CORREO VARCHAR(100),
DIRECCION VARCHAR(200) NOT NULL
);

-- Query para crear la tabla grupos.
CREATE TABLE GRUPOS (
ID INT PRIMARY KEY AUTO_INCREMENT,
SUPER_GRUPO INT NOT NULL,
SIERVO_GRUPO INT NOT NULL,
NUMERO_DE_INTEGRANTES INT(50)
);

-- Query para crear la tabla informes.
CREATE TABLE INFORMES (
ID INT PRIMARY KEY AUTO_INCREMENT,
ID_USUARIO INT NOT NULL,
ID_GRUPO INT NOT NULL,
PRIMER_NOMBRE VARCHAR(50) NOT NULL,
SEGUNDO_NOMBRE VARCHAR(50),
PRIMER_APELLIDO VARCHAR(70) NOT NULL,
SEGUNDO_APELLIDO VARCHAR(70),
FECHA_INFO DATE
);

-- QUery para crear la tabla privilegios.
CREATE TABLE PRIVILEGIOS (
ID INT PRIMARY KEY AUTO_INCREMENT,
TIPO VARCHAR(150) NOT NULL
);

-- Query para agregar una llave foranea a la tabla usuarios.
USE Infosis;
ALTER TABLE USUARIOS
ADD FOREIGN KEY (GRUPO) REFERENCES GRUPOS(ID);

-- Query para modificar el tipo de datos y caracteristicas de un campo especifico de la tabla usuarios.
ALTER TABLE USUARIOS MODIFY TELEFONO_2 varchar(100) DEFAULT NULL;

-- Query para actualizar el campo grupo de cada usuario.
UPDATE USUARIOS SET GRUPO = 5 WHERE ID = 13;

-- Consulta para traer los uruarios de cada grupo.
SELECT * FROM USUARIOS WHERE GRUPO = 2;
