$(".btn-delete").on({
    click: function() {
        var id = $(this).attr('name');
        $("#id-treinamento").val(id);
        $("#btn-nao").append(
            "<i class='fa fa-times' aria-hidden='true'></i> Não"
        );
        $("#btn-sim").show();
        $("#modal-title").append(
            'Atenção'
        );
        $("#modal-body").append(
            'Tem certeza que deseja excluir esse treinamento?'
        );
        $("#modalDelete").modal();
    }
});

$("#btn-sim").on({
    click: function() {
        var id = $("#id-treinamento").val();
        $.ajax({
            url: '/treinamento/delete',
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
                    'Treinamento excluído com sucesso'
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