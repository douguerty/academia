var controle = 0;
$(".humor").on({
    click: function() {
        if(controle == 0 || controle == $(this).attr('value')) {
            if($(this).hasClass('text-warning')) {
                $(this).removeClass('text-warning');
                controle = 0;
            } else {
                $(this).addClass('text-warning');
                controle = $(this).attr('value');
            }
        } else {
            $("#modal-title").append(
                'Atenção'
            );
            $("#modal-body").append(
                '<p>Você só pode escolher um estado emocional por vez!</p>'
            );
            $("#modalHumor").modal();
        }
    }
});

$("#salvar").on({
    click: function() {
        if (controle == 0) {
            $("#modal-title").append(
                'Atenção'
            );
            $("#modal-body").append(
                '<p>Para salvar selecione um estado emocional!</p>'
            );
            $("#modalHumor").modal();
        } else {
            let usuario = $("#id_usuario").val();
            $.ajax({
                url: '.',
                type: 'POST',
                dataType: 'json',
                data: {
                    usuario: usuario,
                    humor: controle
                }, success: function(data) {
                    if(data.error) {
                        $("#modal-title").append(
                            'Erro'
                        );
                        $("#modal-body").append(
                            '<p>Erro ao salvar estado emociona!<br>Tente novamente, se o erro persistir entre em contato com o suporte técnico.</p>'
                        );
                        $("#modalHumor").modal();
                    } else {
                        $("#modal-title").append(
                            'Sucesso'
                        );
                        $("#modal-body").append(
                            '<p>Estado emocional registrado com sucesso!</p>'
                        );
                        $("#modalHumor").modal();
                    }
                }, error: function(data) {
                    $("#modal-title").append(
                        'Erro'
                    );
                    $("#modal-body").append(
                        '<p>Erro ao salvar estado emociona!<br>Tente novamente, se o erro persistir entre em contato com o suporte técnico.</p>'
                    );
                    $("#modalHumor").modal();
                }
            });
        }
    }
});

//Limpa modal
$("#modalHumor").on("hidden.bs.modal", function () {
    $("#modal-title").empty();
    $("#modal-body").empty();
});