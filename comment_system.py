
class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False
    
    def add_reply(self, reply):
        if isinstance(reply, Comment):
            self.replies.append(reply)
        else:
            raise TypeError("Reply must be an object of the Comment class")
    
    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True
    
    def display(self, indent=0):
        indent_str = '    ' * indent
        if self.is_deleted:
            print(f"{indent_str}{self.text}")
        else:
            print(f"{indent_str}{self.author}: {self.text}")
        
        for reply in self.replies:
            reply.display(indent + 1)

