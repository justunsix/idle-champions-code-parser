# Idle Champions Codes Parser

## About The Project

The program takes manual copied chat history from the Idle Champions Discord server's combinations channel, and parses it into a list of combinations that can be inputted into the [Idle Combos](https://github.com/dhusemann/idlecombos/) program.

### Built With

- [Python 3](https://www.python.org/)

## Getting Started

- Copy the recent chat history from the [Idle Champions Discord server](https://discord.com/invite/idlechampions), Combinations channel into a file `idle-codes.txt`.
- Run the program below to parse the Idle Champion codes from it and get an output file.
- The output file `ic-codes-parsed.txt` will be generated and contain the codes in a format that can be submitted to the [Idle Combos](https://github.com/dhusemann/idlecombos/) AHK interface.
- Format of the output file will have a code on each line, for example:
 
```txt
XXXX-XXXX-XXX1
XXXX-XXXX-XXXX-XXX2
XXXX-XXXX-XXX3
XXXX-XXXX-XXX4
```

## Usage

Run in root of repository

```sh
cd src
python parse-ic-codes-from-file.py
```

Find the output in the file `ic-codes-parsed.txt`.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Justin Tung - [GitHub](https://github.com/justunsix/)

## Acknowledgments

- [Best ReadMe Template](https://github.com/othneildrew/Best-README-Template)
- [VS Code](https://code.visualstudio.com/) and [Python Extensions](https://code.visualstudio.com/docs/languages/python) and [GitHub Copilot](https://github.com/features/copilot)
