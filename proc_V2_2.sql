CREATE PROC INSERTION_WORD
	@pid_word_w INT ,
	@pword VARCHAR (50)  ,
	@plemma VARCHAR (50) ,
	@ppos_tag VARCHAR (50) ,
	@position INT ,
	@pid_article_w INT 
AS
INSERT INTO WORD (id_word,word,lemma,pos_tag,position,id_article) VALUES (@pid_word_w,@pword,@plemma,@ppos_tag,@position,@pid_article_w);

CREATE PROC INSERTION_ARTICLE
	@pid_article_a INT ,
	@pname_np VARCHAR (50) ,
	@pdate_pub date
AS
INSERT INTO ARTICLE (id_article,name_np,date_pub) VALUES (@pid_article_a,@pname_np,@pdate_pub);

CREATE PROC INSERTION_LOCALISATION
	@pid_localisation_l INT , 
	@pcountry VARCHAR (50) , 
	@pcity VARCHAR (50) ,
	@pid_article_l INT 
AS
INSERT INTO LOCALISATION (id_localisation,country,city,id_article) VALUES (@pid_localisation_l,@pcountry,@pcity,@pid_article_l);

