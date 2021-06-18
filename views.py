from rest_framework.cctv_prediction.services import CrimeService
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","project.settings")

class CrimeAPI(object):

    @staticmethod
    def main():
        crimeservice = CrimeService()
        while 1:
            menu = input('0-Exit\n1-서울CCTV DF')

            if menu == '0':
                break
            elif menu == '1':
                crimeservice.csv({'context': './data/', 'fname': 'cctv_in_seoul'})
            elif menu == '2':
                crimeservice.xls({'context': './data/', 'fname': 'cctv_in_seoul'})
            elif menu == '3':
                crimeservice.csv({'context': './data/', 'fname': 'police_position'})
            elif menu == '4':
                crimeservice.xls({'context': './data/', 'fname': 'police_position'})
            elif menu == '5':
                crimeservice.csv({'context': './data/', 'fname': 'pop_in_seoul'})
            elif menu == '6':
                crimeservice.xls({'context': './data/', 'fname': 'us_unemployment'})
            elif menu == '7':
                crimeservice.csv({'context': './data/', 'fname': 'us_unemployment'})
            else:
                continue

CrimeAPI.main()