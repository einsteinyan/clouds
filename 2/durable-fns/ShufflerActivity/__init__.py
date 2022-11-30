# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from collections import Counter

def main(wordList: list) -> list:
    output = list()
    for word in wordList:
        entry = (word[0], [1] * wordList.count(word))
        if entry not in output:
            output.append(entry)
    return output

