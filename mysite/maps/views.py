from django.shortcuts import render
import plotly.express as px
from .forms import AudioLabelForm
from csv import DictWriter
import os


def chart(request):
    df = px.data.iris()
    fig = px.density_heatmap(
        df, x="sepal_width", y="sepal_length", marginal_x="rug", marginal_y="histogram")

    chart = fig.to_html()

    context = {'chart': chart}

    return render(request, 'maps/chart.html', context)


def audio(request):
    if request.method == "POST":
        form = AudioLabelForm(request.POST)
        if form.is_valid():
            field_names = ["frequency1", "frequency2", "time1", "time2"]
            file_path = "./maps/others/labels.csv"
            write_header = not os.path.exists(file_path)
            with open(file_path, "a", newline="") as csv_file:
                dt = DictWriter(csv_file, fieldnames=field_names)
                if write_header:
                    dt.writeheader()
                dt.writerow(form.cleaned_data)
            print(form.cleaned_data)
        else:
            print("Not valid")

    form = AudioLabelForm()

    return render(request, 'maps/audio.html', {"form": form})
