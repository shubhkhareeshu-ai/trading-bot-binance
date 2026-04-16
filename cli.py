import argparse
from bot.orders import place_order
from bot.validators import validate_input
from bot.logging_config import setup_logging
import logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        print("\nPlacing Order...")
        logging.info(f"Request: {args}")

        response = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        if "error" in response:
            print("❌ Order Failed:", response["error"])
            logging.error(response["error"])
        else:
            print("✅ Order Success")
            print("Order ID:", response.get("orderId"))
            print("Status:", response.get("status"))
            print("Executed Qty:", response.get("executedQty"))

            logging.info(f"Response: {response}")

    except Exception as e:
        print("Error:", str(e))
        logging.error(str(e))


if __name__ == "__main__":
    main()