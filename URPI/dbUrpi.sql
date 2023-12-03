USE master;

DROP DATABASE IF EXISTS dbUrpi;
CREATE DATABASE dbUrpi;

USE dbUrpi;

DROP TABLE IF EXISTS Audio;
CREATE TABLE Audio (
    id INT IDENTITY(1,1) PRIMARY KEY,
    names VARCHAR(80),
    artist VARCHAR(80),
    gender VARCHAR(80),
    archive VARCHAR(255)
);
	
/* Crear vista Audio */
CREATE VIEW List_Audio
	AS
	SELECT
			id AS 'ID',
			names AS 'Nombre de Música',
			artist AS 'Artista',
			gender AS 'Género',
			archive AS 'Archivo'
	FROM Audio
GO


select*from List_Audio;