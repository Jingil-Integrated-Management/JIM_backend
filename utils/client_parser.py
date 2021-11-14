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
        representative = _get(row, 1)
        business_id = _get(row, 2)
        tel = _get(row, 3)
        fax = _get(row, 4)
        address = _get(row, 5)
        note = _get(row, 6)
        manager = _get(row, 7)
        manager_tel = _get(row, 8)
        manager_phone = _get(row, 9)
        primary_bank = _get(row, 10)
        primary_bank_account = _get(row, 11)
        bank_account_name = _get(row, 12)

        if not business_id or business_id == '000-00-00000':
            continue

        try:
            print('{} / {}'.format(name, business_id))
            Client.objects.create(
                business_id=business_id,
                name=name,
                representative=representative,
                tel=tel,
                fax=fax,
                address=address,
                note=note,
                manager=manager,
                manager_tel=manager_tel,
                manager_phone=manager_phone,
                primary_bank=primary_bank,
                primary_bank_account=primary_bank_account,
                bank_account_name=bank_account_name
            )
        except:
            print('Error on {} / {}'.format(name, business_id))
