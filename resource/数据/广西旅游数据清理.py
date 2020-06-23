import pandas as pd

def clear(data):
    ww = ['Scenic_spot_type', 'Open_time', 'Introduce']
    for i in ww:
        for j in data['序号']:
            if data[i][j] == str(['None']):
                data.drop(data['序号'][j], axis=0, inplace=True)
    print(len(data))
    zz = ['Scenic_spot_name', 'Address', 'Scenic_spot_type', 'Open_time',
          'Ticket_information', 'Ticket_price', 'Introduce', 'Traffic']
    for i in zz:
        for j in data['序号']:
            data[i][j] = data[i][j].replace('\\xa0', '') \
                .replace('\\r\\n', '').replace("', '", "") \
                .replace('\\r', '').replace('\\u3000', '').replace(' ', '')
                #.replace('\n\t', '').replace('\n', '').replace('\n\n', '').replace('\n\n\t', '')

    for i in zz:
        for j in data['序号']:
            data[i][j] = data[i][j].strip("['']")
            data[i][j] = data[i][j].strip("\\n\\t")

    kk = ['Introduce', 'Traffic']
    for i in kk:
        for j in data['序号']:
            if data[i][j] == '':
                data.drop(data['序号'][j], axis=0, inplace=True)

    #print(len(data))
    data.to_excel('G://travel//data.xlsx', encoding='utf-8')
    #print(data)


if __name__ == '__main__':
    data = pd.read_excel(r"G:/travel/scenic_data.xlsx")
    clear(data)