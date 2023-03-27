# faking-time-demo
Faking time demo repository

Detailed at:


Pre-requisites:
1. docker
2. docker-compose

Execution:
1. Create and start containers
   `docker-compose up`
2. Execute tests
   `docker exec -it faking_time_est pytest -v`
3. Run with fake time
   ```
    docker exec -it faking_time_est bash
    LD_PRELOAD=/usr/lib/aarch64-linux-gnu/faketime/libfaketime.so.1 FAKETIME="2023-09-29 22:00:00" python /app/faking_time_demo/main.py --input-timezone Europe/Amsterdam
    ```
   