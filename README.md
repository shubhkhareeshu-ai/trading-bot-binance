# trading-bot-binance

# Trading Bot (Binance Futures Testnet)

## Overview

This project is a Python-based CLI trading bot that interacts with the Binance Futures Testnet to place BUY and SELL orders.
It supports both MARKET and LIMIT orders with proper validation, logging, and error handling.

The code is structured in a modular way for better readability and maintainability.

---

## Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL
* CLI-based input system
* Input validation
* Error handling (API + user input)
* Logging of requests, responses, and errors
* Structured and modular code

---

## Testnet Usage

This project uses Binance Futures Testnet to simulate trading without real funds.

---

## Project Structure

trading_bot/

├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py

├── cli.py
├── requirements.txt
├── README.md

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/shubhkhareeshu-ai/trading-bot-binance
cd trading-bot-binance

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add API Keys

Create a .env file in the root directory:
API_KEY=your_api_key
API_SECRET=your_secret_key

---

## How to Run

### Market Order

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

### Limit Order

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

---

## Output

The bot displays:

* Order summary
* Order ID
* Status
* Executed quantity
* Success/Failure message

---

## Logging

All API requests, responses, and errors are stored in:
bot.log

---

## Error Handling

* Invalid inputs are validated
* API errors are handled
* Network failures are logged

---

## Assumptions

* User has a Binance Futures Testnet account
* API keys are configured correctly
* Internet connection is available

---

## Future Improvements

* Add Stop-Limit orders
* Improve CLI interaction
* Add risk management features

---

