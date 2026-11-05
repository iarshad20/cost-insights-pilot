# cost-insights-pilot

A throwaway SAM app used to test AWS Cost Insights end to end. It is one Python Lambda
behind an HTTP API in ap-south-1. Nothing here is real; do not put real data in it.

## The test

1. Deploy it once (`sam build`, then `sam deploy`), so a real stack exists to read usage from.
2. Open a pull request that raises `MemorySize` in `template.yaml`.
3. Expect one `AWS cost` check, one comment and one email. A further push that does not
   change cost must send no second email.
