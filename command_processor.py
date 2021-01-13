class Command:
    def __init__(self, name, description="", command=None):
        self.name = name
        self.description = description
        self.command = command

class CommandProcessor:
    def __init__(self):
        self.commands = {}
        self.executables = []

    def register_command(self, command):
        self.commands[command.name] = command

    def get_commands(self):
        return [self.commands[key] for key in self.commands]

    def execute(self, raw_command):
        parts = raw_command.split(' ')
        try:
            return self.commands[parts[0]].command((parts[1:]))
        except:
            return 'error'
