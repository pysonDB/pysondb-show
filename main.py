import argparse
import json
from argparse import _SubParsersAction

from beautifultable import BeautifulTable


class Plugin:

    def __init__(self) -> None:
        pass

    def plugin_parser(self, subparser: _SubParsersAction):
        display_parser = subparser.add_parser("show", help="Display a database file")
        display_parser.add_argument(
            "file_name", help="Name of the database file to display"
        )

    def action(self, args: argparse.Namespace):
        """
        Print a database file
        :param str file_name: The absolute path to the DB file
        """
        table = BeautifulTable()
        with open(args.file_name) as jsondoc:
            data = json.load(jsondoc)
            real_data = data["data"]
            try:
                header = list(data["data"][0].keys())
            except IndexError:
                print("Database is empty.")
                return 1
            for all_data in real_data:
                table.rows.append(list(all_data.values()))
            table.columns.header = header
            print(table)
        return 0
