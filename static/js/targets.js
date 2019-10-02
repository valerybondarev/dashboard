$(document).ready(function () {

    // Поиск по таблице
    // Ищет по всем полям таблицы (даже цифры)
    $("#SearchTarget").keyup(function() {
        _this = this;
        $.each($(".table-targets tbody tr"), function () {
            if ($(this).text().toLowerCase().indexOf($(_this).val().toLowerCase()) === -1) {
                $(this).hide();
            } else {
                $(this).show();
            }
        });
    });

    // При нажатии на сканирование выбранных
    $('span[data-original-title="Scan Targets"]').click(function () {
        // Обходим все отмеченные хосты
        $('.cbx:checked').each(function () {
            // Запускаем сканирование на всех выбранных
            $(this).parent('td').parent('tr').children('td:last-child').children('span').children('a').children('button').removeClass('btn-info');
            $(this).parent('td').parent('tr').children('td:last-child').children('span').children('a').children('button').addClass('btn-danger');
            $(this).parent('td').parent('tr').children('td:last-child').children('span').children('a').children('button').children('i').removeClass('fa-play');
            $(this).parent('td').parent('tr').children('td:last-child').children('span').children('a').children('button').children('i').addClass('fa-stop');
            $(this).parent('td').parent('tr').children('td:last-child').children('span').children('a').children('span').html('Scanning ...');
            $.ajax({
                url: '/scan_target',
                type: 'post',
                data: {'target_id': $(this).data('id')},
                success: function (resp) {
                    console.log(resp);
                }
            });
        });
    });

    // При выделении всех хостов
    $('span[data-original-title="Select All"]').click(function () {
        $('.cbx').prop("checked",true);
        cnt_cbx = cnt_cbx = $('.cbx').length;
        // Разблокируем кнопку
        $('span[data-original-title="Scan Targets"] > a, span[data-original-title="Delete"] > a').removeClass('disabled');
    });

    var cnt_cbx = 0;
    // Считаем количество отмеченных и блокируем/разблокируем кнопку
    $(function () {
        cnt_cbx = $('.cbx:checked').length;
        $('.cbx').bind('click' , function(e, a) {
         if (this.checked) {
              cnt_cbx += a ? -1 : 1;
         } else {
              cnt_cbx += a ? 1 : -1;
         }
         if(cnt_cbx > 0) {
             $('span[data-original-title="Scan Targets"] > a, span[data-original-title="Delete"] > a').removeClass('disabled');
         } else {
             $('span[data-original-title="Scan Targets"] > a, span[data-original-title="Delete"] > a').addClass('disabled');
         }
    });
    });
    var deleted_target_id = 0;
    // Если нажато удаление выбранных
    $('span[data-original-title="Delete"]').click(function () {
        $('.cbx:checked').each(function () {
            $.ajax({
                url: '/delete_target',
                type: 'post',
                data: {'target_id': $(this).data('id')},
                success: function (resp) {
                    console.log(resp);
                    $('input[data-id="' + resp + '"]').parents('td').parent('tr').remove();
                }
            });

        });
    });

    // При нажатии на сканирование напротив хоста
    $('.scan_target').click(function () {
        $(this).children('a').children('button').removeClass('btn-info');
        $(this).children('a').children('button').addClass('btn-danger');
        $(this).children('a').children('button').children('i').removeClass('fa-play');
        $(this).children('a').children('button').children('i').addClass('fa-stop');
        $(this).children('a').children('span').html('Scanning ...');
        $.ajax({
                url: '/scan_target',
                type: 'post',
                data: {'target_id': $(this).data('id')},
                success: function (resp) {
                    console.log(resp);
                }
            });
    });
    $('.show_modal').click(function () {
        $('#target-new-modal').modal('show');
        $('#target-new-modal').css('display', 'block');
    })
});