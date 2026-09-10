class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        title = self.name.center(30, "*")
        items = ""
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"[:7]
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + "\n" + items + total


def create_spend_chart(categories):
    spent_amounts = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent_amounts.append(spent)

    total_spent = sum(spent_amounts)
    percentages = [int((spent / total_spent) * 100 // 10) * 10 for spent in spent_amounts]

    chart = "Percentage spent by category\n"

    for value in range(100, -1, -10):
        chart += str(value).rjust(3) + "| "
        for percent in percentages:
            chart += "o  " if percent >= value else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_length) for category in categories]

    name_lines = []
    for row in zip(*names):
        name_lines.append("     " + "  ".join(row) + "  ")

    chart += "\n".join(name_lines)

    return chart

#exemplo:
if __name__ == "__main__":
    food = Category("Food")
    food.deposit(1000, "salary")
    food.withdraw(200, "groceries")

    clothing = Category("Clothing")
    clothing.deposit(1000, "salary")
    clothing.withdraw(50, "shirt")

    print(create_spend_chart([food, clothing]))