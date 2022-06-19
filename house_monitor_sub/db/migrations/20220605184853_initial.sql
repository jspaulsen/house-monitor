-- migrate:up
CREATE EXTENSION IF NOT EXISTS timescaledb;


CREATE TABLE IF NOT EXISTS device_readings (
    id SERIAL,
    reading_ts TIMESTAMPTZ,
    device_id TEXT,
    temperature NUMERIC,
    pressure NUMERIC,
    humidity NUMERIC,

    PRIMARY KEY (reading_ts, device_id, id)
);

SELECT create_hypertable('device_readings', 'reading_ts', chunk_time_interval => INTERVAL '1 day');
ALTER TABLE device_readings SET (timescaledb.compress, timescaledb.compress_orderby = 'reading_ts DESC, id DESC', timescaledb.compress_segmentby = 'device_id');
SELECT add_compression_policy('device_readings', INTERVAL '1d');


-- migrate:down
