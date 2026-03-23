CREATE DATABASE escuela;
USE escuela;
CREATE TABLE Persona (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    cedula VARCHAR(20),
    edad INT
);
INSERT INTO Persona (nombre, apellido, cedula, edad) VALUES
('Joshi', 'Sangurima', '1234567890', 20),
('Joan', 'Atucucho', '0987654321', 25),
('Joseph', 'Segundo', '1122334455', 18),
('Carlos', 'Torres', '5566778899', 30);
SELECT*FROM Persona;
