from rest_framework.cctv_prediction.common.entity import FileDTO
from rest_framework.cctv_prediction.common.services import Reader, Printer


class CrimeService(Printer, Reader):
    Printer = Printer()
    reader = Reader()
    file = FileDTO

    def csv(self, payload):
        self.file.context = payload.get('context')
        self.file.fname = payload.get('fname')
        self.printer.dframe(self.reader.csv(self.file))

    def xls(self, payload):
        self.file.context = payload.get('context')
        self.file.fname = payload.get('fname')
        self.printer.dframe(self.reader.xls(self.file))

    def json(self, payload):
        self.file.context = payload.get('context')
        self.file.fname = payload.get('fname')
        self.printer.dframe(self.reader.xls(self.file))

    def new_file(self):
        pass