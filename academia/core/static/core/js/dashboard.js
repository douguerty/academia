$(document).ready(function() {
    $("#btn-loading").hide();
    var usuario = $("#id_usuario").val();
    $.ajax({
        url: '.',
        type: 'POST',
        dataType: 'json',
        data: {
            user: usuario
        }, success: function(data) {
            let consumido = (parseFloat(data[0].consumo_agua)/parseFloat(data[0].agua))*100;
            let a_consumir = 100-consumido;
            let cor_consumido = '';

            if(consumido <= 40) {
                cor_consumido = '#a33554';
            } else if (consumido > 40 && consumido <= 65) {
                cor_consumido = '#c16d30';
            } else if (consumido > 65) {
                cor_consumido = '#58d89a';
            }
          
            zingchart.THEME="classic";
          
            //mychart
            var myConfig = {
                "globals": {
                    "font-family":"Lato",
                    "font-weight":"100"
                },
                "graphset":[
                    {
                        "type":"ring",
                        "background-color":"#fff",
                        "tooltip":{
                            "visible":0
                        },
                        "plotarea":{
                            "margin":"0% 0% 0% 0%"
                        },
                        "plot":{
                            "slice":175,
                            "ref-angle":270,
                            "detach":false,
                            "hover-state":{
                                "visible":false
                            },
                            "value-box":{
                                "visible":true,
                                "type":"first",
                                "connected":false,
                                "placement":"center",
                                "text":"<span style='font-size:60px;'>"+data[0].consumo_agua+" ml</span><br>consumido hoje<br>"+consumido.toFixed(2)+" %",
                                "rules":[
                                    {
                                    "rule":"%v > 50",
                                    "visible":false
                                    }
                                ],
                                "font-color":"#000",
                                "font-size":"40px"
                            },
                            "animation":{
                                "delay":0,
                                "effect":2,
                                "speed":"600",
                                "method":"0",
                                "sequence":"1"
                            }
                        },
                        "series":[
                            {
                            "values":[consumido],
                            "background-color":cor_consumido,
                            "border-color":"#282E3D",
                            "border-width":"1px",
                            "shadow":0
                            },
                            {
                            "values":[a_consumir],
                            "background-color":"#ced5e0",
                            "border-color":"#282E3D",
                            "border-width":"1px",
                            "shadow":0
                            }
                        ]
                    }
                ]
            };
    
            zingchart.render({ 
                id : 'myChart', 
                data : myConfig, 
                hideprogresslogo: true
            });
    
            //mychart2
            var myConfig2 = {
                "type":"hbar",
                "font-family":"Arial",
                "backgroundColor":"#fff",
                "title":{
                    "text":"Relação do seu estado emocional",
                    "font-family":"Arial",
                    "background-color":"none",
                    "font-color":"#000",
                    "font-size":"18px"
                },
                "labels":[
                    {
                        "text":"DIAS",
                        "font-size":"12px",
                        "font-color":"#9d9d9d",
                        "x":"11.5%",
                        "y":"10%"
                    },
                    {
                        "text":"% DE FELICIDADE",
                        "font-size":"12px",
                        "font-color":"#9d9d9d",
                        "x":"20%",
                        "y":"10%"
                    },
                    {
                        "x":"4%",
                        "y":"10%"
                    }
                ],
                "arrows":[
                    {
                        "backgroundColor":"#CCCCCC",
                        "direction":"bottom",
                        "borderWidth": 0,
                        "to":{
                            "x": "6%",
                            "y": "27%"
                        },
                        "from":{
                            "x": "6%",
                            "y": "79%"
                        }
                    }
                ],
                "shapes":[
                    {
                        "type":"circle",
                        "x": 45,
                        "y": 99,
                        "backgroundColor": "white",
                        "borderColor":"#6FA6DF",
                        "borderWidth":3,
                        "size": 14
                    },
                    {
                        "type":"circle",
                        "x": 40,
                        "y": 95,
                        "backgroundColor": "#6FA6DF",
                        "size": 2
                    },
                    {
                        "type":"circle",
                        "x": 50,
                        "y": 95,
                        "backgroundColor": "#6FA6DF",
                        "size": 2
                    },
                    {
                        "type":"pie",
                        "background-color":"#5297b6",
                        "size":8,
                        "x":45,
                        "y":100,
                        "angle-start":0,
                        "angle-end":180,
                    },
                    {
                        "type":"pie",
                        "background-color":"#fff",
                        "size":6,
                        "x":45,
                        "y":100,
                        "angle-start":0,
                        "angle-end":180,
                    },
                    {
                        "type":"circle",
                        "x": 45,
                        "y": 433,
                        "backgroundColor": "white",
                        "borderColor":"#FA8452",
                        "borderWidth":3,
                        "size": 14
                    },
                    {
                        "type":"circle",
                        "x": 40,
                        "y": 429,
                        "backgroundColor": "#FA8452",
                        "size": 2
                    },
                    {
                        "type":"circle",
                        "x": 50,
                        "y": 429,
                        "backgroundColor": "#FA8452",
                        "size": 2
                    },
                    {
                        "type":"pie",
                        "background-color":"#FA8452",
                        "size":8,
                        "x":45,
                        "y":439,
                        "angle-start":170,
                        "angle-end":10,
                    },
                    {
                        "type":"pie",
                        "background-color":"#fff",
                        "size":5,
                        "x":45,
                        "y":440,
                        "angle-start":170,
                        "angle-end":10,
                    }
                ],
                "plot":{
                    "bars-overlap":"100%",
                    "borderRadius":8,
                    "hover-state":{
                        "visible":false
                    },
                    "animation": {
                        "delay": 300,
                        "effect": 3,
                        "speed": "500",
                        "method": "0",
                        "sequence": "3"
                    }
                },
                "plotarea":{
                    "margin":"60px 20px 20px 140px"
                },
                "scale-x":{
                    "line-color":"none",
                    "values":["120+","90-120","60-90","30-60","0-30"],
                    "tick":{
                        "visible":false
                    },
                    "guide":{
                        "visible":false
                    },
                    "item":{
                        "font-size":"14px",
                        "padding-right":"20px",
                        "auto-align":true,
                        "rules":[
                            {
                                "rule":"%i==0",
                                "font-color":"#FA8452"
                            },
                            {
                                "rule":"%i==1",
                                "font-color":"#FCAE48"
                            },
                            {
                                "rule":"%i==2",
                                "font-color":"#FCCC65"
                            },
                            {
                                "rule":"%i==3",
                                "font-color":"#A0BE4A"
                            },
                            {
                                "rule":"%i==4",
                                "font-color":"#6FA6DF"
                            }
                        ]
                    }
                },
                "scale-y":{
                    "visible":false,
                    "guide":{
                        "visible":false
                    }
                },
                "series":[
                    {
                        "values":[100,100,100,100,100],
                        "bar-width":"40px",
                        "background-color":"#f2f2f2",
                        "border-color": "#e8e3e3",
                        "border-width":2,
                        "fill-angle":90,
                        "tooltip":{
                            "visible":false
                        }
                    },
                    {
                        "values":[data[1].bom_up_120,data[1].bom_120,data[1].bom_90,data[1].bom_60,data[1].bom_30],
                        "bar-width":"32px",
                        "max-trackers":0,
                        "value-box":{
                            "placement":"top-out",
                            "text":"%v",
                            "decimals":0,
                            "font-color":"#A4A4A4",
                            "font-size":"14px",
                            "alpha":0.6
                        },
                        "rules":[
                            {
                                "rule":"%i==0",
                                "background-color":"#FA8452"
                            },
                            {
                                "rule":"%i==1",
                                "background-color":"#FCAE48"
                            },
                            {
                                "rule":"%i==2",
                                "background-color":"#FCCC65"
                            },
                            {
                                "rule":"%i==3",
                                "background-color":"#A0BE4A"
                            },
                            {
                                "rule":"%i==4",
                                "background-color":"#6FA6DF"
                            }
                        ]
                    }
                ]
            };

            zingchart.render({ 
                id : 'myChart2', 
                data : myConfig2,
                width: '90%'
            });
        }
    });
});

$("#troca-data").on({
    click: function() {
        let data_a = $("#data-a").val();
        let data_b = $("#data-b").val();

        $("#data-a").val(data_b);
        $("#data-b").val(data_a);
    }
});

$("#btn-chart").on({
    click: function() {
        var usuario = $("#id_usuario").val();
        var data_de = $("#data-a").val();
        var data_ate = $("#data-b").val();
        $.ajax({
            url: '.',
            type: 'POST',
            dataType: 'json',
            data: {
                user: usuario,
                data_de: data_de,
                data_ate: data_ate,
                chart: 1
            },
        })
        .done(function() {
            console.log("success");
        })
        .fail(function() {
            console.log("error");
        })
        .always(function() {
            console.log("complete");
        }); 
    }
});