import logging
import os
from datetime import date, timedelta

import nltk
from nltk.corpus import wordnet as wn

directory = '/Users/gpanez/Documents/news/lemmas'


class LemmaExplorer:
    def __init__(self):
        self.verb_triggers = ["resign", "run", "announce", "challenge", "promote", "demote", "exit",
                              "sign", "agreement", "vote", "quit", "condemn", "leave", "appear",
                              "hold", "refuse", "win", "lose", "appoint", "give",
                              "approve", "negotiate", "reject", "refuse", "dismiss",
                              "publish", "launch", "endorse", "elect", "form", "open", "fundrise"]
        self.noun_triggers = ["speech", "nomination", "debate", "statement", "commission", "march"]
        #statement, commission, "march", "stand", "express"
        self.triggerLemmas = set()

    def get_lemmas(self):
        for trigger in self.verb_triggers:
            for synset in wn.synsets(trigger, pos='v'):
                lemmas = [l.name() for l in synset.lemmas()]
                for lemma in lemmas:
                    self.triggerLemmas.add(lemma)
        return

    def print_lemmas(self):
        self.get_lemmas()
        with open(directory + '/lemmas.txt', 'w') as file:
            file.write(str(len(self.triggerLemmas)) + '\n')
            for lemma in self.triggerLemmas:
                file.write(lemma + '\n')


def main():
    logging.basicConfig(filename=directory + '/log.txt',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)
    logging.info("Lemma Explorer")
    logging.getLogger('LE')
    le = LemmaExplorer()
    le.print_lemmas()


if __name__ == '__main__':
    main()
