-- Computes and store the average score for a student

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE user_score FLOAT;
	SET user_score = (SELECT AVG(score)
		FROM corrections
		WHERE corrections.user_id = user_id);
	UPDATE users SET average_score = user_score
		WHERE users.id = user_id;
END $$

DELIMITER ; $$
