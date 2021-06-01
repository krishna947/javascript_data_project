data = 'saarc1.json';
fetch(data).then((response)=> response.json())
.then((final_response) => {
  console.log(final_response);
  Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Total Population of SAARC Countries over the years'
    },
    subtitle: {
        text: 'Source: <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">World Population Data</a>'
    },
    xAxis: {
        title: {
          text: 'Years'
        },
        type: 'category',
        labels: {
            rotation: -45,
            style: {
                fontSize: '13px',
                fontFamily: 'Verdana, sans-serif'
            }
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Population'
        }
    },
    legend: {
        enabled: false
    },
    series: [{
        name: 'Population',
        data: final_response,
        dataLabels: {
            enabled: true,
            rotation: -90,
            color: '#FFFFFF',
            align: 'right',
            format: '{point.y:.1f}', // one decimal
            y: 10, // 10 pixels down from the top
            style: {
                fontSize: '13px',
                fontFamily: 'Verdana, sans-serif'
            }
        }
    }]
  });
});
