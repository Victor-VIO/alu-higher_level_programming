#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns length and first character"""
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
