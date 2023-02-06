from django.shortcuts import render
import plotly.express as px


def chart(request):
    df = px.data.carshare()

    fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                            mapbox_style="carto-positron")

    chart = fig.to_html()

    context = {'chart': chart}

    return render(request, 'maps/chart.html', context)
