/*------------------------------------------------------------
*        Script SQLSERVER - CREATION DE LA BASE
------------------------------------------------------------*/

DROP TABLE ARTICLE;
DROP TABLE LOCALISATION;
DROP TABLE WORD;
DROP PROCEDURE INSERTION_ARTICLE;
DROP PROCEDURE INSERTION_LOCALISATION;
DROP PROCEDURE INSERTION_WORD;

/*------------------------------------------------------------
-- Table: WORD
------------------------------------------------------------*/
CREATE TABLE WORD(
	id_word    INT  NOT NULL ,
	word       VARCHAR (50)  ,
	lemma      VARCHAR (50)  ,
	pos_tag    VARCHAR (50)  ,
	position   INT   ,
	id_article INT   ,
	CONSTRAINT prk_constraint_WORD PRIMARY KEY (id_word)
);


/*------------------------------------------------------------
-- Table: LOCALISATION
------------------------------------------------------------*/
CREATE TABLE LOCALISATION(
	id_localisation INT  NOT NULL ,
	country         VARCHAR (50)  ,
	city            VARCHAR (50)  ,
	id_article      INT   ,
	CONSTRAINT prk_constraint_LOCALISATION PRIMARY KEY (id_localisation)
);


/*------------------------------------------------------------
-- Table: ARTICLE
------------------------------------------------------------*/
CREATE TABLE ARTICLE(
	id_article INT  NOT NULL ,
	name_np    VARCHAR (50)  ,
	date_pub    date  ,
	CONSTRAINT prk_constraint_ARTICLE PRIMARY KEY (id_article)
);


ALTER TABLE WORD ADD CONSTRAINT FK_WORD_id_article FOREIGN KEY (id_article) REFERENCES ARTICLE(id_article);
ALTER TABLE LOCALISATION ADD CONSTRAINT FK_LOCALISATION_id_article FOREIGN KEY (id_article) REFERENCES ARTICLE(id_article);

/*-------------------------------------------------------
*        CREATION DES PROCEDURES D'INSERTION
-------------------------------------------------------*/

/*------------------------------------------------------------
-- Procedure: ARTICLE
------------------------------------------------------------*/
CREATE PROC INSERTION_WORD
	@pid_word_w INT ,
	@pword VARCHAR (50)  ,
	@plemma VARCHAR (50) ,
	@ppos_tag VARCHAR (50) ,
	@position INT ,
	@pid_article_w INT 
AS
INSERT INTO WORD (id_word,word,lemma,pos_tag,position,id_article) VALUES (@pid_word_w,@pword,@plemma,@ppos_tag,@position,@pid_article_w);


/*------------------------------------------------------------
-- Procedure: ARTICLE
------------------------------------------------------------*/
CREATE PROC INSERTION_ARTICLE
	@pid_article_a INT ,
	@pname_np VARCHAR (50) ,
	@pdate_pub DATETIME
AS
INSERT INTO ARTICLE (id_article,name_np,date_pub) VALUES (@pid_article_a,@pname_np,@pdate_pub);


/*------------------------------------------------------------
-- Procedure: LOCALISATION
------------------------------------------------------------*/
CREATE PROC INSERTION_LOCALISATION
	@pid_localisation_l INT , 
	@pcountry VARCHAR (50) , 
	@pcity VARCHAR (50) ,
	@pid_article_l INT 
AS
INSERT INTO LOCALISATION (id_localisation,country,city,id_article) VALUES (@pid_localisation_l,@pcountry,@pcity,@pid_article_l);

