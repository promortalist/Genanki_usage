import genanki
import re
my_model = genanki.Model(
  1607392319,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])
my_deck = genanki.Deck(
  2059400110,
  'Terms about Greek Tragedy')
rr = open("greekgeek.txt","r")
i = 1
for line in rr.readlines():
     morf=str(line)
     i = i + 1
     if len(morf) > 0:
        morf=morf.split(":")
        print(morf[0],morf[1])
        globals()["note" + str(i)] =  genanki.Note(model=my_model, fields=[morf[0], morf[1]])
        my_deck.add_note(globals()["note" + str(i)])
        genanki.Package(my_deck).write_to_file('greekgeek.apkg')
rr.close()
genanki.Package(my_deck).write_to_file('greekgeek.apkg')

