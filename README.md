# 📒 Personal Assistant - Console-Based Contact & Note Manager

Your intelligent command-line companion for managing personal contacts, appointments, and notes — built with Python, designed for reliability, and engineered for real-world use.

## 🎯 What is the Personal Assistant?

The Personal Assistant is a fully functional, console-based application that helps you organize your personal and professional life without leaving the terminal. It combines modern Python best practices with a clean, intuitive interface and comprehensive data management capabilities.

## 🚀 Installation & Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the repository:**
```bash
git clone <repository-url>
cd project-dream32t
```

2. **Install the package:**
```bash
pip install .
```

3. **Run the application:**
```bash
personal-assistant
```

### Alternative: Run Directly (No Installation)

If you prefer not to install the package or encounter PATH issues:

```bash
# Install dependencies only
pip install -r requirements.txt

# Run directly
python main.py
```

### Troubleshooting

**If `personal-assistant` command is not found:**

This happens when Python's Scripts folder is not in your system PATH.

**Solution 1: Add Python Scripts to PATH (Windows)**

1. Press `Win + X` and select "System"
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Under "User variables", select "Path" and click "Edit"
5. Click "New" and add your Python Scripts folder:
   - For standard Python: `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python3XX\Scripts`
   - For Windows Store Python: `C:\Users\<YourUsername>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.XX_xxxxx\LocalCache\local-packages\Python3XX\Scripts`
6. Click OK on all dialogs
7. **Restart your terminal or VS Code**

**Solution 2: Use Python directly**
```bash
python main.py
```

**Solution 3: Use full path to executable**
```bash
python -m pip show personal-assistant  # Find installation location
# Then run the .exe from the Scripts folder shown
```

### First Time Setup

After installation, start the application and type `help` to see all available commands:

```bash
personal-assistant
> help
```

## 🚀 Key Features

### ✅ Smart Contact Management

**Complete contact profiles** with:
- Name (unique, case-insensitive)
- Multiple phone numbers (10 digit format: `0501234567`)
- Email addresses (RFC-compliant validation)
- Physical address
- Birthday (DD.MM.YYYY format with leap year validation)

**Automatic validation:**
- Email addresses verified with RFC standards
- Birthday dates validated including leap years
- Duplicate prevention for phones and contacts

**Flexible editing:**
- Add, change, or delete any field independently
- Multiple phones per contact
- Multiple emails per contact
- Multiple addresses per contact
- Replace existing emails, addresses and phones

**Intelligent search by:**
- Name (case-insensitive)
- Phone number (exact match after normalization)
- Email address (case-insensitive)
- Birthday date (exact match)

**Birthday intelligence:**
- View upcoming birthdays within N days (default: 7 days)
- Automatic calculation across year boundaries
- Weekend birthdays shown with Monday congratulation dates

### 📝 Powerful Note System with Tags

**Full note lifecycle:**
- Create notes with single line text
- Edit note content
- Delete notes

**Tag-based organization:**
- Tags normalized to lowercase for consistency
- Case-insensitive tag search and comparison
- Remove individual tags while preserving others

**Search capabilities:**
- Search by note topic or text content (case-insensitive substring matching)
- Filter by multiple tags (case-insensitive)
- View all notes at once
- Sort all notes by their tags in alphabetical order

### 💾 Reliable Data Persistence

**Automatic save/load:**
- No manual "save" command needed
- Data stored as JSON in current directory
- Separate files: `contacts.json` and `notes.json`
- UTF-8 encoding with version tracking

### 🎨 Enhanced User Experience

**Color-coded output:** Different colors for different data types (using `rich` library)  
**Table formatting:** Contacts and notes displayed in clean, aligned tables  
**Comprehensive help:** Built-in command reference with detailed examples  
**Error prevention:** Clear, actionable error messages with suggestions  
**Command consistency:** Uniform kebab-case syntax across all operations  
**English interface:** All messages and prompts in English

## 🏗️ Architecture Highlights

- **SOLID Principles:** Single responsibility, open/closed design
- **Command Pattern:** Each command is a separate, testable class
- **Strategy Pattern:** Validation strategies for different field types
- **Factory Pattern:** Contact and note creation with proper validation
- **Observer Pattern:** Automatic data persistence on model changes

## 📊 Complete Command Reference

### Contact Management

```bash
# Create contact (name and phone are mandatory parameters)
add-contact "Dr. Maria Chen" 1234567890

# Show all contacts
all-contacts

# Delete contact
del-contact "Dr. Maria Chen"

# Add phone, supports multiple phones. Phone must be in 10 digit format
add-phone "Dr. Maria Chen" 0501234567

# Change specific phone number
change-phone "Dr. Maria Chen" 0501234567 0679876543

# Delete phone from contact
del-phone "Dr. Maria Chen" 1234567890

# Add email
add-email "Dr. Maria Chen" maria.chen@hospital.ua

# Change email
change-email "Dr. Maria Chen" maria.chen@hospital.ua maria.chen@hospital.com

# Delete email
del-email "Dr. Maria Chen" maria.chen@hospital.ua

# Add/update birthday
set-birthday "Dr. Maria Chen" 12.03.1978

# Upcoming birthdays (default: 7 days)
list-birthdays 14

# Delete birthday
del-birthday "Dr. Maria Chen"

# Add/update address (multi-word supported)
add-address "Dr. Maria Chen" "Hospital St, 15, Kyiv, 01001"

# Change address
change-address "Dr. Maria Chen" "Hospital St, 15, Kyiv, 01001" "Clinic Ave, 22, Lviv, 79000"

# Delete address
del-address "Dr. Maria Chen" "Clinic Ave, 22, Lviv, 79000"
```

