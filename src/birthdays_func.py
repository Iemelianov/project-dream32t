def add_birthday(args, book):
        # Ensure name and birthday are provided
        if len(args) < 2:
            raise ValueError("Give me name and birthday. Even my goldfish has better planning.")
        name, birthday_str = args
        record = book.find(name)
        if record is None:
            raise KeyError("Contact not found. But hey, fake friends don’t count.")
        record.add_birthday(birthday_str)
        return f"Added birthday for [bold cyan]{name}[/bold cyan]. Try to remember it this year.😏"


def birthdays(args, book):
        # Get upcoming birthdays
        upcoming = sorted(book.get_upcoming_birthdays(), key=lambda x: x["congratulation_date"])
        if not upcoming:
            return "No birthdays soon. Guess nobody likes you this week."
        table = Table(
            title="[bold magenta]🎂 Upcoming Birthdays[/bold magenta]",
            title_style="bold magenta",
            show_header=True,
            header_style="bold yellow",
            border_style="magenta"
            )
        table.add_column("Name", style="green")
        table.add_column("Congratulation Date", style="cyan")

        for item in upcoming:
            table.add_row(item["name"], item["congratulation_date"])
        return table


def get_upcoming_birthdays(self, days=7):
    from datetime import datetime, timedelta
    today = datetime.today().date()
    upcoming_birthdays = []

    for record in self.data.values():
        if record.birthday is None:
            continue
        birthday = record.birthday.value

        # Adjust to this year (handle Feb 29)
        try:
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            birthday_this_year = birthday.replace(year=today.year, day=28)

        # If already passed, use next year
        if birthday_this_year < today:
            try:
                birthday_this_year = birthday.replace(year=today.year + 1)
            except ValueError:
                birthday_this_year = birthday.replace(year=today.year + 1, day=28)

        days_until = (birthday_this_year - today).days

        # ONLY process if within range
        if 0 <= days_until <= days:
            congratulation_date = birthday_this_year

            # Adjust for weekends
            if congratulation_date.weekday() == 5:  # Saturday
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Sunday
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": record.name.value,
                "congratulation_date": congratulation_date.strftime("%d.%m.%Y")
            })

    return upcoming_birthdays