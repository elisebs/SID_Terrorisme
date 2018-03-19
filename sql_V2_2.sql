/*------------------------------------------------------------
*        Script SQLSERVER 
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
