--criação da DB
CREATE DATABASE datatran;

--criação da tabela de dias da semana
CREATE TABLE datatran.dias(
        cod SMALLINT PRIMARY KEY,
        descricao VARCHAR(13)
);

--criação da tabela de estados
CREATE TABLE datatran.estados(
        cod SMALLINT PRIMARY KEY,
        descricao VARCHAR(2)
);

--criação da tabela de causas de acidentes
CREATE TABLE datatran.causas(
        cod SMALLINT PRIMARY KEY,
        descricao VARCHAR(76)
);

--criação da tabela de tipos de acidentes
CREATE TABLE datatran.tipos(
        cod SMALLINT PRIMARY KEY,
        descricao VARCHAR(30) 
);

--criação da tabela de classificações de acidentes
CREATE TABLE datatran.classificacoes(
        cod SMALLINT PRIMARY KEY,
        descricao VARCHAR(19)
);


--criação da tabela de condições climáticas
CREATE TABLE datatran.condicoes(
        cod SMALLINT PRIMARY KEY,
        descricao VARCHAR(16)
);

--criação da tabela geral de acidentes
CREATE TABLE datatran.acidentes(
        cod INT PRIMARY KEY,
        data_acidente DATE,
        hora TIME,    
        br SMALLINT,
        mortos SMALLINT,
        feridos_leves SMALLINT,
        feridos_graves SMALLINT,
        ilesos SMALLINT,
        ignorados SMALLINT,
        veiculos SMALLINT
);

--criação da tabela registros    
CREATE TABLE datatran.registros(
        cod_acidente INT,
        cod_dia SMALLINT,
        cod_estado SMALLINT,
        cod_causa SMALLINT,
        cod_tipo SMALLINT,
        cod_classificacao SMALLINT,
        cod_condicao SMALLINT,    
        FOREIGN KEY (cod_acidente) REFERENCES datatran.acidentes (cod),
        FOREIGN KEY (cod_dia) REFERENCES datatran.dias (cod),
        FOREIGN KEY (cod_estado) REFERENCES datatran.estados (cod),
        FOREIGN KEY (cod_causa) REFERENCES datatran.causas (cod),
        FOREIGN KEY (cod_tipo) REFERENCES datatran.tipos (cod),
        FOREIGN KEY (cod_classificacao) REFERENCES datatran.classificacoes (cod),
        FOREIGN KEY (cod_condicao) REFERENCES datatran.condicoes (cod)
); 