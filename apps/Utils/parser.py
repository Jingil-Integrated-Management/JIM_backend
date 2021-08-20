from openpyxl import load_workbook

from apps.Client.models import Client
from apps.Division.models import Division
from apps.Drawing.models import Drawing
from apps.Part.models import Part


def load(path, worksheet):
    wb = load_workbook(path, read_only=True)
    ws = wb[worksheet]
    return ws


def parse():

    tmp_drawing = 'SW-'
    CNT = 0  # Just for temporary usage
    worksheets = ['18. Locking Block',
                  '18. Adjustment Plate',
                  '19. Slide Guide Base',
                  '20. Slide Guide Rail',
                  '26. Inter Lock'
                  ]

    for ws in worksheets:
        data = load('apps/Utils/data.xlsx', ws)

        first_row = False
        for row in data.rows:

            if not first_row:
                first_row = True
                continue

            try:
                x = row[0].value
                y = row[1].value
                z = row[2].value
                material = row[3].value
                price = row[4].value
                main_division = row[5].value
                sub_division = row[6].value
                drawing = row[7].value
                client = row[8].value
                material_price = row[9].value
                milling_price = row[10].value
                heat_treat_price = row[11].value

                if x:

                    print('{},{},{} - {}W {}'.format(x,
                          y, z, price, drawing))

                    client_obj, created = Client.objects.get_or_create(
                        name=client
                    )

                    div_obj, created = Division.objects.get_or_create(
                        main_division=main_division,
                        sub_division=sub_division
                        client=client_obj
                    )

                    drawing = Drawing.objects.create(
                        name=tmp_drawing + '%05d' % CNT,
                        client=client_obj,
                    )
                    CNT += 1
                    Part.objects.create(
                        drawing=drawing,
                        division=div_obj,
                        x=x, y=y, z=z,
                        price=price,
                        material=material
                    )

            except IndexError:
                pass


parse()
