# Create_Tables.cql
#
# By: Jeff.Davies@datastax.com
#
# The purpose of this script is to create a table that holds a diverse
# amount of data typs so we can test our script.

# We use the demo keyspace for this
use demo;

drop type if exists test_type;

create type test_type (
    record_id uuid,
    quantity double,
    name text
);

drop table if exists test_data;

create table test_data(
    id uuid,
    name text,
    test_items FROZEN<list<test_type>>,
    myblob blob,
    mybool boolean,
    myfloat float,
    PRIMARY KEY((name))
);

-- Test 
-- create table test_data(
--     id uuid,
--     name text,
--     mybool boolean,
--     myfloat float,
--     PRIMARY KEY((name))
-- );