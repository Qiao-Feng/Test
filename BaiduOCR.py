from aip import AipOcr
import json

APP_ID = '10706210'
API_KEY = 'kh6kczBGNeE6zFDDFS6U6zC4'
SECRET_KEY = 'L8D6xMO5BkVlISKGaG2TP90vhM0yd1eV'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}


def get_file_content(c_filePath):
    with open(c_filePath, 'rb') as fp:
        return fp.read()


if __name__ == '__main__':
    q_filePath = "test.jpg"
    result = aipOcr.basicGeneral(get_file_content(q_filePath), options)
    c_Result_s = ''
    for word_s in result['words_result']:
        c_Result_s = c_Result_s + word_s['words']
    print(c_Result_s)
