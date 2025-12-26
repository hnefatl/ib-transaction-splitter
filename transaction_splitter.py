import dataclasses
import argparse
import csv


@dataclasses.dataclass
class Args:
    in_file: str
    out_file: str
    symbol: str

    @staticmethod
    def parse() -> "Args":
        p = argparse.ArgumentParser()
        p.add_argument("--in_file", default="transactions.csv")
        p.add_argument("--out_file", default="out.csv")
        p.add_argument("--symbol", required=True)
        args = p.parse_args()
        return Args(**vars(args))


KEEP_COLUMNS = {
    "Date": "Date",
    "Transaction Type": "Transaction Type",
    "Quantity": "Quantity",
    "Price": "Price ($)",
    "Net Amount": "Total Cost ($)",
}


def main():
    args = Args.parse()

    with open(args.in_file, "rt") as t, open(args.out_file, "wt") as o:
        header = None
        for line in t:
            if line.startswith("Transaction History"):
                header = line
                break
        if header is None:
            print("Failed to find data.")
            return
        rows = t.readlines()
        rows.reverse()  # Downloaded log is in reverse order.

        reader = csv.DictReader(rows, [h.strip() for h in header.split(",")])
        writer = csv.DictWriter(o, KEEP_COLUMNS.values())

        writer.writeheader()
        for row in reader:
            if row.get("Symbol") != args.symbol:
                continue

            values = dict[str, str]()
            for i, o in KEEP_COLUMNS.items():
                value = row[i]
                if value == "-":
                    value = ""
                values[o] = value

            writer.writerow(values)


if __name__ == "__main__":
    main()
