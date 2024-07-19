import pathlib

cwd = pathlib.Path.cwd()
print(cwd)
print(cwd.parent)

print('>>>', list(cwd.parents))
print('<<<', list(cwd.glob('*')))