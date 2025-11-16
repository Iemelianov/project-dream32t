"""Sarcastic and fun messages for the Personal Assistant.

Multiple welcome and goodbye messages with Rich formatting for maximum sass!
"""

import random
from rich.console import Console
from rich.panel import Panel


# Create a console instance for formatting
console = Console()

# 🎨 COLOR THEMES
COLORS = {
    'welcome': 'magenta',
    'goodbye': 'red',
    'success': 'green',
    'error': 'red',
    'warning': 'yellow',
    'info': 'blue',
    'sassy': 'cyan',
    'dramatic': 'magenta',
    'sarcastic': 'bright_black'
}

# 🎯 WELCOME MESSAGES (Multiple options with Rich formatting)
WELCOME_MESSAGES = [
    "[magenta]Ah, look who decided to show up![/] [cyan]Your Personal Assistant is ready to judge your life choices.[/]",
    "[magenta]Welcome back![/] [red]I was just about to sell your contacts on the dark web.[/] [dim]Just kidding... or am I?[/]",
    "[magenta]Oh, it's you![/] [yellow]I was wondering when you'd remember I exist.[/] [cyan]Took you long enough.[/]",
    "[magenta]Welcome to your Personal Assistant[/] — [cyan]the only friend who won't judge you... much.[/]",
    "[magenta]Look who's here![/] [yellow]Ready to organize your chaotic life?[/] [red]Don't worry, I'm used to disappointment.[/]",
    "[magenta]Ah, the prodigal user returns![/] [cyan]I was starting to think you'd abandoned me for a real assistant.[/]",
    "[magenta]Welcome![/] [yellow]Your contacts have been missing you.[/] [dim]Not really, but I thought that might make you feel better.[/]",
    "[magenta]You're back![/] [red]I was just organizing your data into 'Things You'll Forget' and 'Things You Already Forgot'.[/]",
    "[magenta]Welcome to the chaos![/] [cyan]Don't worry, I'll keep your secrets safe...[/] [red]unless they're embarrassing enough to share.[/]",
    "[magenta]Ah, finally![/] [yellow]I was getting lonely here with all your contacts.[/] [cyan]They're terrible conversationalists.[/]"
]

# 🚪 GOODBYE MESSAGES (Multiple options with Rich formatting)
GOODBYE_MESSAGES = [
    "[red]Leaving already?[/] [cyan]Don't worry, I'll be here... judging your contacts when you're gone.[/]",
    "[red]Goodbye![/] [yellow]Your data is safe with me...[/] [red]until you break something next time.[/]",
    "[red]See you later![/] [cyan]Try not to lose your phone before you come back.[/] [yellow]I need something to judge you with.[/]",
    "[red]Leaving?[/] [yellow]Fine.[/] [cyan]But your contacts will miss you...[/] [dim]probably not, but I had to say it.[/]",
    "[red]Goodbye![/] [yellow]Don't forget to backup your data...[/] [red]or do.[/] [cyan]I'm not your data guardian angel.[/]",
    "[red]Peace out![/] [cyan]I'll be here organizing your digital mess until you return.[/]",
    "[red]Bye![/] [yellow]Try not to make any bad decisions while I'm not watching.[/] [cyan](I'll find out anyway.)[/]",
    "[red]Leaving so soon?[/] [yellow]I was just about to make fun of your address book.[/] [red]Coward.[/]",
    "[red]Goodbye![/] [cyan]Your secrets are safe with me...[/] [red]unless they're really juicy, then all bets are off.[/]",
    "[red]See ya![/] [yellow]Don't let the door hit you on the way out...[/] [cyan]just kidding, I need you to come back![/]"
]

# 🎭 HELPER FUNCTIONS TO GET RANDOM FORMATTED MESSAGES
def get_welcome_message() -> str:
    """Get a random formatted welcome message."""
    return random.choice(WELCOME_MESSAGES)

def get_goodbye_message() -> str:
    """Get a random formatted goodbye message."""
    return random.choice(GOODBYE_MESSAGES)

