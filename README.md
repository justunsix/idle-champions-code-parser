# Idle Champions Code Parse

## About

Open a text file call "idle-codes.txt" and parse the Idle Champion codes from it and write out the codes that match the format below to another text file called "ic-codes-parsed.txt"

Idle Champion codes are in the format of:
   XXXX-XXXX-XXXX or XXXX-XXXX-XXXX-XXXX
  where X is a character in the range of A-Z, 0-9, or !

The input text file is manual copied chat information from the Idle Champions Discord server, Combinations channel.

The output file will contain the codes in a format that can be submitted to the [Idle Combos](https://github.com/dhusemann/idlecombos/) AHK interface.

## Run

Run in root of repository

```sh
cd src
python parse-ic-codes-from-file.py
```

Find the output in the file `ic-codes-parsed.txt`.
