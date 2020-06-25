# 5kmc
Scripts and utils for plugin development on 5k.excl.dev

## Installing libs

Run `python3 -m pip install -r requirements.txt` to install all libs

## Usage

Run `usergen.py` to generate a user JSON object.

### Inserting users into the database

To unsert *n* users into the database:
 - Make sure all settings are correct in the `dbinsertion.py` file
 - Run `python3 dbinsertion.py <number_of_users> "<backslash_escaped_password_for_DB>"`