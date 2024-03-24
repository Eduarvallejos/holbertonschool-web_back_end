// Import the Currency class from 3-currency.js
import Currency from './3-currency';

export default class Pricing {
  constructor(amount = 0, currency = Currency) {
    // Constructor to initialize the amount and currency of the pricing
    this._amount = amount;
    this._currency = currency; // The currency parameter is set to the Currency class by default
  }

  // Getter and setter for the 'amount' attribute.
  get amount() {
    return this._amount;
  }

  set amount(amount) {
    this._amount = amount;
  }

  // Getter and setter for the 'currency' attribute.
  get currency() {
    return this._currency;
  }

  set currency(currency) {
    this._currency = currency;
  }

  // Method to display the full price (amount and currency)
  displayFullPrice() {
    return `${this.amount} ${this.currency.displayFullCurrency()}`;
  }

  // Static method to convert a price based on a conversion rate
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
