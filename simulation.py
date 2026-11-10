
# AI Assistance: ChatGPT (OpenAI) was used on November 10, 2026 to help plan the simulation and write the Python functions and loops.
# I reviewed the calculations and tested the program locally.
# I checked the profit calculation using a manually worked example and confirmed that a fixed random seed produces consistent results.

import random


def calculate_profit(tickets_sold, arrivals, seats, ticket_price, bumping_cost):
    bumped = max(0, arrivals - seats)
    revenue = tickets_sold * ticket_price
    compensation = bumped * bumping_cost
    profit = revenue - compensation
    return profit


def simulate_arrivals(tickets_sold, no_show_probability, rng):
    arrivals = 0

    for passenger in range(tickets_sold):
        if rng.random() >= no_show_probability:
            arrivals += 1

    return arrivals


def main():
    # Set up the simulation
    rng = random.Random(42)

    seats = 100
    ticket_price = 200
    no_show_probability = 0.10
    bumping_cost = 400
    num_flights = 1000

    ticket_quantities = []
    average_profits = []

    # Test selling 100 through 120 tickets
    for tickets_sold in range(100, 121):
        total_profit = 0

        # Simulate 1,000 flights
        for flight in range(num_flights):
            arrivals = simulate_arrivals(tickets_sold, no_show_probability, rng)

            profit = calculate_profit(tickets_sold, arrivals, seats, ticket_price, bumping_cost)

            total_profit += profit

        # Calculate and store the average profit
        average_profit = total_profit / num_flights

        ticket_quantities.append(tickets_sold)
        average_profits.append(average_profit)

        print(f"{tickets_sold} tickets: ${average_profit:,.2f}")

    # Find the ticket quantity with the highest average profit
    best_tickets = ticket_quantities[0]
    best_profit = average_profits[0]

    for i in range(1, len(average_profits)):
        if average_profits[i] > best_profit:
            best_profit = average_profits[i]
            best_tickets = ticket_quantities[i]

    print(f"\nBest ticket quantity: {best_tickets}")
    print(f"Highest average profit: ${best_profit:,.2f}")


if __name__ == "__main__":
    main()
