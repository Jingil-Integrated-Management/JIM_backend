from datetime import date

from openpyxl import load_workbook

from apps.client.models import Client
from apps.division.models import Division
from apps.drawing.models import Drawing
from apps.part.models import Part, Material, OutSource


def _get(data, index):
    try:
        if data[index].value != 0:
            return data[index].value
        else:
            return None
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
        data = load('utils/data.xlsx', ws)
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
            material_client = _get(row, 10)
            milling_price = _get(row, 11)
            milling_client = _get(row, 12)
            heat_treat_price = _get(row, 13)
            heat_treat_client = _get(row, 14)
            wire_price = _get(row, 15)
            wire_client = _get(row, 16)

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
                        client=client_obj,
                        is_closed=True,
                        created_at=str(date.today())
                    )

                else:
                    drawing = Drawing.objects.create(
                        name=tmp_drawing + '%05d' % CNT,
                        client=client_obj,
                        is_closed=True,
                        created_at=str(date.today())
                    )
                    CNT += 1

                material_client_obj = Client.objects.get(
                    name=material_client) if material_price else None
                milling_client_obj = Client.objects.get(
                    name=milling_client) if milling_price else None
                heat_treat_client_obj = Client.objects.get(
                    name=heat_treat_client) if heat_treat_price else None
                wire_client_obj = Client.objects.get(
                    name=wire_client) if wire_price else None

                outsource = None

                if material_price or milling_price or \
                        heat_treat_price or wire_price:
                    outsource = OutSource.objects.create(
                        material_price=int(
                            material_price) if material_price else None,
                        milling_price=int(
                            milling_price) if milling_price else None,
                        heat_treat_price=int(
                            heat_treat_price) if heat_treat_price else None,
                        wire_price=int(
                            wire_price) if wire_price else None,
                        material_client=material_client_obj,
                        milling_client=milling_client_obj,
                        heat_treat_client=heat_treat_client_obj,
                        wire_client=wire_client_obj
                    )

                material_obj, _ = Material.objects.get_or_create(
                    name=material
                )

                Part.objects.create(
                    drawing=drawing,
                    division=div_obj,
                    x=x, y=y, z=z,
                    price=int(price),
                    material=material_obj,
                    outsource=outsource
                )
