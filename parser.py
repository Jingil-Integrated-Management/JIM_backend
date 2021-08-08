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
        data = load('data.xlsx', ws)

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
                division = str(row[5].value).split('-')
                division_name = row[6].value
                client = row[7].value

                try:
                    subdivision = int(division[1])
                except:
                    subdivision = None

                if x:

                    print('{},{},{} - {}W {}'.format(x,
                          y, z, price, division_name))

                    div_obj, created = Division.objects.get_or_create(
                        name=division_name,
                        main_division=int(float(division[0])),
                        sub_division=subdivision
                    )

                    client_obj, created = Client.objects.get_or_create(
                        name=client,
                        address=None,
                        contact=None
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
