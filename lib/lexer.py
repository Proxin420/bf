import os

class Tokenizer:
    def __init__(self):
        self.types = {
          "KWORD": [
              ">",
              "<",
              "+",
              "-",
              ".",
              ",",
              "=",
              "[",
              "]",
              "=>",
              "!>",
              "!=>",
              "!!>"
          ]
        }

    def getType(self, token):
        if token in self.types["KWORD"]:
            return "KWORD"
        else:
            return "Value" 

    def lexer(self, code):
        output = code.split("\x20")
        for idx, i in enumerate(output):
            output[idx] = {"type":  self.getType(output[idx]), "value": output[idx]}
        return output

    def parser(self, tokens):
        output = {
            "type": None,
            "body": {
                "type": None,
                "args": []
            }
        }
        if tokens[0]["type"] == "KWORD":
            if tokens[0]["value"] == ">":
                output["type"] = "KWORD"
                output["body"]["type"] = "+idx"
                output["body"]["args"] = tokens[1:]
            elif tokens[0]["value"] == "<": 
                output["type"] = "KWORD"
                output["body"]["type"] = "-idx"
                output["body"]["args"] = tokens[1:] 
            elif tokens[0]["value"] == "+": 
                output["type"] = "KWORD"
                output["body"]["type"] = "+value"
                output["body"]["args"] = tokens[1:]
            elif tokens[0]["value"] == "-": 
                output["type"] = "KWORD"
                output["body"]["type"] = "-value"
                output["body"]["args"] = tokens[1:]
            elif tokens[0]["value"] == "=": 
                output["type"] = "KWORD"
                output["body"]["type"] = "=value"
                output["body"]["args"] = tokens[1:]     
            elif tokens[0]["value"] == ".": 
                output["type"] = "KWORD"
                output["body"]["type"] = "output"
                output["body"]["args"] = tokens[1:]
            elif tokens[0]["value"] == ",": 
                output["type"] = "KWORD"
                output["body"]["type"] = "input"
                output["body"]["args"] = tokens[1:]     
            elif tokens[0]["value"] == "[": 
                output["type"] = "KWORD"
                output["body"]["type"] = "loop"
                output["body"]["args"] = tokens[1:]     
            elif tokens[0]["value"] == "]": 
                output["type"] = "KWORD"
                output["body"]["type"] = "end"
                output["body"]["args"] = tokens[1:]
            elif tokens[0]["value"] == "=>": 
                output["type"] = "KWORD"
                output["body"]["type"] = "if"
                output["body"]["args"] = tokens[1:]
            elif tokens[0]["value"] == "!>": 
                output["type"] = "KWORD"
                output["body"]["type"] = "ifnot"
                output["body"]["args"] = tokens[1:]
            elif tokens[0]["value"] == "!=>": 
                output["type"] = "KWORD"
                output["body"]["type"] = "elseif"
                output["body"]["args"] = tokens[1:]
            elif tokens[0]["value"] == "!!>": 
                output["type"] = "KWORD"
                output["body"]["type"] = "elseifnot"
                output["body"]["args"] = tokens[1:]
        else:
            print("[ERROR] '" + tokens[0]["value"] + "' Is not a keyword")
            exit()
            os.remove("temp.c")

        return output
