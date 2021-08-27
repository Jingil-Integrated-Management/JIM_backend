from openpyxl import load_workbook

from apps.Client.models import Client
from apps.Division.models import Division
from apps.Drawing.models import Drawing
from apps.Part.models import Part


def _get(data, index):
    try:
        return data[index].value

    except IndexError:
        return None


def load(path, worksheet):
    wb = load_workbook(path, read_only=True)
    ws = wb[worksheet]
    return ws


def parse():

    tmp_drawing = 'SW-'
    CNT = 0  # Just for temporary usage
    worksheets = ['상우정밀', '성우금형(제작)']

    for ws in worksheets:
        data = load('apps/Utils/data.xlsx', ws)
        first_row = False

        for row in data.rows:

            if not first_row:
                first_row = True
                continue

            x = str(_get(row, 0))
            y = str(_get(row, 1))
            z = str(_get(row, 2))
            material = _get(row, 3)
            price = _get(row, 4)
            main_division = _get(row, 5)
            sub_division = _get(row, 6)
            drawing = _get(row, 7)
            client = _get(row, 8)
            material_price = _get(row, 9)
            milling_price = _get(row, 10)
            heat_treat_price = _get(row, 11)
            wire_price = _get(row, 12)

            try:
                main_division = int(main_division)
            except:
                pass
            try:
                sub_division = int(sub_division)
            except:
                pass

            if not main_division or main_division == ' ':
                continue

            if x:

                print('{},{},{} - {}W {}'.format(x,
                                                 y, z, price, drawing))

                client_obj, _ = Client.objects.get_or_create(
                    name=client
                )

                div_obj, _ = Division.objects.get_or_create(
                    main_division=main_division,
                    sub_division=sub_division,
                    client=client_obj
                )

                if drawing:
                    drawing, _ = Drawing.objects.get_or_create(
                        name=drawing,
                        client=client_obj
                    )

                else:
                    drawing = Drawing.objects.create(
                        name=tmp_drawing + '%05d' % CNT,
                        client=client_obj,
                    )
                    CNT += 1

                Part.objects.create(
                    drawing=drawing,
                    division=div_obj,
                    x=x, y=y, z=z,
                    price=int(price),
                    material=material,
                    client=client_obj,
                    material_price=int(
                        material_price) if material_price else None,
                    milling_price=int(
                        milling_price) if milling_price else None,
                    heat_treat_price=int(
                        heat_treat_price) if heat_treat_price else None,
                    wire_price=int(
                        wire_price) if wire_price else None
                )


parse()
