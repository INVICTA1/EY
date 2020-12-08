
DROP schema if exists `ey`;
CREATE SCHEMA IF NOT EXISTS `ey` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `ey`;



create table `file`(file_id int primary key ,
						file_name varchar(100),
                        upload_datetime datetime);

create table `sheet` (bank_account int  NOT NULL,
						incoming_saldo_asset float NOT NULL,
                        incoming_saldo_liabilities float NOT NULL,
                        turnover_credit float NOT NULL,
                        turnover_debit float NOT NULL,
                        outgoing_saldo_asset float NOT NULL,
                        outgoing_saldo_liabilities float NOT NULL,
                        class_type varchar(100),
						file_id int,
                        constraint `file_sheet`
                        foreign key (file_id) references `file`(file_id) on delete cascade on update cascade);
