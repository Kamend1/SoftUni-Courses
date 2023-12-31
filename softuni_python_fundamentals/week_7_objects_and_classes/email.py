class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False
    def send(self):
        self.is_sent = True
    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []
user_command = input().split()

while user_command[0] != "Stop":
    sender, receiver, content = user_command[0], user_command[1], user_command[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    user_command = input().split()

send_emails = list(map(lambda x: int(x), input().split(', ')))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())
