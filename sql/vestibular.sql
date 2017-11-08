BEGIN;
CREATE TABLE `app_vestibular` (`id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, `nome` varchar(200) NOT NULL);

insert into app_vestibular(nome) values ('FUVEST');
insert into app_vestibular(nome) values ('IMPACTA');

COMMIT;

