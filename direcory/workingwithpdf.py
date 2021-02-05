import PyPDF2

# it is very important to open in binary mode
with open("first.pdf", "rb") as file:

    # where file is a stream
    reader = PyPDF2.PdfFileReader(file)

    # getting pages in our pdf file
    x = reader.numPages

    # page objects its start from 0 index
    page = reader.getPage(0)

    # down method doesnot modified original pdf its only this is only rotating page object
    page.rotateClockwise(90)

    # so we need to store in different
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)

    with open("rotated.pdf", "wb") as output:
        writer.write(output)

# combining multiple pdf into single

merge = PyPDF2.PdfFileMerger()
file_name = ["first.pdf", "second.pdf"]
for filename in file_name:
    merge.append(filename)

merge.write("combine.pdf")
