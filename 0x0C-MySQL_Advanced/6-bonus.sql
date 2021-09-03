-- Procedure
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER ;$
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name CHAR(255), IN score INT)
  BEGIN
    IF NOT EXISTS (SELECT p.name FROM projects p WHERE p.name = project_name)
      THEN
        INSERT INTO projects (name) VALUES (project_name);
    END IF ;
    
    SET @project_id = (SELECT p.id FROM projects p WHERE p.name = project_name);
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, @project_id, score);
  END;
;$
DELIMITER ;
