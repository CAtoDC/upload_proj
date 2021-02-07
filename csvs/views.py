import csv
from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import CsvModelForm
from .models import Csv
from sales.models import Sale


def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()  # reset the form after save
        obj = Csv.objects.get(activated=False)
        with open(obj.filename.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):  # handles header
                if i == 0:
                    pass
                else:
                    row = ''.join(row)
                    row = row.replace(';', ' ')  # delimiter replaced with space
                    row = row.split()   # list items split on space
                    product = row[1].upper()
                    user = User.objects.get(username=row[3])
                    Sale.objects.create(
                        product = product,
                        quantity = int(row[2]),
                        salesman = user
                    )
                    # print(row)
                    # print(type(row))
            obj.activated = True
            obj.save()
    context = {
        'form': form
    }
    return render(request, "csvs/upload.html", context)

