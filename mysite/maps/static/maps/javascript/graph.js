let freq1 = document.getElementById("id_frequency1");
let freq2 = document.getElementById("id_frequency2");
let time1 = document.getElementById("id_time1");
let time2 = document.getElementById("id_time2");


var graphDiv = document.getElementById('myDiv');
var N = 1000;
var color1 = '#7b3294';
var color1Light = '#c2a5cf';
var colorX = '#ffa7b5';
var colorY = '#fdae61';

function randomArray() {
    var out = new Array(N);
    for (var i = 0; i < N; i++) {
        out[i] = Math.random();
    }
    return out;
}
var x = randomArray();
var y = randomArray();

Plotly.newPlot(graphDiv, [{
    type: 'scatter',
    mode: 'markers',
    x: x,
    y: y,
    xaxis: 'x',
    yaxis: 'y',
    name: 'random data',
    marker: { color: color1, size: 10 }
}, {
    type: 'histogram',
    x: x,
    xaxis: 'x2',
    yaxis: 'y2',
    name: 'x coord dist.',
    marker: { color: colorX }
}, {
    type: 'histogram',
    x: y,
    xaxis: 'x3',
    yaxis: 'y3',
    name: 'y coord dist.',
    marker: { color: colorY }
}], {
    title: 'Lasso around the scatter points to see sub-distributions',
    dragmode: 'lasso',
    xaxis: {
        zeroline: false,
    },
    yaxis: {
        domain: [0.55, 1],
    },
    xaxis2: {
        domain: [0, 0.45],
        anchor: 'y2',
    },
    yaxis2: {
        domain: [0, 0.45],
        anchor: 'x2'
    },
    xaxis3: {
        domain: [0.55, 1],
        anchor: 'y3'
    },
    yaxis3: {
        domain: [0, 0.45],
        anchor: 'x3'
    }
});

graphDiv.on('plotly_selected', function (eventData) {
    var x = [];
    var y = [];

    var colors = [];
    for (var i = 0; i < N; i++) colors.push(color1Light);

    eventData.points.forEach(function (pt) {
        let convertX = parseFloat(pt.x)
        let convertY = parseFloat(pt.y)
        freq1.value = convertX;
        time1.value = convertY;
        freq2.value = convertX + 0.1;
        time2.value = convertY + 0.1;
        console.log(typeof pt.x)
        x.push(pt.x);
        y.push(pt.y);
        colors[pt.pointNumber] = color1;
    });

    Plotly.restyle(graphDiv, {
        x: [x, y],
        xbins: {}
    }, [1, 2]);

    Plotly.restyle(graphDiv, 'marker.color', [colors], [0]);
});
