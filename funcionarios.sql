CREATE DATABASE IF NOT EXISTS funcionarios;

USE funcionarios;

CREATE TABLE IF NOT EXISTS funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    telefone VARCHAR(15) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    salario int NOT NULL
);

select * from funcionarios