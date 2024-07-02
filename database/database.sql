CREATE TABLE dummy (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO dummy (name) VALUES ('Example'), ('Test');

CREATE TABLE routine (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    routine_key CHAR(36) NOT NULL,
    created_at VARCHAR(255) NOT NULL,
    deactivated_on VARCHAR(255) NOT NULL,
);

CREATE TABLE execution (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    execution_key CHAR(36) NOT NULL,
    created_at VARCHAR(255) NOT NULL,
    execution_data JSONB NOT NULL,
    routine_id INTEGER,
    trigger_at VARCHAR(255),
    UNIQUE (execution_key)
    CONSTRAINT fk_execution_routine FOREIGN KEY (routine_id) REFERENCES routine(id)
)

CREATE TABLE execution_event (
    id SERIAL PRIMARY KEY,
    execution_event_key CHAR(36) NOT NULL,
    execution_id INTEGER,
    created_at VARCHAR(255) NOT NULL,
    executed_at VARCHAR(255)
    UNIQUE (execution_event_key)
    CONSTRAINT fk_execution_event_execution FOREIGN KEY (execution_id) REFERENCES execution(id)
)