import Chartist from 'chartist';

var oChart = {
    sel: {
        productId: '#product_id',
        pieChart: '#pie-chart',
        barChart: '#bar-chart'
    },
    data: {
        productId: null
    },
    init: function() {
        oChart.data.productId = document.querySelector('#product_id').innerText;
        oChart.getPieChart();
        //oChart.getBarChart();
    },
    getPieChart: function() {
        fetch(`/product/${oChart.data.productId}/recommendationRatio`)
        .then(res => res.json())
        .then(json => {
            let recommend = 0;
            let notRecommend = 0;
            for(let i = 0; i < json.length; i++) {
                if(json[i][0] === "Polecam") {
                    recommend++;
                } else if(json[i][0] === "Nie polecam") {
                    notRecommend++;
                }
            }
            let data = {
                series: [recommend, notRecommend]
            };
            let labels = ['Polecane:', 'Niepolecane:'];

            let options = {
                width: 400,
                height: 400,
                chartPadding: 50,
                labelOffset: 60,
                labelDirection: 'explode',
                labelInterpolationFnc: function(value, idx) {
                    let percentage = Math.round(value / data.series.reduce(oChart.sum) * 100) + '%';
                    return labels[idx] + ' ' + percentage;
                }
            }; 
            new Chartist.Pie(oChart.sel.pieChart, data, options);
        })

    },
    sum: function(a, b) { 
        return a + b 
    }
}

export default oChart;