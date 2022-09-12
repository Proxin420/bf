

class codeGenerator:
    def __init__(self):
        self.File = open("temp.c", "w+")
        self.File.write("""
#include <stdio.h>
int main() {
char array[3000];
char *idx = array;
        """)

    def CodeGen(self, i):
        if i["body"]["type"] == "+idx":
            self.File.write("\nfor (int i = 0; i < " + str(int(i["body"]["args"][0]["value"]) + 1) + "; i++) {\nidx++;\n}")
        elif i["body"]["type"] == "-idx":
            self.File.write("\nfor (int i = 0; i < " + str(int(i["body"]["args"][0]["value"]) + 1) + "; i++) {\nidx--;\n}")
        elif i["body"]["type"] == "+value":
            self.File.write("\nfor (int i = 0; i < " + str(int(i["body"]["args"][0]["value"]) + 1) + "; i++) {\n++*idx;\n}")
        elif i["body"]["type"] == "-value":
            self.File.write("\nfor (int i = 0; i < " + str(int(i["body"]["args"][0]["value"]) + 1) + "; i++) {\n--*idx;\n}")
        elif i["body"]["type"] == "=value":
            self.File.write("\n*idx = " + i["body"]["args"][0]["value"] + ";\n")
        elif i["body"]["type"] == "output":
            self.File.write("\nputchar(*idx);\n") 
        elif i["body"]["type"] == "input":
            self.File.write("\n*idx = getchar();\n")
        elif i["body"]["type"] == "loop":
            self.File.write("\nwhile (*idx !=  " + i["body"]["args"][0]["value"] + ") {\n")
        elif i["body"]["type"] == "end":
            self.File.write("\n}\n")
        elif i["body"]["type"] == "if":
            self.File.write("\nif (*idx == " + i["body"]["args"][0]["value"] + ") {\n")
        elif i["body"]["type"] == "ifnot":
            self.File.write("\nif (*idx != " + i["body"]["args"][0]["value"] + ") {\n")
        elif i["body"]["type"] == "elseif":
            self.File.write("\nelse if (*idx == " + i["body"]["args"][0]["value"] + ") {\n")
        elif i["body"]["type"] == "elseifnot":
            self.File.write("\nelse if (*idx != " + i["body"]["args"][0]["value"] + ") {\n")
    def Close(self):
        self.File.write("\n}")
        self.File.close()