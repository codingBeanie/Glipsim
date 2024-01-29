document.addEventListener('DOMContentLoaded', function() {
    fetch_statistics();
});

function fetch_statistics() { 
    fetch('api/get_stats')
        .then(response => response.json())
        .then(data => {
            graph_population(data)
            graph_appearance(data)
            graph_preference(data)
            graph_tolerance_dating(data)
            graph_tolerance_age(data)
            graph_health(data)
            graph_actions(data)
            graph_death_age(data)
        })
        .catch(error => console.error(error));
}

function graph_population(data) { 
    let trace_population = {
        x: data.map(d => d.tick),
        y: data.map(d => d.population),
        type: 'scatter',
        marker: { color: 'rgb(50,50,200)' }
    }
    let trace_births = {
        x: data.map(d => d.tick),
        y: data.map(d => d.births),
        type: 'scatter',
        name: 'births',
        marker: { color: 'green' }
    }
    let trace_deaths = {
        x: data.map(d => d.tick),
        y: data.map(d => d.deaths),
        type: 'scatter',
        name: 'Deaths',
        marker: { color: 'red' }
    }

    trace_population = [trace_population]
    trace_changes = [trace_births, trace_deaths]

    let layout_population = {
        title: 'Population Developement',
        xaxis: {
            title: 'Tick',
            range: [0, undefined]
        },
        yaxis: {
            title: 'Population'
        }
    }

    let layout_change = {
        title: 'Deaths and Births',
        xaxis: {
            title: 'Tick'
        },
        yaxis: {
            title: '# Glips'
        }
    }


    Plotly.newPlot('plot_population', trace_population, layout_population)
    Plotly.newPlot('plot_births_deaths', trace_changes, layout_change)
}

function graph_appearance(data) {
    let trace_red = {
        x: data.map(d => d.tick),
        y: data.map(d => d.appearance_red),
        type: 'scatter',
        name: 'red',
        marker: { color: 'rgb(200,0,0)' }
    }
    let trace_blue = {
        x: data.map(d => d.tick),
        y: data.map(d => d.appearance_blue),
        type: 'scatter',
        name: 'blue',
        marker: { color: 'rgb(0,0,200)' }
    }
    let trace_green = {
        x: data.map(d => d.tick),
        y: data.map(d => d.appearance_green),
        type: 'scatter',
        name: 'green',
        marker: { color: 'rgb(0, 200, 0)' }
    }
    let trace_yellow = {
        x: data.map(d => d.tick),
        y: data.map(d => d.appearance_yellow),
        type: 'scatter',
        name: 'yellow',
        marker: { color: 'rgb(230, 230, 0)' }
    }
    let trace_black = {
        x: data.map(d => d.tick),
        y: data.map(d => d.appearance_black),
        type: 'scatter',
        name: 'black',
        marker: { color: 'rgb(50, 50, 50,)' }
    }
    let trace_white = {
        x: data.map(d => d.tick),
        y: data.map(d => d.appearance_white),
        type: 'scatter',
        name: 'white',
        marker: { color: 'rgb(180, 180, 180)' }
    }
    let trace_pink = {
        x: data.map(d => d.tick),
        y: data.map(d => d.appearance_pink),
        type: 'scatter',
        name: 'pink',
        marker: { color: 'rgb(200, 0, 200)' }
    }
    let trace_turq = {
        x: data.map(d => d.tick),
        y: data.map(d => d.appearance_turq),
        type: 'scatter',
        name: 'turq',
        marker: { color: 'rgb(0, 200 , 200)' }
    }
    let layout = {
        title: 'Appearance of Glips',
        xaxis: {
            title: 'Tick'
        },
        yaxis : {title: 'Relative share [%]'}
    }

    trace = [trace_red, trace_blue, trace_green, trace_yellow, trace_black, trace_white, trace_pink, trace_turq]
    Plotly.newPlot('plot_appearance', trace, layout)
}

function graph_preference(data) {
    let trace_red = {
        x: data.map(d => d.tick),
        y: data.map(d => d.preference_red),
        type: 'scatter',
        name: 'red',
        marker: { color: 'rgb(200,0,0)' }
    }
    let trace_blue = {
        x: data.map(d => d.tick),
        y: data.map(d => d.preference_blue),
        type: 'scatter',
        name: 'blue',
        marker: { color: 'rgb(0,0,200)' }
    }
    let trace_green = {
        x: data.map(d => d.tick),
        y: data.map(d => d.preference_green),
        type: 'scatter',
        name: 'green',
        marker: { color: 'rgb(0, 200, 0)' }
    }
    let trace_yellow = {
        x: data.map(d => d.tick),
        y: data.map(d => d.preference_yellow),
        type: 'scatter',
        name: 'yellow',
        marker: { color: 'rgb(230, 230, 0)' }
    }
    let trace_black = {
        x: data.map(d => d.tick),
        y: data.map(d => d.preference_black),
        type: 'scatter',
        name: 'black',
        marker: { color: 'rgb(50, 50, 50)' }
    }
    let trace_white = {
        x: data.map(d => d.tick),
        y: data.map(d => d.preference_white),
        type: 'scatter',
        name: 'white',
        marker: { color: 'rgb(180, 180, 180)' }
    }
    let trace_pink = {
        x: data.map(d => d.tick),
        y: data.map(d => d.preference_pink),
        type: 'scatter',
        name: 'pink',
        marker: { color: 'rgb(200, 0, 200)' }
    }
    let trace_turq = {
        x: data.map(d => d.tick),
        y: data.map(d => d.preference_turq),
        type: 'scatter',
        name: 'turq',
        marker: { color: 'rgb(0, 200 , 200)' }
    }
    let layout = {
        title: 'Preferred Appearance of Glips',
        xaxis: {
            title: 'Preference'
        },
        yaxis: { title: 'Relative share [%]' }
    }

    trace = [trace_black, trace_blue, trace_green, trace_yellow, trace_red, trace_white, trace_pink, trace_turq]
    Plotly.newPlot('plot_preference', trace, layout)
}

