-- swimmers table
create table if not exists swimmers
(
    id   integer     not null
        primary key autoincrement,
    name varchar(32) not null,
    age  integer     not null
);
-- events table
create table if not exists events
(
    id       integer     not null
        primary key autoincrement,
    distance varchar(16) not null,
    stroke   varchar(16) not null
);
-- events times
create table if not exists times
(
    swimmer_id integer     not null,
    event_id   integer     not null,
    time       varchar(16) not null,
    ts         timestamp default current_timestamp
);

