USE comments_keyspace;

DROP TABLE comments;

CREATE TABLE comments (
    answer_id int,
    user_id int,
    publication_ts timestamp,
    body text,
    PRIMARY KEY(answer_id, user_id, publication_ts)
);

INSERT INTO comments_keyspace.comments (answer_id, user_id, publication_ts, body)
VALUES (?, ?, ?, ?)
IF NOT EXISTS;
