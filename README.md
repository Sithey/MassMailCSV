# MassMailCSV

**MassMailCSV** is a Python tool that allows you to send mass emails using data from CSV files and customizable HTML templates. The tool is designed to help you send personalized emails to a large number of recipients without having to manually write each email.

## Features

- Send mass emails based on CSV files with dynamic placeholders.
- Use HTML templates stored in a `templates/` folder.
- Secure SMTP credentials with environment variables (`.env` file).
- Select CSV files and templates dynamically during execution.
- Supports SSL connections for SMTP servers.

## Prerequisites

- Python 3.x
- SMTP account (e.g., IONOS, Gmail, etc.)
  
## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Sithey/MassMailCSV.git
    cd MassMailCSV
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file to store your SMTP credentials:

    ```bash
    touch .env
    ```

    Add the following variables to your `.env` file:

    ```env
    SMTP_SERVER=smtp.example.com
    SMTP_PORT=465
    SMTP_EMAIL=your_email@example.com
    SMTP_PASSWORD=your_password
    ```

## Usage

1. Place your CSV files in the `emails/` directory.
2. Place your HTML templates in the `templates/` directory.
3. Run the script:

    ```bash
    python send_emails.py
    ```

4. You will be prompted to:
    - Enter the email subject.
    - Select a CSV file from the `emails/` directory.
    - Select an HTML template from the `templates/` directory.

5. The script will send personalized emails based on the selected CSV file and template.

## Creating HTML Email Templates

We recommend using **[htmleditor.tools](https://htmleditor.tools/)** to easily create and customize your email templates. It's a free online tool that allows you to visually design HTML emails and export them for use in this project. Simply design your template, export the HTML, and save it in the `templates/` directory of your project.

## Example Template:

```html
<html>
<body>
    <h1>Hello {name},</h1>
    <p>Thank you for signing up!</p>
</body>
</html>
```

## Folder Structure
```
/MassMailCSV/
│
├── send_emails.py         # Main Python script to send emails
├── requirements.txt       # Dependencies file
├── .env                   # SMTP credentials (not included in repo)
├── README.md              # Project documentation
│
├── /emails/               # Directory for CSV files
│   └── example.csv        # Sample CSV file with recipient data
│
├── /templates/            # Directory for HTML email templates
│   └── template1.html     # Sample HTML email template
```

## License
This project is licensed under the [MIT License](LICENSE).