from note_notebook import Note
from note_notebook import Notebook

my_notebook = Notebook('내꺼')
# print(my_notebook.title)

new_note = Note('수업하기 싫다...')
# print(new_note)

new_note2 = Note('PYTHON...')
# print(new_note2)

my_notebook.add_note(new_note)
my_notebook.add_note(new_note2, 100)

# print(my_notebook.notes)
# print(my_notebook.notes[100])

# print(my_notebook.get_number_of_pages())

my_notebook.notes[2] = Note('hellooooo')
print(my_notebook.notes[2])