$("#salvar").on({
    click: function() {
        console.log("Clicou");
        var nome = $("#nome").val();
        var sobrenome = $("#sobrenome").val();
        var genero = $("#genero").val();
        var nascimento = $("#nascimento").val();
        var idade = $("#idade").val();
        var altura = $("#altura").val();
        var peso = $("#peso").val();
        
        if(nome == "") {
            alert("Nome é nescessario");
        }
        else if(sobrenome == "") {
            alert("Sobrenome é nescessario");
        }
        else if(altura == "") {
            alert("Altura é nescessario");
        }
        else if(peso == "") {
            alert("Nome é nescessario");
        } else {
            $.ajax({
                url: '.',
                type: 'POST',
                dataType: 'json',
                data: {
                    nome: nome,
                    sobrenome: sobrenome,
                    genero: genero,
                    nascimento: nascimento,
                    idade: idade,
                    altura: altura,
                    peso: peso
                }, success: function(data) {
                    $("#modal-title").append(
                        "Sucesso"
                    );
                    $("#modal-body").append(
                        "<p align='center'>Alterações realizadas com sucesso!</p>"
                    );
                    $("#modalInfo").modal();
                }, error: function(data) {
                    $("#modal-title").append(
                        "Erro"
                    );
                    $("#modal-body").append(
                        "<p align='center'>Erro ao salvar alterações!</p>"
                    );
                    $("#modalInfo").modal();
                }
            });
        }
    }
});

$('#modalInfo').on('hidden.bs.modal', function () {
    $("#modal-title").empty();
    $("#modal-body").empty();
});