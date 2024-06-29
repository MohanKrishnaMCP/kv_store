class CommandParser:
    # To handle commands to set/get/delete values
    # eg - set/key/value, get/key, delete/key

    def parse(self, command):
        parts = command.split("/")
        return parts[0].lower, parts[1:]