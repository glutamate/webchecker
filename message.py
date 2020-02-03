class Message:
    INFO=6
    NOTICE=5
    WARN=4
    ERROR=3
    CRITICAL=2

    LEVELS=["","","CRITICAL","ERROR","WARN","NOTICE","INFO"]
    def __init__(self, module, level, text):
        self.module=module
        self.level=level
        self.text=text
    def __iter__(self):
        yield 'module', self.module
        yield 'level', self.level
        yield 'text', self.text
    def __repr__(self):
        return f'Message({self.module!r}, {Message.LEVELS[self.level]}, {self.text!r})'