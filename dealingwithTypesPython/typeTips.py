

def calc_cost(tax: int) -> int:
    """Calcs total cost of item"""
    cost: int = int(input("how much did the item cost: "))
    cost += tax

    print(type(cost))

    return cost


if __name__ == "__main__":
    print(calc_cost(5))