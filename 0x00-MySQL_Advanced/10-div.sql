-- Function SafeDiv that divides (and returns) the first by 
-- the second number or returns 0 if the second number is equal to 0
DROP IF EXISTS SafeDiv;
CREATE FUNCTION SafeDiv(a INT, b INT)
	RETURNS FLOAT DETERMINISTIC
	RETURN IF (b = 0, 0, a / b);
