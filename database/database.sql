CREATE TABLE dummy (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO dummy (name) VALUES ('Example'), ('Test');

CREATE TABLE routine (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    routine_key CHAR(36) NOT NULL,
    trigger_data JSONB NOT NULL,
    steps_data JSONB NOT NULL,
    created_at VARCHAR(255) NOT NULL,
    UNIQUE (routine_key)
);