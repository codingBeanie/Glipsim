document.addEventListener('DOMContentLoaded', function () {
    graph_survival();
    graph_reproduction();
    graph_probabilities();
});


function graph_survival() {
    let x = data_survival.map(element => element[0]);
    let y = data_survival.map(element => element[1]);

    let trace = {
        x: x,
        y: y,
        type: 'scatter',
        name: 'survival',
        marker: { color: 'rgb(0,0,200)' }
    }

    let layout = {
        title: 'Survival Probability',
        xaxis: {
            title: 'Age'
        },
        yaxis: {
            title: 'Survival Rate'
        }
    };

    Plotly.newPlot('plot_survival', [trace], layout);
}

function graph_reproduction() { 
    let x = data_reproduction.map(element => element[0]);
    let y = data_reproduction.map(element => element[1]);

    let trace = {
        x: x,
        y: y,
        type: 'scatter',
        name: 'reproduction',
        marker: { color: 'rgb(0,0,200)' }
    }

    let layout = {
        title: 'Reproduction Probability',
        xaxis: {
            title: 'Age'
        },
        yaxis: {
            title: 'Reproduction Rate'
        }
    };

    Plotly.newPlot('plot_reproduction', [trace], layout);
}

function graph_probabilities() {
    let trace_reproduction_age = {
        x: data_evaluation_reproduction_age.map(element => element[0]),
        y: data_evaluation_reproduction_age.map(element => element[1]),
        type: 'scatter',
        name: 'reproduction/age',
        marker: { color: 'rgb(0,0,200)' }
    }
    let layout_reproduction = {
        title: 'Probability of Reproduction',
    }
    traces = [trace_reproduction_age];
    Plotly.newPlot('plot_evaluation_reproduction', traces, layout_reproduction);
}