data = 'group1.json';
fetch(data).then((response)=> response.json())
.then((final_response) => {
  console.log(final_response);
  Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'ASEAN Population vs. Years'
    },
    subtitle: {
        text: 'Source: <a href="https://datahub.io/core/population-growth-estimates-and-projections/r/population-estimates.csv">World Population Data</a>'
    },
    xAxis: {
        categories: [
            '2004',
            '2005',
            '2006',
            '2007',
            '2008',
            '2009',
            '2010',
            '2011',
            '2012',
            '2013',
            '2014'

        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Population'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    },
    series: final_response
});
              
});
