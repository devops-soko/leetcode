class Solution:
    def interpret(self, command: str) -> str:
        if len(command) <1 or len(command) >100:
            return
        if command.replace("G","").replace("()","").replace("(al)","") != "":
            return
        return command.replace("(al)", "al").replace("()", "o")