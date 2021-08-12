-- @BLOCK
CREATE TABLE Users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    email Varchar(255) ,
    bio TEXT,
    country VARCHAR(2)
);



-- @BLOCK
INSERT INTO Users(email, bio, country)
VALUES
    ('a@gmail.com','First Letter','bd'),
    ('f@gmail.com','First Letter','bd'),
    ('k@gmail.com','First Letter','bd'),
    ('at@gmail.com','First Letter','bd'),
    ('t@gmail.com','First Letter','bd');

-- @BLOCK
ALTER TABLE Users
ADD UNIQUE (email);


-- @BLOCK
DELETE FROM Users where email = 's@gmail.com';

-- @BLOCK
SELECT * FROM Users
ORDER BY ID DESC;

-- @BLOCK
UPDATE Users
SET country = 'FN'
WHERE email = 'f@gmail.com';

-- @BLOCK
SELECT id, country FROM Users
WHERE country = 'bd'
ORDER BY ID DESC
LIMIT 2;

-- @BLOCK



