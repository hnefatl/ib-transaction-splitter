# IB Transaction Splitter

Download transaction history from Interactive Brokers reports:

```bash
$ python3 transaction_splitter.py --in_file=....csv --list_symbols=True
...
WDESG
GBP.USD

# Get just the WDESG stock events.
$ python3 transaction_splitter.py --in_file=....csv --symbol=WDESG
$ cat out.csv
Date,Transaction Type,Quantity,Price ($),Total Cost ($)
2021-04-06,Buy,3.0,154.48,-342.462824
2021-05-10,Buy,1.0,159.9,-120.34356799999999
...
```

Ready for import into Google sheets (Import -> Replace cells at bottom of sheet).
