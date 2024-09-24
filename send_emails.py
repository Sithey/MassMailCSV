import pandas as pd
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to load CSV data
def load_data(file_path):
    # Read the CSV file using pandas
    df = pd.read_csv(file_path)
    return df

# Function to send an email
def send_email(sender_email, sender_password, receiver_email, subject, body_html, smtp_server, port):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the HTML body to the email
    msg.attach(MIMEText(body_html, 'html'))

    # Configure SSL context for secure connection
    context = ssl.create_default_context()

    try:
        # Connect to the SMTP server using SSL
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            # Send the email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"Email successfully sent to {receiver_email}")
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {str(e)}")

# Function to load the content of an HTML template file
def load_template(template_name):
    # Construct the path to the template file
    template_path = os.path.join('templates', template_name)

    # Check if the template file exists
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"The template file '{template_name}' does not exist in the 'templates' folder.")

    # Read the content of the template file
    with open(template_path, 'r', encoding='utf-8') as file:
        template_content = file.read()
    
    return template_content

# Generate the HTML body by replacing placeholders with data
def generate_html_body(template, data):
    # Dynamically replace placeholders in the HTML template with actual data
    return template.format(**data)

# Function to send mass emails using data from a CSV file
def send_mass_emails(csv_file_path, smtp_server, port, sender_email, sender_password, subject, template_name):
    # Load data from the CSV file
    data = load_data(csv_file_path)

    # Load the HTML template
    template = load_template(template_name)

    # Iterate through each row in the CSV and send an email
    for index, row in data.iterrows():
        # Convert the row to a dictionary for easy access
        row_data = row.to_dict()

        # Generate the HTML body for the email with dynamic data
        body_html = generate_html_body(template, row_data)

        # Send the email
        send_email(sender_email, sender_password, row_data['email'], subject, body_html, smtp_server, port)

if __name__ == "__main__":
    # Load SMTP settings from environment variables
    smtp_server = os.getenv("SMTP_SERVER", "smtp.ionos.com")  # SMTP server, default is IONOS
    port = int(os.getenv("SMTP_PORT", 465))  # Port for SMTP
    sender_email = os.getenv("SMTP_EMAIL")  # Your email from environment
    sender_password = os.getenv("SMTP_PASSWORD")  # Your email password from environment

    # Check if the required environment variables are set
    if not sender_email or not sender_password:
        raise ValueError("SMTP credentials are not set in the environment variables.")

    # Prompt the user to enter the subject of the email
    subject = input("Enter the subject of the email: ")

    # Directory containing CSV files
    emails_folder = 'emails'

    # List available CSV files in the 'emails/' folder
    csv_files = [f for f in os.listdir(emails_folder) if f.endswith('.csv')]

    # Display the available CSV files
    print("Available CSV files:")
    for i, file in enumerate(csv_files):
        print(f"{i + 1}. {file}")

    # Prompt the user to select a CSV file
    file_choice = int(input(f"Select a CSV file (1-{len(csv_files)}): ")) - 1
    csv_file_path = os.path.join(emails_folder, csv_files[file_choice])

    # Directory containing HTML templates
    templates_folder = 'templates'

    # List available HTML templates in the 'templates/' folder
    template_files = [f for f in os.listdir(templates_folder) if f.endswith('.html')]

    # Display the available HTML templates
    print("\nAvailable templates:")
    for i, template in enumerate(template_files):
        print(f"{i + 1}. {template}")

    # Prompt the user to select an HTML template
    template_choice = int(input(f"Select a template (1-{len(template_files)}): ")) - 1
    template_name = template_files[template_choice]

    # Send mass emails using the selected CSV and template
    send_mass_emails(csv_file_path, smtp_server, port, sender_email, sender_password, subject, template_name)
