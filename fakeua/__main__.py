#!/usr/bin/env python3

from fakeua.fakeua import update_useragent_db
from fakeua.fakeua import get_useragent_list
from fakeua.fakeua import get_random_ua

from fakeua.fakeua import DEFAULT_BROWSER
from fakeua.fakeua import DEFAULT_VERSION_FILTER
from fakeua.fakeua import DEFAULT_JSON_FP

from pathlib import Path

import typer

app = typer.Typer()


@app.command()
def main(
    update: bool = typer.Option(
        False,
        "--update",
        "-u",
        help="Update useragent DB."
    ),
    path: str = typer.Option(
        DEFAULT_JSON_FP.as_posix(),
        "--path",
        "-p",
        help=f"Json filepath where data_browsers dict is saved, by default is {DEFAULT_JSON_FP}."
    ),
    browser: str = typer.Option(
        DEFAULT_BROWSER,
        "--browser",
        "-b",
        help="Specify a web browser"
    ),
    filter: str = typer.Option(
        DEFAULT_VERSION_FILTER,
        "--filter",
        "-f",
        help="Specify a browser version filter"
    ),
    list: bool = typer.Option(
        False,
        "--list",
        "-r",
        help="Get UA list."
    ),
    random: bool = typer.Option(
        False,
        "--random",
        "-c",
        help="Choice a random element from UA list."
    )
):
    if update:
        update_useragent_db(path=Path(path))
        print("Browsers database updated.")
        raise typer.Exit(0)

    if list:
        filtered_ua_list = get_useragent_list(
            browser=browser,
            version_filter=filter,
            path=Path(path)
        )
        if random:
            random_ua = get_random_ua(
                browser=browser,
                version_filter=filter,
                path=Path(path)
            )
            print(random_ua)
        else:
            for ua in filtered_ua_list:
                print(ua)


if __name__ == "__main__":
    app()
