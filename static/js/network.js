// Call the dataTables jQuery plugin
$(document).ready(function() {

  $('#dataTable').DataTable({
      "processing": true,
        "serverSide": true,
        ajax: {
            url: '/data_source',
            type: 'POST'
        },
      "lengthChange": false,
          "columns": [
                { "data": "ip_address" },
                { "data": "hostnames" },
                { "data": "port" },
                { "data": "protocol" },
                { "data": "service" },
                { "data": "service_info" }
            ]
  });
});
