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
- Name (up to 32 characters, unique, case-insensitive)
- Multiple phone numbers (international E.164 format: `+380501234567`)
- Email addresses (RFC-compliant validation)
- Physical address (up to 300 characters)
- Birthday (DD.MM.YYYY format with leap year validation)

**Automatic validation:**
- Phone numbers normalized to E.164 format (spaces and dashes removed)
- Email addresses verified with RFC standards
- Birthday dates validated including leap years
- Duplicate prevention for phones and contacts

**Flexible editing:**
- Add, change, or delete any field independently
- Multiple phones per contact
- Replace existing emails and addresses
- Safe deletion with confirmation prompts

**Intelligent search by:**
- Name (case-insensitive, partial matching)
- Phone number (exact match after normalization)
- Email address (case-insensitive)
- Birthday date (exact match)

**Birthday intelligence:**
- View upcoming birthdays within N days (default: 7 days)
- Automatic calculation across year boundaries
- Weekend birthdays shown with Monday congratulation dates

### 📝 Powerful Note System with Tags

**Full note lifecycle:**
- Create notes with topics and text (up to 500 characters)
- Edit note content
- Delete notes with confirmation

**Tag-based organization:**
- Tags normalized to lowercase for consistency
- Case-insensitive tag search and comparison
- Remove individual tags while preserving others

**Search capabilities:**
- Search by note topic or text content (case-insensitive substring matching)
- Filter by multiple tags (case-insensitive)
- List all unique tags across all notes (alphabetically sorted)
- View all notes at once

### 💾 Reliable Data Persistence

**Automatic save/load:**
- No manual "save" command needed
- Data stored as JSON in current directory
- Separate files: `contacts.json` and `notes.json`
- UTF-8 encoding with version tracking

**Crash recovery:**
- Atomic writes to temporary files before replacing originals
- Recovery from backup if main file is corrupted
- Graceful error handling with user notifications

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
# Create contact (name only, then add details)
add-contact "Dr. Maria Chen"

# Delete contact (with confirmation)
del-contact "Dr. Maria Chen"

# Add phone (supports multiple phones)
add-phone "Dr. Maria Chen" +380501234567

# Change specific phone number
change-phone "Dr. Maria Chen" +380501234567 +380679876543

# Delete phone from contact
del-phone "Dr. Maria Chen" +380501234567

# Add email
add-email "Dr. Maria Chen" maria.chen@hospital.ua

# Change email
change-email "Dr. Maria Chen" maria.chen@hospital.ua maria.chen@hospital.com

# Delete email
del-email "Dr. Maria Chen"

# Add/update birthday
set-birthday "Dr. Maria Chen" 12.03.1978

# Delete birthday
del-birthday "Dr. Maria Chen"

# Add/update address (multi-word supported)
add-address "Dr. Maria Chen" "Hospital St, 15, Kyiv, 01001"

# Change address
change-address "Dr. Maria Chen" "Hospital St, 15, Kyiv, 01001" "Clinic Ave, 22, Lviv, 79000"

# Delete address
del-address "Dr. Maria Chen"
```

### Contact Search

```bash
# Search by name (partial, case-insensitive)
find-contact Maria

# Upcoming birthdays (default: 7 days)
list-birthdays
list-birthdays 14
```

### Note Management

```bash
# Create note (topic is required)
add-note topic_is_test "Follow up with Dr. Chen about test results"

# Edit note content (topic is required)
change-note topic_is_test "Updated: Follow up completed"

# Delete note (topic is required)
del-note topic_is_test
```

### Note Search & Tags

```bash
# Search by text content (case-insensitive substring)
note-by-text "follow up"

# Search by tags (case-insensitive, matches any tag)
note-by-tags #medical,#urgent

# Add tags to existing note (topic is required)
add-tags topic_is_test #important,#followup

# Remove specific tags from note (topic is required)
del-tags topic_is_test #urgent