### Contact Search

```bash
# Search by name
find-contact "Dr. Maria Chen"
```

### Note Management

```bash
# Create note (topic is mandatory field)
add-note DrChen "Follow up with Dr. Chen about test results" tag1,tag2

# Display all notes.
list-notes

# Edit note content(command must have topic field)
change-note DrChen "Updated: Follow up completed"

# Delete note (command must have topic field)
del-note DrChen


### Note Search & Tags

```bash
# Search by text content (case-insensitive substring)
note-by-text "follow up"

# Search by tags (case-insensitive, matches any tag)
note-by-tag tag1

# Add tags to existing note (command must have topic field)
add-tags DrChen important,followup

# Remove specific tags from note
del-tags DrChen important

# List all notes or tags (alphabetically sorted)
 sort-notes-tags
```

### System Commands

```bash
# Get help on any command
help
help add-contact
usage: add-contact <name> <phone>
  - name   Name of a contact.
  - phone  Phone number of a contact.

# Exit application
exit
```

## 💡 Sample Workflow

```bash
# Start the assistant
> personal-assistant

# Or if not in PATH
> python main.py

# Get help
> help
The command list:
 Command          Description
 add-contact      Adds a contact to the address book.
 del-contact      Deletes a contact from a contact book.
 find-contact     Find contact in the address book.
 all-contacts     Shows all contacts in the address book.
 add-phone        Adds a phone number to a contact.
 change-phone     This command changes the phone number of a contact.
 del-phone        Deletes a phone number from a a contact.
 add-email        Adds an email address to a contact.
 change-email     This command changes the email address of a contact.
 del-email        Deletes an email address from a contact.
 add-address      Adds an address to a contact.
 change-address   Changes an existing address of a contact to a new one.
 del-address      Deletes an address from a contact.
 set-birthday     Sets or updates the birthday of a contact.
 del-birthday     Deletes a birthday from a contact.
 list-birthdays   Shows contacts with birthdays in the next N days (default: 7).
 add-note         Adds a note to notes.
 change-note      This command changes the note of notes.
 del-note         Deletes a note from notes.
 list-notes       Show all notes.
 note-by-text     Finds a note in notes by text.
 note-by-tag      Finds a note in notes by tag.
 add-tags         Adds tags to note.
 change-tag       This command changes the tag of note.
 del-tags         Deletes tags from note.
 sort-notes-tags  Sort all notes by their tags in alphabetical order.
 exit             Exits the program.
 help             Displays a list of available commands or help for a specific command.

# Build your contact book
> add-contact "Dr. Maria Chen" 0123456789
Contact 'Dr. Maria Chen' added successfully.

> add-phone "Dr. Maria Chen" 0501234567
Phone number added to contact 'Dr. Maria Chen'.

> add-email "Dr. Maria Chen" maria.chen@hospital.ua
Email added to contact 'Dr. Maria Chen'.

> add-address "Dr. Maria Chen" "Hospital St, 15, Kyiv, 01001"
Address added to contact 'Dr. Maria Chen'.

> set-birthday "Dr. Maria Chen" 12.03.1978
> set-birthday "Dr. Maria Chen" 12.03.1978
Birthday added to contact 'Dr. Maria Chen'.

# Add some notes
> add-note "Follow up with Dr. Chen about test results" #medical #urgent
Note created with ID: 1

> add-note "Buy groceries for the week" #shopping
Note created with ID: 2

# Check upcoming events
> list-birthdays 14
Upcoming birthdays in next 14 days:
- Dr. Maria Chen: 12.03.2025 (congratulate on Monday, 10.03.2025)

# Add some notes
> add-note DrChen "Follow up with Dr. Chen about test results" medical,urgent
New note is added

> add-note groceries "Buy groceries for the week" shopping
New note is added

# Find notes with predefined tag(s)
> note-by-tag urgent
  DrChen   Follow up with Dr. Chen about test results   medical, urgent

# Delete tag(s)
> del-tags DrChen urgent
Tags deleted.

```

## 📋 Input Validation Rules

| Field | Rules | Example |
|-------|-------|---------|
| **Phone** | 10 digits | `0501234567`, `6505550100` |
| **Email** | RFC-compliant: `user@domain.ext` format | `user.name+tag@example.com` |
| **Birthday** | Strict `DD.MM.YYYY` format. Validates leap years. Rejects invalid dates (e.g., 31.11.2024) | `12.03.1978`, `29.02.2000` ✅, `29.02.2001` ❌ |
| **Name** | Must be unique (case-insensitive) | `Dr. Maria Chen` |
| **Address** | Multi-word supported | `Hospital St, 15, Apt 4B, Kyiv` |
| **Note text** | Any text in single-line format
| **Tags** | Allowed multiple per note, normalized to lowercase |

## 📁 Data Storage

- **Location:** Current directory
- **Files:** `contacts.json`, `notes.json`
- **Format:** JSON with UTF-8 encoding
- **Versioning:** Each file includes `version: 1` field

## 🔧 Dependencies

- **rich** (for enhanced terminal output and table formatting)
- **colorama** (for cross-platform color support)
- **Python 3.8+** (for modern syntax and features)

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## 👥 Team "Dream32t"

**GoIT Neoversity — November 2025**

* Maksym Sambulat
* Anton Iemelianov
* Marharyta Che
* Letta Savchenko
* Mykola Horb
---

## 📄 License

This project is part of the GoIT Neoversity curriculum.

---

**Note:** All commands follow kebab-case convention. All messages are in English. Data is stored locally with automatic backup and recovery mechanisms.
