# seller_ranking

Prototype for a seller_ranking logic

## How to use

### Requirements
- Docker
- Python 3.8.5
- MySQL 8

### Start the enviroment
To start the enviroment first you need to star the pyton virtual env with:
``` python3 -m venv venv ```

To activate the virtualenv use the command:
``` source venv/bin/activate ```

To start the database containing the 5 registered sellers you must use the command:
``` docker-compose up ```

With this 3 steps you are ready to star working.

### Running the script
To run the script you just need to run:
``` python proto_ranking.py``` 

This will star the script. Follow the instructions on the screen to use it.
There is 5 seller pre registered: seller_1, seller_2, seller_3, seller_4, seller 5.
Any other name used will result on an exception.

The item_value is a float, so you can use numbers with decimal cases.

### Warning
This is a prototype, as such there is no tests, too much of error handling.
The ideia of this prototype is to validate the system general idea and ordering logic!!!

