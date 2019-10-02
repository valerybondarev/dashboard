
var months;
var critical_data;
var high_data;
var medium_data;
var low_data;

  $(document).ready(function () {
    $.ajax({
      url: '/get_report_data',
      type: 'post',
      success: function (response) {
        console.log(response);
        months = response['months'];
        critical_data = response['critical_data'];
        high_data = response['high_data'];
        medium_data = response['medium_data'];
        low_data = response['low_data'];


        var ctx = document.getElementById('myChart').getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: months,
      datasets: [{
        label: 'Critical',
        data: critical_data,
        backgroundColor: "rgba(237,85,101,0.7)"
      }, {
        label: 'High',
        data: high_data,
        backgroundColor: "rgba(248,172,89,1)"
      }, {
        label: 'Medium',
        data: medium_data,
        backgroundColor: "rgba(35,198,200,0.8)"
      }, {
        label: 'Low',
        data: low_data,
        backgroundColor: "rgba(28,132,198,0.5)"
      }]
    },
    options: {
      maintainAspectRatio: false,
      animation: {
        duration: 0
      },
      scales: {
        yAxes: [{
          ticks: {
            stepSize: 1,
            min: 0,
            suggestedMax: 4
          },
          scaleLabel: {
            labelString: 'Number of Issues',
            display: true
          }

        }]
      }
    }
  });
      }
    });
  });


