def main():
  file_path = "books/frankenstein.txt"
  content = read_file_content(file_path)
  total_words = numbers_of_words(content)
  print(total_words)

def read_file_content(path):
  with open(path) as f:
    file_contents = f.read()
  return file_contents

def numbers_of_words(text):
  words = text.split()
  return len(words)

main()





    