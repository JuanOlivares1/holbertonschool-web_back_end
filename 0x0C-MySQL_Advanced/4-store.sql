-- Triggers
DROP TRIGGER IF EXISTS testref;
DELIMITER ;$
CREATE TRIGGER testref AFTER INSERT ON orders
  FOR EACH ROW
  BEGIN
    UPDATE items
      SET quantity = quantity - NEW.number
      WHERE name = NEW.item_name;
  END;
;$
DELIMITER ;
