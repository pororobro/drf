from rest_framework.cctv_prediction.abstracts import PrinterBase , ReaderBase, Read
from rest_framework.cctv_prediction.common.entity import FileDTO
import pandas as pd
import json

class Printer(PrinterBase):

    def dframe(self,this):

        n = 10
        print('*' * 100)
        print(f'1. Target의 Type은 {type(this)}')
        print(f'2. Target의 Type은 {type(this)}')
        print(f'3. Target의 Type은 {type(this)}')
        print(f'4. Target의 Type은 {type(this)}')

class Reader(ReaderBase):
    def new_file(self, file) -> str:
        return file.context + file.fname

    def csv(self, file) -> object:
        return pd.read_csv(f'{self.new_file(file)}.csv', encoding='UTF-8')

    def xls(self, file) -> object:
        return pd.read_excel(f'{self.new_file(file)}.xls')

    def json(self, file) -> object:
        return pd.read_json(f'{self.new_file(file)}.json', encoding='UTF-8')

    def create_gmaps(self):
        pass
