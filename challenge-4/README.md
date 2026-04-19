# Challenge 4: What's wrong?

This one was trial-and-error for me.

## Recon
```shell
cat blackbox
# I was able to see the expected success from the challenge, as well as the expected failure AND a third human-readable string "the_magic_filez.txt"
```

## Run the binary
```shell
./blackbox
# exec format error: Expected though, you mentioned it in the tip. I am on a Mac.
```

## Wrap the binary into something I can run

First I tried with Alpine and ran into some lib issues. Then switched to Debian. Had to Google for this.

```shell
# Build the wrapper
podman build -t blackbox -f Dockerfile-wrapper .
```

```shell
podman run --rm --platform linux/amd64 blackbox
# Ooooh, what's wrong? :(
```

Great! Expected failure. Running the binary works. Let's create a file `the_magic_filez.txt` and pass it as argument to the binary.

```shell
# Build the fixed container
podman build -t blackbox .
```

```shell
podman run --rm --platform linux/amd64 blackbox
# Congrats! :)
```

## Notes

When I went through all steps again to write the README.md, I realized the file doesn't need to be passed as arg, but only needs to be in the same folder as the `blackbox` binary. You could comment out `CMD ["the_magic_filez.txt"]`, build again and it would still work.

The slightly different syntax in `Dockerfile` and `Dockerfile-wrapper` is to avoid to unintentionally copy the `the_magic_filez.txt` into the "broken" container.
