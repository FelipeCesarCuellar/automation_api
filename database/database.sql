CREATE TABLE dummy (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO dummy (name) VALUES ('Example'), ('Test');