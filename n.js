// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
      processing: true,
    serverSide: true,
      "lengthChange": false,
    ajax: {
        url: '/data_source',
        type: 'POST'
    },
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
