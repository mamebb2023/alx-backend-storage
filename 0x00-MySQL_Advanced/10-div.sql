-- Function SafeDiv that divides (and returns) the first by 
-- the second number or returns 0 if the second number is equal to 0
CREATE FUNCTION SafeDiv(IN a INT, IN b INT)
	RETURNS INT DETERMINISTIC
	RETURN IF (b = 0, 0, a / b);
