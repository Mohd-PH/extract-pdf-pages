import argparse
from PyPDF2 import PdfFileWriter, PdfFileReader



def split(inputFileName, outputFileName, startPage, endPage):
    inputpdf = PdfFileReader(open(inputFileName, "rb"))
    output = PdfFileWriter()

    for i in range(startPage - 1, endPage):
        output.addPage(
                inputpdf.getPage(i)
            )

    with open(outputFileName, "wb") as outputStream:
        output.write(outputStream)

def main():
    parser = argparse.ArgumentParser(
            prog="split-pdf",
            description="Split a pdf file by pages\npy extractpdf.py ./inputfile.pdf 1-20 ./outputfile.pdf",
        )
    parser.add_argument("inputFileName", help = "Input file");
    parser.add_argument("pages", help = "Pages to extract, first page(inclusive)-last page(inclusive), eg: 1-20");
    parser.add_argument("outputFileName", help = "Output file");
    args = parser.parse_args()

    # Parse pages
    startPage = int(args.pages.split("-")[0])
    endPage = int(args.pages.split("-")[1])

    split(args.inputFileName, args.outputFileName, startPage, endPage)

if __name__ == "__main__":
    main()
