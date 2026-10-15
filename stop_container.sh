#!/bin/bash
set +e
docker stop student-app
docker rm student-app
exit 0
