create database colegio;
use colegio;
create table alumnos(
id int primary key auto_increment,
nombre varchar(100) not null,
ape_paterno varchar(50) not null,
ape_materno varchar(50) not null,
correo varchar(250) unique not null,
num_emergencia varchar(10),
curso_id int,
foreign key(curso_id) references cursos(id)
);

alter table cursos drop foreign key cursos_ibfk_1;
alter table cursos drop column alumno_id;

drop table cursos;
drop table alumnos;

create table cursos(
id int primary key auto_increment,
nombre varchar(100) not null,
color text,
dificultad enum('FACIL','MEDIO','DIFICIL')
);

select * from alumnos;
select * from cursos;

select * from cursos c where c.dificultad = 'facil' or 'dificil';  

select * from cursos c where c.color = 'amarillo' or 'celeste' and c.dificultad ='medio' ;  


insert into cursos values (default, 'MATEMATICA', 'AMARILLO','MEDIO'),
						  (default, 'CTS', 'NARANJA','MEDIO'),
                          (default, 'ARTE', 'MORADO','MEDIO'),
                          (default, 'EDUCACION FISICA', 'VERDE','MEDIO'),
                          (default, 'INGLES', 'CELESTE','MEDIO'),
                          (default, 'COMUNICACION', 'ROJO','MEDIO');
                          
INSERT INTO alumnos VALUES  (DEFAULT, 'Eduardo', 'de Rivero', 'Manrique', 'ederiveroman@gmail.com','974207075',1),
                            (DEFAULT, 'Carla', 'Monterrosa', 'Macedo', 'cmonterrosa@gmail.com','974207074',3),
                            (DEFAULT, 'Juan', 'Perez', 'Rodriguez', 'jperez@gmail.com','974207076',5),
                            (DEFAULT, 'Rodrigo', 'Buenaventura', 'Rodrigues', 'rbuenaventura@gmail.com','974159075',2),
                            (DEFAULT, 'Sofia', 'Baldarrago', 'Vera', 'sbaldarrago@gmail.com','972503648',6);


select *
from alumnos
inner join cursos on alumnos.curso_id = cursos.id
where correo like '%gmail%';

select *
from alumnos
left join cursos on alumnos.curso_id = cursos.id;

select *
from alumnos
right join cursos on alumnos.curso_id = cursos.id;


insert into alumnos values(default, 'juan','Maicel','Roman','jsas@ssdds.com','925361048', null);





