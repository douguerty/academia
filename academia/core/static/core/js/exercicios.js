$(".btn-delete").on({
    click: function() {
        var id = $(this).attr('name');
        $("#id-exercicio").val(id);
        $("#btn-nao").append(
            "<i class='fa fa-times' aria-hidden='true'></i> Não"
        );
        $("#btn-sim").show();
        $("#modal-title").append(
            'Atenção'
        );
        $("#modal-body").append(
            'Tem certeza que deseja excluir esse exercicio?'
        );
        $("#modalDelete").modal();
    }
});

$("#btn-sim").on({
    click: function() {
        var id = $("#id-exercicio").val();
        $.ajax({
            url: '/exercicio/delete',
            type: 'POST',
            dataType: 'json',
            data: {
                id: id
            },
            success: function(data) {
                $("#modal-title").empty();
                $("#modal-body").empty();
                $("#btn-nao").empty();
                $("#btn-sim").hide();
                $("#btn-nao").append(
                    "<i class='fa fa-times' aria-hidden='true'></i>"
                );
                $("#modal-title").append(
                    'Sucesso'
                );
                $("#modal-body").append(
                    'Exercicio excluído com sucesso'
                );
            },
            error: function(data) {
                $("#modal-title").empty();
                $("#modal-body").empty();
                $("#btn-nao").empty();
                $("#btn-sim").hide();
                $("#btn-nao").append(
                    "<i class='fa fa-times' aria-hidden='true'></i>"
                );
                $("#modal-title").append(
                    'Erro'
                );
                $("#modal-body").append(
                    'Erro ao excluir exercicio'
                );
            }
        });
    }
});

$('#modalDelete').on('hidden.bs.modal', function () {
    $("#modal-title").empty();
    $("#modal-body").empty();
    $("#btn-nao").empty();
    location.reload();
});