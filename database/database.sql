CREATE TABLE dummy (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO dummy (name) VALUES ('Example'), ('Test');

CREATE TABLE routine (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    routine_key CHAR(36) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    deactivated_on TIMESTAMP
);

CREATE TABLE execution (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    execution_key CHAR(36) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    execution_data JSONB NOT NULL,
    routine_id INTEGER,
    trigger_at TIMESTAMP,
    UNIQUE (execution_key),
    FOREIGN KEY (routine_id) REFERENCES routine(id)
);

CREATE TABLE execution_instance(
    id SERIAL PRIMARY KEY,
    execution_instance_key CHAR(36) NOT NULL,
    execution_id INTEGER,
    created_at TIMESTAMP NOT NULL,
    trigger_at TIMESTAMP NOT NULL,
    triggered_at TIMESTAMP,
    UNIQUE (execution_instance_key),
    FOREIGN KEY (execution_id) REFERENCES execution(id)
);

CREATE TABLE execution_instance_event (
    id SERIAL PRIMARY KEY,
    execution_instance_event_key CHAR(36) NOT NULL,
    execution_instance_id INTEGER,
    created_at TIMESTAMP NOT NULL,
    executed_at TIMESTAMP,
    UNIQUE (execution_instance_event_key),
    FOREIGN KEY (execution_instance_id) REFERENCES execution_instance(id)
);