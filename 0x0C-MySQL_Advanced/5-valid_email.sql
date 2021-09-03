-- Resets valid_email when email has been updated
DROP TRIGGER IF EXISTS updateEmail;
DELIMITER ;$
CREATE TRIGGER updateEmail BEFORE UPDATE ON users 
  FOR EACH ROW
  BEGIN
    IF NEW.email <> OLD.email
      THEN
        SET NEW.valid_email = 0;
    END IF ;
  END;
;$
DELIMITER ;
