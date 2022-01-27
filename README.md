# market-scraper
Reports item count of listed items in specified in your watchlist.

# BDO Market API guide

https://developers.veliainn.com/

# How to use

1. Update `watchlist.json` with the list of items you want to watch.
    - Follow the in-game enhancement level range for your `min_level` and `max_level` values.
        - Example for +0 ~ +7: `min_level: 0`, `max_level: 7`
        - Example for TET: `min_level: 19`, `max_level: 19`
        - Example for PEN: `min_level: 20`, `max_level: 20`

2. Install python stuff
    - Navigate to `./src`
    - `$ pipenv install`

3. Run the code while still in the `./src` directory
    - `$ pipenv run python main.py`

4. The software will print in the terminal how many items are listed for each item in your watchlist if count is > 0

# Future features

- Discord notification
- SMS notification maybe