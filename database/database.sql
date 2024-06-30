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

INSERT INTO routine (name, routine_key, trigger_data, steps_data, created_at) VALUES ('Teste', 'c575cb4f-9828-4470-91d7-665165a75c21', '{"batata": "cenoura"}', '{"tomate": "alface"}', '2022-09-27T18:00:00Z')