create database pruebas;

show databases;

use pruebas;

create table alumnos(
id int primary key auto_increment,
nombre varchar(50) not null,
sexo enum('FEMENNO', 'MASCULINO', 'BINARIX', 'OTRO', 'HELICOPTERO'),
tipo_documento enum('DNI','C.E.','PASAPORTE') default 'DNI',
num_documento varchar(10) not null,
fec_nacimiento datetime
);

select nombre, sexo from alumnos;
select * from alumnos;

insert into alumnos(nombre, sexo, num_documento, fec_nacimiento) values
('Eduardo','MASCULINO','73500746','1992-08-01');

insert into alumnos(nombre, sexo, num_documento, fec_nacimiento) values
('Adolfo','MASCULINO','47213049','1991-04-08');

insert into alumnos(nombre, sexo, num_documento, fec_nacimiento) values
('Irma','FEMENNO','45652132','1995-05-07');

INSERT INTO alumnos (nombre, sexo, num_documento, fec_nacimiento) VALUES
                    ('Ronald', 'BINARIX', '75268256', '1995-07-25'),
                    ('Karim', 'FEMENNO', '85234716', '1991-01-15'),
                    ('Alexa', 'HELICOPTERO', '14729583', '1995-06-08');

INSERT INTO alumnos VALUES 
                    (DEFAULT, 'Romina', 'FEMENNO', 'C.E.', '456789132', '1987-05-14'),
                    (DEFAULT, 'Roberto', 'BINARIX', 'PASAPORTE', '15946789', '1985-01-01'),
                    (DEFAULT, 'Jair', 'MASCULINO', DEFAULT, '34598746', '1995-04-09');
