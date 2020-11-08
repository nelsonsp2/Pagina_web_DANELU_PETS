
--Codigo SQL para la agregacion de Admins
INSERT INTO blog_admin (cedula_admin, nombre1, nombre2, apellido1, apellido2) VALUES 
('1000697895','Luna','Gabriela','Duran','Perez');

INSERT INTO blog_admin (cedula_admin, nombre1, nombre2, apellido1, apellido2)

VALUES 
('1000472446','Nelson','Santiago','Guayazan','Palacios');

INSERT INTO blog_admin (cedula_admin, nombre1, nombre2, apellido1, apellido2) VALUES 
('1000591286','Dayana','Valentina','Gonzalez','Vargas');

INSERT INTO blog_admin (cedula_admin, nombre1, nombre2, apellido1, apellido2) VALUES 
('1000047984','Daniel','Felipe','Ramirez','Torres');

SELECT * FROM blog_admin


----------------------------------------------------------------------------------------

--Codigo SQL para la agregacion de categorias
INSERT INTO blog_categoria(id_categoria, nombre_categoria, especie) VALUES ('1', 'Comida',
																	
INSERT INTO blog_categoria(id_categoria, nombre_categoria, especie) VALUES ('2', 'Comida',
																			'Gatos');
INSERT INTO blog_categoria(id_categoria, nombre_categoria, especie) VALUES ('3', 'Collares','Perro');
																	
INSERT INTO blog_categoria(id_categoria, nombre_categoria, especie) VALUES ('4', 'Ropa',	'Conejo');
																		
INSERT INTO blog_categoria(id_categoria, nombre_categoria, especie) VALUES ('5', 'Juguetes','Hamster');

INSERT INTO blog_categoria(id_categoria, nombre_categoria, especie) VALUES ('6', 'Pecera',
																			'Pez');

SELECT * FROM blog_categoria ORDER BY id_categoria																		
																																					
																																					
-----------------------------------------------------------------------------------------------
																			
--Codigo SQL para la agregacion de productos
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('1', 'Pecera_Redonda_Pequeña',30000,10000,'1000472446','6','pecera redonda con 15cm de diametro');
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('2', 'Pecera_Cubica_Mediana',60000,30000,'1000472446','6','pecera cubica con 70cm X 50cm X 60cm ');		
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('3', 'Pecera_Cubica_Grande',100000,50000,'1000472446','6','pecera redonda con 120cm X 80cm X 90cm ');
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones)
VALUES ('4', 'Pecera_Redonda_Mediana',70000,30000,'1000472446','6','pecera redonda con 40cm de diametro');
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones)
VALUES ('5', 'aquario',200000,120000, '1000472446','6','pecera cubica con 180cm X 100cm X 120cm');
																			

---
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('6', 'Rueda de hamster pequeño',15000,5000,'1000047984','5','Rueda de ejercicio para hamster pequeño');
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('7', 'Rueda de hamster mediano',20000,7000,'1000047984','5','Rueda de ejercicio para hamster mediano');		
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones)
VALUES ('8', 'Rueda de hamster mediano',25000,10000,'1000047984','5','Rueda de hamster mediano');
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('9', 'Madera mordisquitos de hamster',10000,3000,'1000047984','5','Juguete de madera para evitar el crecimiento de los dientes');
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('10', 'tuberia hamster',5000,1000, '1000047984','5','tuberia para hamster');

--

INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('11', 'Galletas gato pelo largo MiauMiau',52000,35000,'1000697895','2','Comida premium para gato de pelo largo
		adulto, cantidad: 1 k');
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('12', 'Comida humeda Snackitty',7000,3500,'1000697895','2','Delicioso bocado de comida para
		premiar a gatos de todas las edades, cantidad: 500 gr');		
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones)
VALUES ('13', 'Concentrado para gatos cachorros Misifu' ,35000,22000,'1000697895','2','Comida rica en proteinas y vitaminas
		para gatos entre 1-6 meses, cantidad: 700 gr');
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('14', 'Alimento Wild Animals',60000,30000,'1000697895','2','Comida rica en proteinas
		para gatos adultos que salen mucho de casa, cantidad: 1 k');
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('15', 'Bites de pollo y atun ÑomÑom',15000,9000, '1000697895','2','Pequeños bocaditos para que tu gatito
		disfrute, Cantidad: 30 gr');																			
							
--
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('16', 'Vestido formal',20000,9000, '1000591286','4','Unicos coleres rojo y negro, talla pequeña');

INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('17', 'Vestido formal con cuadros',25000,11000, '1000591286','4','Unicos coleres rojo,blanco y negro, talla media');
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('18', 'Vestido formal con flores',30000,14000, '1000591286','4','Unicos coleres azul y rosado, talla grande');
																			
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('19', 'Chaqueta de invierno',24000,9000, '1000591286','4','Unicos coleres rojo y azul ambas con rayas negras, talla pequeña');
																
INSERT INTO blog_producto(id_producto, nombre_producto,
precio_producto,precio_produccion,admin_producto_id, categoria_producto_id, especificaciones) 
VALUES ('20', 'disfraz de batman',40000,20000, '1000591286','4','trae accesorio como capa y antifaz, talla mediana');																	

																			
SELECT * FROM blog_producto;
--
--Codigo SQL para clientes																			
	
INSERT INTO blog_cliente (id_cliente, nombre1, nombre2, apellido1, apellido2, correo, direccion, ciudad)
VALUES('1000123453', 'Alvaro','Andres','Jimenez', 'Escobar', 'alvaro.jim@gmail.com', 'Calle 80 #18-3', 'Bogotá');
																			
INSERT INTO blog_cliente (id_cliente, nombre1, nombre2, apellido1, apellido2, correo, direccion, ciudad)
VALUES('1543783749', 'Juan','Carlos','Bodoque', 'Gaviria', 'juanc.bodoque@hotmail.com', 'Calle 90 #11-34', 'Bogotá');
																			
INSERT INTO blog_cliente (id_cliente, nombre1, nombre2, apellido1, apellido2, correo, direccion, ciudad)
VALUES('1004598394', 'Maria','Camila','Gomez', 'Lopez', 'marigomez@gmail.com', 'Carrera 189 #1-87', 'Medellín');	
																			
INSERT INTO blog_cliente (id_cliente, nombre1, nombre2, apellido1, apellido2, correo, direccion, ciudad)
VALUES('1046736578', 'Juana','Cecilia','Murcia', 'Amor', 'juana.ce@gmail.com', 'Diagonal 130 #34-6', 'Cali');																			
																			
INSERT INTO blog_cliente (id_cliente, nombre1, nombre2, apellido1, apellido2,correo,direccion,ciudad) 
VALUES('1000365932','Miguel','Angel','Castro','Peralta','miguel.c@gmail.com','Calle 89b #117-20','Bogotá');
																			
INSERT INTO blog_cliente (id_cliente, nombre1, nombre2, apellido1, apellido2,correo,direccion,ciudad)
VALUES('1073456882','Juan','David','Guitierrez','Gonzalez','davidsito@hotmail.com','Calle 35 #80-10','Bogotá');


INSERT INTO blog_cliente (id_cliente, nombre1, nombre2, apellido1, apellido2, correo, direccion, ciudad)
VALUES('1510404942', 'Sonia','Ainos','Lord','Rodriguez', 'panama1234@gmail.com', 'Calle 93 #7-90', 'Barrancabermeja');

INSERT INTO blog_cliente (id_cliente, nombre1, nombre2, apellido1, apellido2, correo, direccion, ciudad)
VALUES('1210304591', 'Tony','Roberto','Paez','Lopez','messitupapa@gmail.com', 'Calle 41 #56-8', 'Bogota');

INSERT INTO blog_cliente (id_cliente, nombre1, nombre2, apellido1, apellido2, correo, direccion, ciudad)
VALUES('1110088812', 'Lola','Mento','Pachon','Calle','lavozcol@gmail.com', 'Calle 13 #4-89', 'Cali');
	
INSERT INTO blog_cliente (id_cliente, nombre1, nombre2, apellido1, apellido2, correo, direccion, ciudad)
VALUES('1110009991', 'Pepi','To','Per','Ez','Pepitoperez@gmail.com', 'Calle 1 #45-9', 'Barrancabermeja');
																			

--------------------------------------------------------------------------------------------------------
																			
--Codigo SQL para agregacion de domiciliarios
																			
INSERT INTO blog_domiciliario (id_domiciliario, nombre1, nombre2, apellido1, apellido2,medio_transporte) 
VALUES('1028673224','Pepe','Alfonzo','Martinez','Soto','bicicleta');
																			
INSERT INTO blog_domiciliario (id_domiciliario, nombre1, nombre2, apellido1, apellido2,medio_transporte) 
VALUES('1022573424','Alejandra','Valentina','Santa maria','de la comarca','moto');
																			
INSERT INTO blog_domiciliario(id_domiciliario,nombre1,nombre2,apellido1,apellido2,medio_transporte)
VALUES ('1000154678','Juan','Camilo','Reyes','Arevalo','Bicicleta');

INSERT INTO blog_domiciliario(id_domiciliario,nombre1,nombre2,apellido1,apellido2,medio_transporte)
VALUES ('1000321788','Enrique','Felipe','Mendoza','Riaño','Bicicleta');

INSERT INTO blog_domiciliario(id_domiciliario,nombre1,nombre2,apellido1,apellido2,medio_transporte)
VALUES ('1000544311','Sara','Lina','Judios','Rubiño','Motocicleta');

INSERT INTO blog_domiciliario(id_domiciliario,nombre1,nombre2,apellido1,apellido2,medio_transporte)
VALUES ('1234567890','Juliana','Felina','Guayazan','Lopez','Moto');
																		
SELECT * FROM blog_domiciliario;			
																			
																			