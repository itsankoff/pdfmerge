from PDF import PdfFileReader, PdfFileWriter
import os
import sys


def merge(input_dir, output_file):
    output = PdfFileWriter()

    inputs = sorted(os.listdir(input_dir))
    for name in inputs:
        if name.endswith('pdf'):
            path = input_dir + name
            in_file = PdfFileReader(open(path, 'rb'))
            [output.addPage(in_file.getPage(pagenum))
             for pagenum in range(in_file.numPages)]

    output.write(open(output_file, 'wb'))


def main():
    if len(sys.argv) < 3:
        print('Usage: python3 merge.py <directory> <outputfile>.pdf')
        print('Example: python3 merge.py ./ merge.pdf')
        exit()

    in_dir = sys.argv[1]
    out_file = sys.argv[2]
    merge(in_dir, out_file)


if __name__ == '__main__':
    main()
