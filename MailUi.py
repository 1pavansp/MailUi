import tkinter as tk
from tkinter import messagebox
import smtplib

class MailApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Mail Application")

        self.create_widgets()

    def create_widgets(self):
        # Sender Email
        sender_label = tk.Label(self.root, text="Sender Email:")
        sender_label.pack()
        self.sender_entry = tk.Entry(self.root)
        self.sender_entry.pack()

        # Sender Password
        password_label = tk.Label(self.root, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        # Recipient Email
        recipient_label = tk.Label(self.root, text="Recipient Email:")
        recipient_label.pack()
        self.recipient_entry = tk.Entry(self.root)
        self.recipient_entry.pack()

        # Subject
        subject_label = tk.Label(self.root, text="Subject:")
        subject_label.pack()
        self.subject_entry = tk.Entry(self.root)
        self.subject_entry.pack()

        # Message
        message_label = tk.Label(self.root, text="Message:")
        message_label.pack()
        self.message_text = tk.Text(self.root)
        self.message_text.pack()

        # Send Button
        send_button = tk.Button(self.root, text="Send", command=self.send_email)
        send_button.pack()

    def send_email(self):
        sender_email = self.sender_entry.get()
        password = self.password_entry.get()
        recipient_email = self.recipient_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        try:
            # Connect to SMTP server
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(sender_email, password)

                # Compose email
                email_message = f"Subject: {subject}\n\n{message}"

                # Send email
                smtp.sendmail(sender_email, recipient_email, email_message)

            messagebox.showinfo("Success", "Email sent successfully.")
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Authentication Error", "Failed to authenticate. Please check your credentials.")
        except smtplib.SMTPException as e:
            messagebox.showerror("Error", f"An error occurred while sending the email: {str(e)}")

# Create the Tkinter application window
root = tk.Tk()

# Create the mail application
app = MailApplication(root)

# Run the Tkinter event loop
root.mainloop()
