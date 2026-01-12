# Parent class
class Notification:
    def send(self):
        print("Sending notification...")

# Child class 1
class EmailNotification(Notification):
    def send(self):
        print("Sending notification via Email")

# Child class 2
class SMSNotification(Notification):
    def send(self):
        print("Sending notification via SMS")

# Child class 3
class PushNotification(Notification):
    def send(self):
        print("Sending notification via Push Notification")

# Main program
def main():
    notifications = [
        EmailNotification(),
        SMSNotification(),
        PushNotification()
    ]

    for notify in notifications:
        notify.send()   # Polymorphism in action

if __name__ == "__main__":
    main()
