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
                    
delete from alumnos where id>=10 and id <=12;

update alumnos set nombre='Marimar' where id = 8;
update alumnos set num_documento='99564879', nombre = 'Rodrigo' where id = 9;

SELECT * FROM alumnos;

-- 1. Mostrar todos los alumnos que tengan C.E.
SELECT * FROM alumnos WHERE tipo_documento = 'C.E.';
-- 2. Mostrar todos los alumnos que tengan SEXO MASCULINO O FEMENINO
SELECT * FROM alumnos WHERE sexo = 'MASCULINO' OR sexo='FEMENINO';
SELECT * FROM alumnos WHERE sexo IN ('MASCULINO', 'FEMENINO');

-- 3. Mostrar a todos los alumnos que nacieron antes del 1990-01-01
SELECT * FROM alumnos WHERE fec_nacimiento < '1990-01-01';

-- Dame todos los alumnos cuyo nombre contenga la letra a
SELECT nombre FROM alumnos WHERE nombre LIKE '%a%';
-- Dame todos los alumnos cuya ultima letra sea la a
-- con la propiedad BINARY le indicamos que haga la comparacion a nivel de binarios esto incluye la comparacion entre mayus, minus
-- y entre tildes y caracteres especiales como la 'ñ'
SELECT nombre FROM alumnos WHERE nombre LIKE BINARY '%A';

SELECT nombre FROM alumnos WHERE nombre LIKE '%d%u%';

-- Dame todos los alumnos cuya segunda letra sea la o
SELECT nombre FROM alumnos WHERE nombre LIKE '_o%';

-- SELECT nombre FROM alumnos WHERE nombre LIKE 'E__%';

SELECT nombre FROM alumnos WHERE nombre LIKE '%d%u%';
SELECT nombre FROM alumnos WHERE nombre LIKE '%d_u%';


-- 4. Mostrar todos los alumnos cuyo nombre tenga al menos la letra 'n'
SELECT * FROM alumnos WHERE nombre LIKE '%n%';

-- 5. Mostrar todos los alumnos cuyo segundo digito del documento sea '8'
SELECT * FROM alumnos WHERE num_documento LIKE '_8%';

-- 6. Mostrar todos los alumnos cuyo sexo contenga la letra 'i' seguido de una letra cualquiera y luego la letra 'o'
SELECT * FROM alumnos WHERE sexo LIKE '%i_o%';






