class Message:
    
    def __init__(self, description):
        self.description = description
        
    def print_mess(self):
        """ Code for printing out the messages"""
        print(self.description)


# Create messages object
message1 = Message("""You are a warrior given the mission of defeating
the Dragon in the Doom Tower.""")
message2 = Message("""Armed only with a pointy stick, your chances are slim
but, through exploration or sheer will, you can defeat the dragon.""")

# List of messages
mess = [message1, message2]