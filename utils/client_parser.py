from openpyxl import load_workbook

from apps.client.models import Client


def load(path, worksheet):
    wb = load_workbook(path, read_only=True)
    ws = wb[worksheet]
    return ws


def _get(data, index):
    try:
        return data[index].value

    except IndexError:
        return None


def parse():

    data = load('utils/clients.xlsx', 'Sheet1')
    first_row = True

    for row in data.rows:

        if first_row:
            first_row = False
            continue

        name = _get(row, 0)
        business_id = _get(row, 2)

        if not business_id or business_id == '000-00-00000':
            continue

        try:
            print('{} / {}'.format(name, business_id))
            Client.objects.create(
                name=name
            )
        except:
            print('Error on {} / {}'.format(name, business_id))
