# Challenge 3: Is it running?

I didn't have `docker` available on my machine, so all commands have been done with `podman` instead. However, they are almost the same.
The `server.py` was not modified, for a production environment I would have made at least the port and log level configurable via env vars, though.

## Build the container
```shell
podman build -t myserver .
```

## Run the container
```shell
podman run --rm -p 8081:8080 myserver
```

## Execute the request (in a separate window)
```shell
curl -H "Challenge: orcrist.org" "http://localhost:8081"
# Everything works!
```
