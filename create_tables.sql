CREATE DATABASE IF NOT EXISTS doencas;

USE doencas;

CREATE TABLE IF NOT EXISTS TipoDePatogeno (
   id INT AUTO_INCREMENT PRIMARY KEY,
   tipo VARCHAR(12) NOT NULL
);

CREATE TABLE IF NOT EXISTS Patogeno (
   id INT AUTO_INCREMENT PRIMARY KEY,
   nome_cientifico VARCHAR(100) NOT NULL,
   tipopatogeno_id INT,
   FOREIGN KEY (tipopatogeno_id) REFERENCES TipoDePatogeno(id)
);

CREATE TABLE IF NOT EXISTS Doenca (
   id INT AUTO_INCREMENT PRIMARY KEY,
   nome VARCHAR(40) NOT NULL,
   cid VARCHAR(15) NOT NULL UNIQUE,
   patogeno_id INT,
   FOREIGN KEY (patogeno_id) REFERENCES Patogeno(id)
);

CREATE TABLE IF NOT EXISTS NomesPopulares (
   id INT AUTO_INCREMENT PRIMARY KEY,
   nomes_populares VARCHAR(40),
   doenca_id INT,
   FOREIGN KEY (doenca_id) REFERENCES Doenca(id)
);

CREATE TABLE IF NOT EXISTS Sintoma (
   id INT AUTO_INCREMENT PRIMARY KEY,
   nome VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS TaxaDeOcorrencia (
   doenca_id INT,
   sintoma_id INT,
   nivel_ocorrencia ENUM('muito comum', 'comum', 'pouco comum', 'raro', 'muito raro'),
   PRIMARY KEY (doenca_id, sintoma_id),
   FOREIGN KEY (doenca_id) REFERENCES Doenca(id),
   FOREIGN KEY (sintoma_id) REFERENCES Sintoma(id)
);

-- DROP DATABASE doencas;