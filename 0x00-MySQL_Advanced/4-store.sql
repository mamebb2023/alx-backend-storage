-- Creates a trigger that decreases
-- the quantity of an item after adding a new order
CREATE TRIGGER update_quantity BEFORE INSERT ON `orders`
	FOR EACH ROW UPDATE `items` SET quantity = quantity - NEW.number
	WHERE NEW.item_name = `items`.name;

	
