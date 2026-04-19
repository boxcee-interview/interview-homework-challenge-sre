# Extra Challenge 3: Test Helm Chart

I picked `helm unittest` over `chart-testing`, because I like the integration as `helm` plugin. Also, I have not used it before.

For the most, I followed the guid from their GitHub directly for setting it up. I left the chart in the original challenge folder and added test in there.

Test cases test everything what is being asked in the challenge #5.

To run:
```shell
helm unittest ../challenge-5/server-chart
```