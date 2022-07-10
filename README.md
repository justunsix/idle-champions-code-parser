# Idle Champions Code Parse

## About

The program takes manual copied chat history from the Idle Champions Discord server, Combinations channel, and parses it into a list of combinations that can be inputted into the [Idle Combos](https://github.com/dhusemann/idlecombos/) program.

## How to use

- Copy the recent chat history from the Idle Champions Discord server, Combinations channel into a file `idle-codes.txt`.
- Run the program below to parse the Idle Champion codes from it and get an output file.
- The output file `ic-codes-parsed.txt` will be generated and contain the codes in a format that can be submitted to the [Idle Combos](https://github.com/dhusemann/idlecombos/) AHK interface.
- Format of the output file will have a code on each line, for example:
 
```txt
XXXX-XXXX-XXX1
XXXX-XXXX-XXXX-XXX2
XXXX-XXXX-XXX3
XXXX-XXXX-XXX4
```

## Run

Run in root of repository

```sh
cd src
python parse-ic-codes-from-file.py
```

Find the output in the file `ic-codes-parsed.txt`.
