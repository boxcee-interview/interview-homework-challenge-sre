# Challenge 1: Basic search

First a note on the challenge itself: the line count given is incorrect. It should be 3660 instead.

Generally, if this was a "

## Count all lines with `500` HTTP code
```shell
./count-500s.sh
# 714
```

## Count all `GET` requests from `yoko` to `/rrhh` location and if it was successful (`200`)
```shell
./count-yoko-get-requests.sh
# 12
```

## How many requests go to `/`?
```shell
./count-requests-to-root.sh
# 717
```

## Count all lines _without_ `5XX` HTTP code
```shell
./count-without-5xx.sh
# 2191
```

## Replace all `503` HTTP codes by `500`, how many requests have a `500` HTTP code
```shell
./replace-and-count-500s.sh
# 1469
```
