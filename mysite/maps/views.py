from django.shortcuts import render
import plotly.express as px


def chart(request):
    df = px.data.iris()
    fig = px.density_heatmap(
        df, x="sepal_width", y="sepal_length", marginal_x="rug", marginal_y="histogram")

    chart = fig.to_html()

    context = {'chart': chart}

    return render(request, 'maps/chart.html', context)


def audio(request):
    return render(request, 'maps/audio.html')