# List and sort notes by tags (alphabetically sorted)
sort-notes-tags
```

### System Commands

```bash
# Get help on any command
help
help add-contact

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
Available commands: add-contact, add-phone, add-email, add-address, 
set-birthday, change-phone, change-email, change-address, del-contact, 
del-phone, del-email, del-birthday, del-address, find-contact, 
list-birthdays, add-note, change-note, del-note, note-by-text, 
note-by-tags, add-tags, del-tags, sort-notes-tags, exit

# Build your contact book
> add-contact "Dr. Maria Chen"
Contact 'Dr. Maria Chen' added successfully.

> add-phone "Dr. Maria Chen" +380501234567
Phone number added to contact 'Dr. Maria Chen'.

> add-email "Dr. Maria Chen" maria.chen@hospital.ua
Email added to contact 'Dr. Maria Chen'.

> add-address "Dr. Maria Chen" "Hospital St, 15, Kyiv, 01001"
Address added to contact 'Dr. Maria Chen'.

> set-birthday "Dr. Maria Chen" 12.03.1978
Birthday added to contact 'Dr. Maria Chen'.

# Add some notes
> add-note medical_followup "Follow up with Dr. Chen about test results" #medical #urgent
Note created with topic: medical_followup

> add-note shopping "Buy groceries for the week" #shopping
Note created with topic: shopping

# Check upcoming events
> list-birthdays 14
Upcoming birthdays in next 14 days:
- Dr. Maria Chen: 12.03.2025 (congratulate on Monday, 10.03.2025)

# Find what you need
> find-contact Maria
Found contact: Dr. Maria Chen
Phone: +380501234567
Email: maria.chen@hospital.ua
Address: Hospital St, 15, Kyiv, 01001
Birthday: 12.03.1978

> note-by-tags #urgent
[medical_followup] Follow up with Dr. Chen about test results #medical #urgent

# Manage tags
> sort-notes-tags
Available tags: #medical, #shopping, #urgent

> del-tags medical_followup #urgent
Tags removed from note [medical_followup]. Remaining tags: #medical
```

## 📋 Input Validation Rules

| Field | Rules | Example |
|-------|-------|---------|
| **Phone** | E.164 format: `+` and up to 15 digits. Spaces/dashes allowed (normalized on save) | `+380501234567`, `+1-650-555-0100` |
| **Email** | RFC-compliant: `user@domain.ext` format | `user.name+tag@example.com` |
| **Birthday** | Strict `DD.MM.YYYY` format. Validates leap years. Rejects invalid dates (e.g., 31.11.2024) | `12.03.1978`, `29.02.2000` ✅, `29.02.2001` ❌ |
| **Name** | Max 32 characters. Must be unique (case-insensitive) | `Dr. Maria Chen` |
| **Address** | Max 300 characters. Multi-word supported | `Hospital St, 15, Apt 4B, Kyiv` |
| **Note text** | Max 500 characters. Single-line | Any text up to 500 chars |
| **Note topic** | Required field for note identification | `medical_followup`, `shopping_list` |
| **Tags** | Max 20 per note. Each max 30 chars. Normalized to lowercase | `#work`, `#urgent-2024` |

## 📁 Data Storage

- **Location:** Current directory
- **Files:** `contacts.json`, `notes.json`
- **Format:** JSON with UTF-8 encoding
- **Versioning:** Each file includes `version: 1` field
- **Backup:** Automatic `.bak` files created before each save
- **Recovery:** Automatic fallback to `.bak` if main file is corrupted

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

- Mykola Gorb
- Maksym Sambulat
- Anton Iemelianov
- Marharyta Che
- Letta Savchenko

*"Your personal command-line companion for organized living!"* 💻✨

---

## 🔮 Future Enhancements

- Multi-line notes support
- Export/import functionality (CSV, VCF)
- Calendar integration for birthday reminders
- Color themes customization
- Multiple language support
- Advanced search with operators (AND, OR, NOT)
- Note categories and folders
- Contact groups and tags
- Recurring reminders

## 📄 License

This project is part of the GoIT Neoversity curriculum.

---

**Note:** All commands follow kebab-case convention. All messages are in English. Data is stored locally with automatic backup and recovery mechanisms.