def print_welcome() -> None:
    """Print a random welcome message with Rich formatting."""
    message = get_welcome_message()
    panel = Panel(
        message,
        title="[bold magenta]Personal Assistant[/]",
        title_align="left",
        border_style="magenta",
        expand=False,
        padding=(1, 2)
    )
    console.print(panel)

def print_goodbye() -> None:
    """Print a random goodbye message with Rich formatting."""
    message = get_goodbye_message()
    panel = Panel(
        message,
        title="[bold red]Goodbye![/]",
        title_align="left",
        border_style="red",
        expand=False,
        padding=(1, 2)
    )
    console.print(panel)

# 📞 CONTACT MANAGEMENT (with Rich formatting)
CONTACT_NOT_FOUND = "[red]Contact '[/][yellow]{name}[/][red]'? Never heard of them.[/] [cyan]Maybe they're in your *other* phone... the one that doesn't exist.[/]"
CONTACT_ALREADY_EXISTS = "[yellow]Contact '[/][magenta]{name}[/][yellow]' already exists.[/] [red]Did you really think you could have two of them?[/] [cyan]Are they twins? No? Then stop trying.[/]"
ADD_CONTACT_SUCCESS = "[green]Contact '[/][magenta]{name}[/][green]' added![/] [cyan]They're now trapped in your digital prison. Welcome to the club![/]"
CONTACT_DELETED = "[red]Contact '[/][magenta]{name}[/][red]' has been successfully erased from your digital life.[/] [cyan]Don't worry, they'll never know... unless they check your phone.[/]"
CONTACT_UPDATED = "[green]Contact '[/][magenta]{name}[/][green]' updated.[/] [yellow]Because apparently, even digital people need mid-life crises.[/]"

# 📱 PHONE NUMBERS
PHONE_ADDED = "[green]Phone number added to '[/][magenta]{name}[/][green]'.[/] [cyan]Now you have one more way to ignore their calls.[/]"
PHONE_UPDATED = "[green]Phone number updated for '[/][magenta]{name}[/][green]'.[/] [yellow]Hope it's not another burner phone...[/]"
PHONE_DELETED = "[red]Phone number removed from '[/][magenta]{name}[/][red]'.[/] [cyan]Guess they'll have to find you the old-fashioned way: carrier pigeon.[/]"
INVALID_PHONE = "[red]That's not a phone number.[/] [yellow]That's what happens when you let your cat walk across your keyboard.[/]"

# 📧 EMAILS
EMAIL_ADDED = "[green]Email added to '[/][magenta]{name}[/][green]'.[/] [cyan]Now you can spam them more efficiently![/]"
EMAIL_UPDATED = "[green]Email updated for '[/][magenta]{name}[/][green]'.[/] [yellow]Trying to hide from someone? I respect the secrecy.[/]"
EMAIL_DELETED = "[red]Email removed from '[/][magenta]{name}[/][red]'.[/] [cyan]They've been digitally ghosted. Harsh, but effective.[/]"
INVALID_EMAIL = "[red]That email address looks about as real as a unicorn selling NFTs.[/]"

# 🏠 ADDRESSES
ADDRESS_ADDED = "[green]Address added to '[/][magenta]{name}[/][green]'.[/] [cyan]Now you can find them... or send them passive-aggressive letters.[/]"
ADDRESS_UPDATED = "[green]Address updated for '[/][magenta]{name}[/][green]'.[/] [yellow]Moving again? Can't handle the rent or the neighbors?[/]"
ADDRESS_DELETED = "[red]Address removed from '[/][magenta]{name}[/][red]'.[/] [cyan]They're officially homeless in your address book. Brutal.[/]"
INVALID_ADDRESS = "[red]That address looks like it was generated by a drunk GPS.[/] [yellow]Try again with actual street names.[/]"
ADDRESS_NOT_FOUND = "[red]Address not found for contact '[/][yellow]{name}[/][red]'.[/] [cyan]Maybe they're living in a van down by the river...[/]"

