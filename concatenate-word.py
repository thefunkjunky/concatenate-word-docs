"""
Concatenates word documents together
"""
import os
import argparse

import docx


def main():
  """Concatenate word documents"""
  parser = argparse.ArgumentParser(
    description="Concatenate word docs."
  )
  parser.add_argument(
    "output_file",
    type=str,
    help="Concatenated output file.")
  parser.add_argument(
    "-f",
    "--files",
    nargs="+",
    help="Files to concatenate."
  )
  args = parser.parse_args()

  files = []
  not_files = []
  not_word_files = []
  for filename in args.files:
    if not filename.endswith(".docx"):
      not_word_files.append(filename)
    if os.path.exists(filename):
      files.append(os.path.abspath(filename))
    else:
      not_files.append(filename)
  if not_files:
    print(f"{not_files} are not files.")
    exit()
  if not_word_files:
    print(f"{not_word_files} are not Word files (.docx).")
    exit()

  concatenated_word = docx.Document()
  for index, filename in enumerate(files):
    subdoc = docx.Document(filename)

    if index < len(files) - 1:
      subdoc.add_page_break()

    for element in subdoc.element.body:
      concatenated_word.element.body.append(element)

  concatenated_word.save(args.output_file)



if __name__ == '__main__':
  main()
