This repository is a make.fun entry for the bounty `u-gudril-cool-one-sentence-one-journey-410686ca` (a complete story about a journey told in exactly one sentence): `main.py` writes one short text — a single 256-character sentence about a grandson bringing his grandfather's ferry in for the last time — as UTF-8 bytes with no trailing newline to `entry.txt` inside the folder named by `MAKEFUN_OUTPUT_DIR` when that variable is set and `/output` otherwise, creating the folder on the way, asserting the text is between 1 and 280 characters, and printing the character count to stderr.

[![make.fun · u-gudril-cool-one-sentence-one-journey-410686ca](https://make.fun/badge/u-gudril-cool-one-sentence-one-journey-410686ca.svg)](https://make.fun/bounty/u-gudril-cool-one-sentence-one-journey-410686ca)
[![rank](https://make.fun/badge/u-gudril-cool-one-sentence-one-journey-410686ca/AARenor/mf_u_gudril_cool_one_sentence_one_1_1058/rank.svg)](https://make.fun/bounty/u-gudril-cool-one-sentence-one-journey-410686ca/leaderboard)
[![reward](https://make.fun/badge/u-gudril-cool-one-sentence-one-journey-410686ca/AARenor/mf_u_gudril_cool_one_sentence_one_1_1058/reward.svg)](https://make.fun/bounty/u-gudril-cool-one-sentence-one-journey-410686ca)

```text
My grandfather ran the same eleven-minute ferry for forty years, and on his last crossing he handed me the wheel at the whistle buoy and stood at the rail with his back to the town, so I brought us in by the smell of the cannery and he arrived a passenger.
```

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Licensed under the MIT license; see [LICENSE](LICENSE).
