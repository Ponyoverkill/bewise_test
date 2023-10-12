BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 66d2bc5d8b6e

CREATE TABLE categories (
    id BIGSERIAL NOT NULL, 
    title VARCHAR, 
    created_at TIMESTAMP WITH TIME ZONE, 
    updated_at TIMESTAMP WITH TIME ZONE, 
    PRIMARY KEY (id), 
    UNIQUE (id)
);

CREATE TABLE questions (
    id BIGSERIAL NOT NULL, 
    answer VARCHAR, 
    question VARCHAR, 
    created_at TIMESTAMP WITH TIME ZONE, 
    updated_at TIMESTAMP WITH TIME ZONE, 
    category_id BIGINT, 
    PRIMARY KEY (id), 
    FOREIGN KEY(category_id) REFERENCES categories (id), 
    UNIQUE (id)
);

INSERT INTO alembic_version (version_num) VALUES ('66d2bc5d8b6e') RETURNING alembic_version.version_num;

COMMIT;