function graph_tolerance_dating(data) { 
    let trace_0 = {
        x: data.map(d => d.tick),
        y: data.map(d => d.tolerance_dating_0),
        type: 'scatter',
        name: '0',
        marker: { color: 'rgb(200,0,0)' }
    }
    let trace_1 = {
        x: data.map(d => d.tick),
        y: data.map(d => d.tolerance_dating_1),
        type: 'scatter',
        name: '1',
        marker: { color: 'rgb(200,50,0)' }
    }
    let trace_2 = {
        x: data.map(d => d.tick),
        y: data.map(d => d.tolerance_dating_2),
        type: 'scatter',
        name: '2',
        marker: { color: 'rgb(100,100,0)' }
    }
    let trace_3 = {
        x: data.map(d => d.tick),
        y: data.map(d => d.tolerance_dating_3),
        type: 'scatter',
        name: '3',
        marker: { color: 'rgb(0,200,0)' }
    }

    let layout = {
        title: 'Tolerance of Dating',
        xaxis: {
            title: 'Tick'
        },
        yaxis: {
            title: 'Relative share [%]'
        }
    }
    trace = [trace_0, trace_1, trace_2, trace_3]
    Plotly.newPlot('plot_tolerance_dating', trace, layout)
}

function graph_tolerance_age(data) { 
    let trace_younger = {
        x: data.map(d => d.tick),
        y: data.map(d => d.tolerance_age_younger),
        type: 'scatter',
        name: 'prefer younger',
        marker: { color: 'rgb(200,0,0)' }
    }
    let trace_similiar = {
        x: data.map(d => d.tick),
        y: data.map(d => d.tolerance_age_similiar),
        type: 'scatter',
        name: 'prefer similiar',
        marker: { color: 'rgb(200, 200,200)' }
    }
    let trace_older = {
        x: data.map(d => d.tick),
        y: data.map(d => d.tolerance_age_older),
        type: 'scatter',
        name: 'prefer older',
        marker: { color: 'rgb(0,0,200)' }
    }

    let layout = {
        title: 'Tolerance of Age',
        xaxis: {
            title: 'Tick'
        },
        yaxis: {
            title: 'Relative share [%]'
        }
    }
    trace = [trace_younger, trace_similiar, trace_older]
    Plotly.newPlot('plot_tolerance_age', trace, layout)
}

function graph_health(data) {
    let trace_avg = {
        x: data.map(d => d.tick),
        y: data.map(d => d.average_health),
        type: 'scatter',
        name: 'avg',
        marker: { color: 'rgb(200,0,0)' }
    }
    let layout = {
        title: 'Health',
        xaxis: {
            title: 'Tick'
        },
        yaxis: {
            title: 'Average Health'
        }
    }

    trace = [trace_avg]
    Plotly.newPlot('plot_health', trace, layout)
}

function graph_actions(data) {
    let trace_idle = {
        x: data.map(d => d.tick),
        y: data.map(d => d.action_idle),
        type: 'scatter',
        name: 'idle',
        marker: { color: 'rgb(200,200,200)' }
    }
    let trace_dating = {
        x: data.map(d => d.tick),
        y: data.map(d => d.action_dating),
        type: 'scatter',
        name: 'dating',
        marker: { color: 'rgb(200,0,0)' }
    }
    let trace_mating = {
        x: data.map(d => d.tick),
        y: data.map(d => d.action_mating),
        type: 'scatter',
        name: 'mating',
        marker: { color: 'rgb(0,200,0)' }
    }

    let layout = {
        title: 'Actions',
        xaxis: {
            title: 'Tick'
        },
        yaxis: {
            title: 'Relative share [%]'
        }
    }

    trace = [trace_idle, trace_dating, trace_mating]
    Plotly.newPlot('plot_actions', trace, layout)
 }

 function graph_death_age(data) {
    let trace = {
        x: data.map(d => d.tick),
        y: data.map(d => d.average_death_age),
        type: 'scatter',
        name: 'Age of Dying',
        marker: { color: 'red' }
    }
    let layout = {
        title: 'Age of Dying',
        xaxis: {
            title: 'Age'
        },
        yaxis: {
            title: 'Average age of dying'
        }
    }

    trace = [trace]
    Plotly.newPlot('plot_death_age', trace, layout)
 }