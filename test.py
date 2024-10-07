import difflib

system = """Hello is mrhc"""

hmrc = """Hello this is hmrc""" 


if system == hmrc:
    print("Correct")
else:
    print("Incorrect")
    system_words = system.split()
    hmrc_words = hmrc.split()
    d = difflib.Differ()
    diff = d.compare(system_words, hmrc_words)
    print('\n'.join(diff))