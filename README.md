# Monte Carlo Option Pricing

This project provides a Monte Carlo option pricing engine for European call and put options. The engine uses the spot price and strike price obtained from Oanda API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites

You will need to have the following libraries installed:

    numpy
    requests
    json
    attrdict

You can install them by running the following command:

pip install numpy requests json attrdict

You will also need an API key from Oanda, which can be obtained by creating an account on the Oanda website.
### Installing

    Clone the repository

git clone https://github.com/<username>/monte-carlo-option-pricing.git

    Enter the project directory

cd monte-carlo-option-pricing

    Create a new file called config.py in the project directory and add the following line to it, replacing YOUR_API_KEY with your actual Oanda API key

API_KEY = "YOUR_API_KEY"

    Run the main script

python main.py

The program will output the call price and put price for the option.
## Built With

    numpy - Used for array operations
    requests - Used for making HTTP requests
    json - Used for parsing JSON data
    attrdict - Used for converting dictionaries to objects, allowing dot notation to access keys.

## Authors

    Ghaith Khalil - *Initial work*

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
Acknowledgments

    Hat tip to anyone whose code was used
    Inspiration
    etc

## Note

The return values are only for educational use. This is not a real world trading platform.
