from PyPDF2 import PdfFileWriter, PdfFileReader




datas = {
    'Project': 'THE DILLON',
    'Task':'RX10',
    'CheckBox': '/yes',
    }

check_request= PdfFileReader('Check_Request.pdf')

print(check_request.getFields())

page = check_request.getPage(0)

output = PdfFileWriter()
output.insertPage(page)
output.updatePageFormFieldValues(page,datas)
with open('Check_Request_new.pdf', 'wb') as out:
    output.write(out)

