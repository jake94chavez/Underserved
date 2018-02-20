CREATE TABLE games (
  app_id integer NOT NULL,
  app_name text NOT NULL,
  metascore smallint
);

CREATE TABLE filters (
  type text NOT NULL,
  name text NOT NULL,
  label text NOT NULL
);

CREATE TABLE index (
  type text NOT NULL,
  name text NOT NULL,
  app_id integer NOT NULL
);

COPY games (app_id, app_name, metascore)
FROM '/Users/jakechavez/development/Projects/Underserved/main_app/sql-crap/steam_games.csv' DELIMITER '<' CSV HEADER;

COPY filters (type, name, label)
FROM '/Users/jakechavez/development/Projects/Underserved/main_app/sql-crap/steam_filters.csv' DELIMITER ',' CSV HEADER;

COPY index (type, name, app_id)
FROM '/Users/jakechavez/development/Projects/Underserved/main_app/sql-crap/steam_index.csv' DELIMITER ',' CSV HEADER;
