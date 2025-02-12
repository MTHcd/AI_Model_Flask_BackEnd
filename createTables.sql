-- SQLite
CREATE TABLE users (
 id INTEGER,
 email VARCHAR(64) NOT NULL,
 password VARCHAR(64) NOT NULL,
 created_at TIMESTAMP NOT NULL,
 updated_at TIMESTAMP NOT NULL,
 deleted_at TIMESTAMP,
 PRIMARY KEY(id)
);

CREATE TABLE keys (
 id INTEGER,
 user_id INTEGER,
 client_id VARCHAR(64) NOT NULL,
 secret_key VARCHAR(64) NOT NULL,
 created_at TIMESTAMP NOT NULL,
 updated_at TIMESTAMP NOT NULL,
 deleted_at TIMESTAMP,
 PRIMARY KEY(id),
 FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE models (
 id INTEGER,
 name VARCHAR(64) NOT NULL,
 domain VARCHAR(64) NOT NULL,
 url VARCHAR(64) NOT NULL,
 client_id VARCHAR(64) NOT NULL,
 secret_key VARCHAR(64) NOT NULL,
 created_at TIMESTAMP NOT NULL,
 updated_at TIMESTAMP NOT NULL,
 deleted_at TIMESTAMP,
 PRIMARY KEY(id)
);

CREATE TABLE sessions (
 id INTEGER,
 user_id INTEGER,
 model_id INTEGER,
 created_at TIMESTAMP NOT NULL,
 updated_at TIMESTAMP NOT NULL,
 deleted_at TIMESTAMP,
 PRIMARY KEY(id),
 FOREIGN KEY(user_id) REFERENCES users(id),
 FOREIGN KEY(model_id) REFERENCES models(id)
);

CREATE TABLE requests (
 id INTEGER,
 session_id INTEGER,
 type VARCHAR(64) NOT NULL,
 request BLOB NOT NULL,
 response TEXT NOT NULL,
 created_at TIMESTAMP NOT NULL,
 updated_at TIMESTAMP NOT NULL,
 deleted_at TIMESTAMP,
 PRIMARY KEY(id),
 FOREIGN KEY(session_id) REFERENCES sessions(id)
);