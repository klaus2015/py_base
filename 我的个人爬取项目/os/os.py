import os
import pathlib
# value1 = os.path.dirname(__file__)
# value2 = os.getcwd()
# print(value1)
# print(value2)
#
# val = pathlib.Path.cwd()
# print(val)
# print(os.path.dirname(os.path.dirname(os.getcwd())))
#
#
# print(pathlib.Path.cwd().parent.parent.parent)
# print(os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), "关注", "微信公众号", "【进击的", "Coder】"))
#
# parts = ["关注", "微信公众号", "【进击的", "Coder】"]
# print(pathlib.Path.cwd().parent.parent.joinpath(*parts))
#
#
# print(pathlib.PurePath(__file__).match('*.py'))

os_path = os.path.dirname(__file__)
pure_path = pathlib.PurePath(__file__)
print(os_path, type(os_path))
print(pure_path, type(pure_path))
print(pathlib.PurePath(__file__).match('*.py'))
