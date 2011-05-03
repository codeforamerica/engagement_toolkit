CREATE TABLE forum_mysqlftsindex (
	id int NOT NULL AUTO_INCREMENT,
	node_id int NOT NULL UNIQUE,
	body longtext NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (node_id) REFERENCES forum_node (id)   ON UPDATE CASCADE ON DELETE CASCADE,
	FULLTEXT (body)
) ENGINE=`MyISAM`;

ALTER TABLE forum_mysqlftsindex CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;

delimiter |

CREATE TRIGGER fts_on_insert AFTER INSERT ON forum_node
  FOR EACH ROW
  BEGIN
    INSERT INTO forum_mysqlftsindex (node_id, body) VALUES (NEW.id, UPPER(CONCAT_WS('\n', NEW.title, NEW.body, NEW.tagnames)));
  END;
|

delimiter |

CREATE TRIGGER fts_on_update AFTER UPDATE ON forum_node
  FOR EACH ROW
  BEGIN
    UPDATE forum_mysqlftsindex SET body = UPPER(CONCAT_WS('\n', NEW.title, NEW.body, NEW.tagnames)) WHERE node_id = NEW.id;
  END;

|

INSERT INTO forum_mysqlftsindex (node_id, body) SELECT id, UPPER(CONCAT_WS('\n', title, body, tagnames)) FROM forum_node;