CREATE TABLE IF NOT EXISTS User 
(
    id INTEGER NOT NULL,
    pseudo VARCHAR(20),
    email VARCHAR,
    level INTEGER,
    class VARCHAR,
    phone VARCHAR(8),
    picture VARCHAR,
    mdpHash VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS Project
(
    idProject INTEGER NOT NULL,
    idLeader INTEGER,
    name VARCHAR,
    summary VARCHAR,
    description VARCHAR,
    picture VARCHAR,
    PRIMARY KEY (idProject)
);

CREATE TABLE IF NOT EXISTS Groupe
(
    idProject INTEGER,
    idUser INTEGER,
    FOREIGN KEY (idProject) REFERENCES Project(idProject),
    FOREIGN KEY (idUser) REFERENCES User(id),
    PRIMARY KEY (idProject, idUser)
);

CREATE TABLE IF NOT EXISTS Freelancer
(
    idUser INTEGER,
    price INTEGER,
    skill VARCHAR,
    description VARCHAR,
    PRIMARY KEY (idUSer),
    FOREIGN KEY (idUser) REFERENCES User(id)
);

CREATE TABLE IF NOT EXISTS Tag
(
    id INTEGER NOT NULL,
    name VARCHAR,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS TagRelation
(
    idProject INTEGER,
    idTag INTEGER,
    FOREIGN KEY (idProject) REFERENCES User(id),
    FOREIGN KEY (idTag) REFERENCES Tag(id),
    PRIMARY KEY (idProject, idTag)
);