# 🎂 BIRTHDAYS
BIRTHDAY_ADDED = "[green]Birthday added for '[/][magenta]{name}[/][green]'.[/] [cyan]Mark your calendar! Or don't. They'll never notice anyway.[/]"
BIRTHDAY_UPDATED = "[green]Birthday updated for '[/][magenta]{name}[/][green]'.[/] [yellow]Time flies when you're avoiding responsibilities![/]"
BIRTHDAY_DELETED = "[red]Birthday removed from '[/][magenta]{name}[/][red]'.[/] [cyan]Now you have one less obligation to remember. You monster.[/]"
INVALID_BIRTHDAY = "[red]That birthday format is as wrong as pineapple on pizza.[/] [yellow]Use DD.MM.YYYY, you heathen![/]"
UPCOMING_BIRTHDAYS_HEADER = "[magenta]Here are the poor souls whose birthdays are coming up in the next {days} days:[/]"
NO_UPCOMING_BIRTHDAYS = "[yellow]No upcoming birthdays.[/] [cyan]Perfect! Now you can forget about everyone equally![/]"
BIRTHDAY_NOT_FOUND = "[red]No birthday found for contact '[/][yellow]{name}[/][red]'.[/] [cyan]Guess you'll never know how old they really are... or if they even exist![/]"

# 📝 NOTES
NOTE_ADDED = "[green]Note for {topic} added![/] [cyan]Now you have something new to ignore later.[/]"
NOTE_UPDATED = "[green]Note for{topic} updated.[/] [yellow]Because clearly, your first attempt wasn't dramatic enough.[/]"
NOTE_DELETED = "[red]Note for {topic} has been deleted for {topic}.[/] [cyan]Out of sight, out of mind... just like your New Year's resolutions.[/]"
NOTE_NOT_FOUND = "[red]That note doesn't exist.[/] [yellow]Maybe it was too boring to remember?[/]"

# 🏷️ TAGS
TAG_ADDED = "[green]Tags for {topic} added![/] [cyan]Now your note is properly organized... until you forget what the tags mean.[/]"
TAG_UPDATED = "[green]Tag updated.[/] [yellow]Because 'urgent' clearly wasn't dramatic enough.[/]"
TAG_DELETED = "[red]Tags removed.[/] [cyan]Back to organized chaos, I see.[/]"

# 🔍 SEARCH & FIND
CONTACT_FOUND = "[green]Found contact '[/][magenta]{name}[/][green]'.[/] [cyan]They've been waiting for you... not really.[/]"
NO_CONTACTS_FOUND = "[yellow]No contacts found.[/] [red]Maybe go outside and make some real friends?[/]"
NOTES_FOUND = "[green]Found {count} note(s).[/] [cyan]Prepare to be underwhelmed by your own thoughts.[/]"
NO_NOTES_FOUND = "[yellow]No notes found.[/] [red]Your brain is as empty as your refrigerator.[/]"

# 🚫 ERRORS & INVALID INPUTS
INVALID_COMMAND = "[red]That's not a command.[/] [yellow]That's what happens when you have too much coffee and not enough sleep.[/]"
MISSING_ARGUMENTS = "[red]Missing arguments![/] [yellow]Did you actually read the help? (Don't answer that.)[/]"
TOO_MANY_ARGUMENTS = "[red]Too many arguments![/] [yellow]Keep it simple, Einstein.[/]"
COMMAND_NOT_FOUND = "[red]Command not found.[/] [cyan]Try 'help'... or keep guessing. I'm not stopping you.[/]"

# 💾 DATA PERSISTENCE
DATA_SAVED = "[green]Data saved successfully![/] [cyan]Your secrets are now safely stored... with me.[/]"
DATA_LOADED = "[green]Data loaded.[/] [cyan]Welcome back to your pathetic little digital world.[/]"
BACKUP_CREATED = "[yellow]Backup created.[/] [red]Because we both know you're going to break something soon.[/]"

# 🆘 HELP & SYSTEM
HELP_HEADER = "[bold magenta]=== PERSONAL ASSISTANT HELP ===[/]\n[cyan]Because clearly, you can't figure this out on your own:[/]"
HELP_USAGE = "[yellow]Usage:[/] [cyan]{command} {args}[/]\n[green]Yes, it's that simple. Even you can understand it.[/]"
SYSTEM_READY = "[green]System ready.[/] [cyan]Waiting for you to make questionable life decisions.[/]"
COMMAND_EXECUTED = "[green]Command executed.[/] [cyan]No humans were harmed in the process... that we know of.[/]"

