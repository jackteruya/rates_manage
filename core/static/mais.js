Highcharts.chart('container', {

    title: {
        text: 'Cotação'
    },

    subtitle: {
        text: 'Source: api.vatcomply.com/rates'
    },

    yAxis: {
        title: {
            text: 'Valor $'
        },
    },

    xAxis: {
        accessibility: {
            rangeDescription: 'Range: 2 to 7'
        },
        categories: dataCategories,
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            // pointStart: point_start
        }
    },

    series: [{
        name: coin,
        data: dataQuote,
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 300
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

});