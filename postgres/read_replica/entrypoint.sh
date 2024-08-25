#!/bin/sh -xeu

pg_basebackup \\
	-h postgres \\
	-D ${PGDATA} \\
	-S my_replication_slot \\
	-X stream \\
	-U replicator \\
	-R || true

/usr/local/bin/docker-entrypoint.sh postgres