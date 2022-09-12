#!/usr/bin/python
import argparse
import subprocess
import os

import lib.lexer
import lib.gen


def ParseArgs():
    Parser = argparse.ArgumentParser(description="Bf++ Compiler")
    Parser.add_argument("Build", help="Build a bf++ program")
    return Parser.parse_args()

def main():
    args = ParseArgs()
    Tokenizer = lib.lexer.Tokenizer()
    CodeGenerator = lib.gen.codeGenerator()
    with open(args.Build) as f:
        for line in f:
            tokens = Tokenizer.lexer(line)
            parsed = Tokenizer.parser(tokens)
            CodeGenerator.CodeGen(parsed)
    CodeGenerator.Close()
    os.system("gcc temp.c -o program")
    print("[CMD] gcc temp.c -o program")
    os.remove("temp.c")
    print("[INFO] Complete compilation")

if __name__ == "__main__":
    main()