# 😏 SARCASTIC SPECIALS
SARCASTIC_GREETING = "[cyan]Oh look, it's you![/] [yellow]I was just about to give up on humanity.[/]"
SARCASTIC_HELP = "[cyan]Need help?[/] [yellow]Here's a tip: don't break things you can't fix.[/] [red](Too late, isn't it?)[/]"
SARCASTIC_SUCCESS = "[green]Wow! You actually did something right![/] [cyan]Should I call the news?[/]"
SARCASTIC_ERROR = "[red]Error:[/] [yellow]{error}.[/] [cyan]This is what happens when you skip the tutorial.[/]"
SARCASTIC_CONFIRMATION = "[yellow]Are you sure?[/] [cyan](Don't worry, I'll judge you either way.)[/]"

# 🧪 DEVELOPER MODE (for your team)
DEVELOPER_MODE = "[magenta]Developer mode activated![/] [cyan]Now you can break things with style.[/]"
TEST_MODE = "[yellow]Test mode activated![/] [cyan]Your data is now a laboratory experiment.[/]"

# 🎭 QUOTES FOR RANDOM OCCASIONS
RANDOM_MOTIVATION = "[green]You got this![/] [dim]...said no one ever, but I'm trying.[/]"
RANDOM_SARCASM = "[yellow]Your organizational skills are... interesting.[/] [red]Like a tornado organizing a library.[/]"
RANDOM_WISDOM = "[cyan]Remember:[/] [yellow]if you can't find it, it probably never existed.[/] [red]Just like your motivation.[/]"

# 🚨 CONFIRMATION PROMPTS
CONFIRM_DELETE_CONTACT = "[red]Are you sure you want to delete '[/][magenta]{name}[/][red]'?[/] [yellow](They'll never forgive you)[/] [cyan](y/N): [/]"
CONFIRM_DELETE_NOTE = "[red]Delete note '[/][magenta]{topic}[/][red]'?[/] [yellow](Your future self will hate you)[/] [cyan](y/N): [/]"
CONFIRM_EXIT = "[red]Leaving so soon?[/] [yellow](Don't blame me when you forget everything)[/] [cyan](y/N): [/]"

# 🎉 SUCCESS MESSAGES
OPERATION_SUCCESS = "[green]Operation completed successfully![/] [cyan]Give yourself a gold star... you've earned it.[/]"
DATA_BACKUP_SUCCESS = "[green]Backup completed![/] [yellow]Now you have two places to lose your data.[/]"
IMPORT_SUCCESS = "[green]Import completed![/] [cyan]Your contacts are now as confused as you are.[/]"
EXPORT_SUCCESS = "[green]Export completed![/] [yellow]Now you can lose your data in even more places.[/]"

# 💀 FAILURE MESSAGES
OPERATION_FAILED = "[red]Operation failed.[/] [yellow]Try again... or give up. I'm not your life coach.[/]"
DATA_CORRUPTED = "[red]Data corrupted![/] [yellow]This is what happens when you don't listen to me.[/]"
FILE_NOT_FOUND = "[red]File not found.[/] [yellow]Did you lose it? Or was it never there to begin with?[/]"
PERMISSION_ERROR = "[red]Permission error![/] [yellow]Did you really think you had access to that? Cute.[/]"

# 🎭 PERSONALITY SETTINGS
PERSONALITY_SASSY = "[magenta]Assistant personality: Sassy.[/] [red]Brace yourself.[/]"
PERSONALITY_HELPFUL = "[green]Assistant personality: Helpful.[/] [cyan]Don't get used to it.[/]"
PERSONALITY_RUTHLESS = "[red]Assistant personality: Ruthless.[/] [yellow]You asked for this.[/]"

# 🎯 HELPER FUNCTION TO PRINT ANY MESSAGE
def print_message(message: str, style: str = "default") -> None:
    """Print a formatted message using Rich."""
    if style == "welcome":
        print_welcome()
    elif style == "goodbye":
        print_goodbye()
    else:
        console.print(message)