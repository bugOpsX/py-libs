# DSA/utils/currency_converter.py

"""
Currency Converter Library

This module uses the Exchangerate API to convert amounts between different currencies.
It provides both function-based and command-line usage.

Usage (as a library):
    from DSA.utils.currency_converter import convert_currency
    result = convert_currency(100, "USD", "EUR")
    print(result)

Usage (CLI):
    python3 DSA/utils/currency_converter.py 100 USD EUR
"""

import sys
import requests

API_URL = "https://open.er-api.com/v6/latest/"  # Free public endpoint


def convert_currency(amount, from_currency, to_currency):
    """
    Convert amount from one currency to another using live exchange rates.

    :param amount: float - Amount of money to convert
    :param from_currency: str - Currency code to convert from (e.g., 'USD')
    :param to_currency: str - Currency code to convert to (e.g., 'EUR')
    :return: float - Converted amount, or None if conversion failed
    """
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    try:
        response = requests.get(API_URL + from_currency)
        response.raise_for_status()
        data = response.json()

        # Check for errors
        if data.get("result") != "success":
            print("❌ Error fetching exchange rates:", data.get("error-type"))
            return None

        rates = data.get("rates", {})
        if to_currency not in rates:
            print(f"❌ Unsupported target currency: {to_currency}")
            return None

        converted = amount * rates[to_currency]
        return round(converted, 2)

    except requests.exceptions.RequestException as e:
        print("⚠️ Network error:", e)
        return None


def cli():
    """Command-line interface for currency conversion."""
    if len(sys.argv) != 4:
        print("Usage: python3 DSA/utils/currency_converter.py <amount> <from_currency> <to_currency>")
        print("Example: python3 DSA/utils/currency_converter.py 100 USD EUR")
        return

    try:
        amount = float(sys.argv[1])
        from_currency = sys.argv[2]
        to_currency = sys.argv[3]

        result = convert_currency(amount, from_currency, to_currency)
        if result is not None:
            print(f"💱 {amount} {from_currency.upper()} = {result} {to_currency.upper()}")

    except ValueError:
        print("❌ Amount must be a number.")


if __name__ == "__main__":
    cli()
