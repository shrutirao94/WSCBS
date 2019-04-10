DROP TABLE IF EXISTS url;

CREATE TABLE url (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  url_short TEXT UNIQUE NOT NULL,
  url_full TEXT UNIQUE NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
)
