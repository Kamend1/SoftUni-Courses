from abc import ABC, abstractmethod


class ISenderReceiver(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def set_name(self):
        pass


class IProtocol(ABC):

    def __init__(self, text: str):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class MyML(IProtocol):

    def format(self):
        return '\n'.join(['<MyML>', self.text, '</MyML>'])


class HTML(IProtocol):

    def format(self):
        return '\n'.join(['<html>', self.text, '</html>'])


class Sender(ISenderReceiver):

    def set_name(self):
        return ''.join(["I'm ", self.name])


class Receiver(ISenderReceiver):

    def set_name(self):
        return ''.join(["I'm ", self.name])


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.set_name()


    def set_receiver(self, receiver):
        self.__receiver = receiver.set_name()

    def set_content(self, content: IProtocol):
            self.__content = content.format()


    def __repr__(self):

        template = f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"

        return template


email = Email('IM')
sender = Sender('gmal')
email.set_sender(sender)
receiver = Receiver('james')
email.set_receiver(receiver)
content = HTML('Hello, there!')
email.set_content(content)
print(email)

