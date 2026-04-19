# Challenge 5: Helm Chart

Using NOTES.md instead of README.md to keep README.md for instructions intact.

1. I copied the contents from `Chart.yaml`, then deleted the `server-chart` folder.
2. Then I re-created the chart folder with `helm create server-chart`. This scaffolds an empty chart which I can use.
3. Deleted all of the things not required for the challenge.
4. Changed the port from `80` to `8080` then.
5. Since the container would respond on the `/` without the correct header, I adjusted `liveness` and `readiness` probes as well.
6. Fixed some issues after running `helm lint`.
7. Rendered the chart once with  `helm template`.
8. Created a test cluster with `kind`.
9. Installed the chart once.
10. Chart install succeeded. Received an expected `ErrImagePull`.
11. Done