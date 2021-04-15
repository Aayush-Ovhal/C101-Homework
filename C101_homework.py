import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFiles(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(fileFrom, "rb")

        dbx.files_upload(f.read(), fileTo)

def main():
    access_token = "oJe3ZVbwrg0AAAAAAAAAARwCeCtmr9eY1p6I71AFhPhUjYxXomggBQIGLB8SoGU9"

    transferData = TransferData(access_token)

    file_from = input("Enter file source: ")
    file_to = "/C101-Homework/"

    transferData.uploadFiles(file_from, file_to)

    print("Uploaded")

main()
    
