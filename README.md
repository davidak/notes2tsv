# notes2tsv

Convert notes of measurements to TSV format

I made a lot of measurements while testing an appliance at work. Now i want to convert my notes into a spreadsheet. I have created this small script to convert the notes to TSV format. CSV would be more popular, but i have commas in the comments.

### Requirements

Tested with Python 3.7, but it should work with any later version too.

## Usage

1. Download this repository as zip and extract it or clone with git
2. Open a terminal and navigate to the repository, e.g. `cd Downloads/notes2tsv`
3. Run the script on your data, e.g. `./notes2tsv.py examples/data.txt >data.tsv`

See files in `examples/` for example notes textfile and converted TSV file.

The following notes would look like that when converted:

```
30 Containers, ext4, dev net
Scan 8 hosts x 1 NVTs
Scan Duration 2:03h
Results: 962
Errors: 0
Target load: 0

30 Containers, ext4, dev net
Scan 8 hosts x 10 NVTs
Scan Duration 1:15h
Results: 1115
Errors: 168
Target load: 0
...
```

```
Targets	Hosts	NVTs	Scan Duration	Results	Errors	Target load	Target iowait	GSM load	Comment
30	8	1	2:03	962	0	0			30 Containers, ext4, dev net
30	8	10	1:15	1115	168	0			30 Containers, ext4, dev net
...
```

## License

Copyright (C) 2020 [davidak](https://davidak.de/)

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
