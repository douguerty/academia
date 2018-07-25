$(document).ready(function() {
    var usuario = $("#id_usuario").val();
    $.ajax({
        url: '.',
        type: 'POST',
        dataType: 'json',
        data: {
            user: usuario
        }
    });
});

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
                "background-color":"#282E3D",
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
                        "text":"<span style='font-size:60px;'>402</span><br>Total Nodes",
                        "rules":[
                            {
                                "rule":"%v > 50",
                                "visible":false
                            }
                        ],
                        "font-color":"#fff",
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
                        "values":[25],
                        "background-color":"#FDFD47",
                        "border-color":"#282E3D",
                        "border-width":"2px",
                        "shadow":0
                    },
                    {
                        "values":[75],
                        "background-color":"#35D884",
                        "border-color":"#282E3D",
                        "border-width":"2px",
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
    "title":{
        "text":"Customer Survey Response",
        "font-family":"Arial",
        "background-color":"none",
        "font-color":"#A4A4A4",
        "font-size":"18px"
    },
    "labels":[
        {
            "text":"DAYS",
            "font-size":"12px",
            "font-color":"#9d9d9d",
            "x":"11.5%",
            "y":"10%"
        },
        {
            "text":"CUSTOMERS",
            "font-size":"12px",
            "font-color":"#9d9d9d",
            "x":"20%",
            "y":"10%"
        },
        {
            "text":"GOAL",
            "font-size":"12px",
            "font-color":"#9d9d9d",
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
            "values":[42,56,77,44,81],
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
width: 725
});


//mychart3
var myConfig3 = {
    type: 'line',
    backgroundColor:'#2C2C39',
    title:{
      text:'Time Series Data with null values',
      adjustLayout: true,
      fontColor:"#E3E3E5",
      marginTop: 7
    },
    legend:{
      align: 'center',
      verticalAlign: 'top',
      backgroundColor:'none',
      borderWidth: 0,
      item:{
        fontColor:'#E3E3E5',
        cursor: 'hand'
      },
      marker:{
        type:'circle',
        borderWidth: 0,
        cursor: 'hand'
      }
    },
    plotarea:{
      margin:'dynamic 70'
    },
    plot:{
      aspect: 'spline',
      lineWidth: 2,
      marker:{
        borderWidth: 0,
        size: 5
      }
    },
    scaleX:{
      lineColor: '#E3E3E5',
      zooming: true,
      zoomTo:[0,15],
      minValue: 1459468800000,
      step: 'day',
      item:{
        fontColor:'#E3E3E5'
      },
      transform:{
        type: 'date',
        all: '%D %M %d<br>%h:%i:%s'
      }
    },
    scaleY:{
      minorTicks: 1,
      lineColor: '#E3E3E5',
      tick:{
        lineColor: '#E3E3E5'
      },
      minorTick:{
        lineColor: '#E3E3E5'
      },
      minorGuide:{
        visible: true,
        lineWidth: 1,
        lineColor: '#E3E3E5',
        alpha: 0.7,
        lineStyle: 'dashed'
      },
      guide:{
        lineStyle: 'dashed'
      },
      item:{
        fontColor:'#E3E3E5'
      }
    },
    tooltip:{
      borderWidth: 0,
      borderRadius: 3
    },
    preview:{
      adjustLayout: true,
      borderColor:'#E3E3E5',
      mask:{
        backgroundColor:'#E3E3E5'
      }
    },
    crosshairX:{
      plotLabel:{
        multiple: true,
        borderRadius: 3
      },
      scaleLabel:{
        backgroundColor:'#53535e',
        borderRadius: 3
      },
      marker:{
        size: 7,
        alpha: 0.5
      }
    },
    crosshairY:{
      lineColor:'#E3E3E5',
      type:'multiple',
      scaleLabel:{
        decimals: 2,
        borderRadius: 3,
        offsetX: -5,
        fontColor:"#2C2C39",
        bold: true
      }
    },
    shapes:[
             {
               type:'rectangle',
               id:'view_all',
               height:'20px',
               width:'75px',
               borderColor:'#E3E3E5',
               borderWidth:1,
               borderRadius: 3,
               x:'85%',
               y:'11%',
               backgroundColor:'#53535e',
               cursor:'hand',
               label:{
                 text:'View All',
                 fontColor:'#E3E3E5',
                 fontSize:12,
                 bold:true
               }
             }
           ],
   series: [
       {
           values: [218.92,212.85,241.95,200.76,203.87,245.26,249.9,240.05,241.8,251.4,230.06,null,null,203.04,229.05,232.37,190.89,236.63,249.18,188.98,194.06,234.61,241.91,196.4,191.87,213.5,194.83,228.48,235.66,235.04,195.74,243.04,null,197.51,232.64,238.99,227.8,235.81,221.7,193.46,252.64,205.35,248.52,218.32,188.55],
           lineColor:'#E34247',
           marker:{
             backgroundColor:'#E34247'
           }
       },
       {
         values:[165.57,170.47,197.17,164.64,132.73,176.89,139.41,158.71,177.85,138.87,135.74,167.06,156.42,182,169.73,151.08,165.58,146.29,124.5,181.71,143.96,null,null,null,146,172.6,149.81,161.09,175.88,149.39,184.1,123.85,186.82,139.72,138.61,170.28,164.06,184.33,null,null,131.85,133.32,134.49,143.79,125.23],
         lineColor: '#FEB32E',
         marker:{
           backgroundColor:'#FEB32E'
         }
       },
       {
         values: [70.19,96.56,75.04,51.58,82.8,68.14,89.61,null,45.33,98.59,92.9,66.94,null,74.08,57.25,79.68,89.66,64.56,96.59,79.96,98.08,42.93,91.93,56.23,82.66,null,85.76,74.98,51,66.99,63.02,63.8,44.33,77.56,95.28,60.93,59.6,80.58,68.51,67.63,69.76,40.54,78.42,90.4,82.3],
         lineColor:'#31A59A',
         marker:{
           backgroundColor:'#31A59A'
         }
       }
   ]
};

zingchart.bind('myChart', 'shape_click', function(p){
 if(p.shapeid == "view_all"){
   zingchart.exec(p.id,'viewall');
 }
})

zingchart.render({ 
   id: 'myChart3', 
   data: myConfig3, 
});


//mychart4
var myConfig4 = {
    "graphset":[
      
      {
        "type":"pie",
        "backgroundColor": "#222",
        "plotarea":{
          "margin":"40"
        },
        "scale":{
          "sizeFactor":1
        },
        "plot":{
          "valueBox":{
            "visible":false
          },
          "refAngle":270,
          "angleStart":270,
          "detach":false,
          "slice":"100%",
          "totals":[100],
          "animation":{
            "speed":1000,
            "effect":2,
            "method":0
          },
          "hoverState":{
            "visible":false
          }
        },
        "series":[
          {
            "size":"100%",
            "values":[84],
            "backgroundColor":"#F61F64",
            "borderWidth":46,
            "borderColor":"#F61F64",
            "text":"Move",
            "tooltip":{
                "x":365,    
                "y":243,
                "width":120,
                "fontSize":19,
                "padding":30,
                "anchor":"c",
                "fontFamily":"Lucida Sans Unicode",
                "text":"<span style='color:%color'>%plot-text</span><br><span style='font-size:31px;font-weight:bold;color:%color;'>%node-percent-value%</span>", 
                "align":"left",
                "borderWidth":0,
                "backgroundColor":"none",
              }
          },
          {
            "size":"75%",
            "values":[76],
            "backgroundColor":"#6fe71c",
            "borderWidth":46,
            "borderColor":"#6fe71c",
            "text":"Exercise",
            "tooltip":{
                "x":365,    
                "y":243,
                "width":120,
                "fontSize":19,
                "padding":30,
                "anchor":"c",
                "fontFamily":"Lucida Sans Unicode",
                "text":"<span style='color:%color'>%plot-text</span><br><span style='font-size:31px;font-weight:bold;color:%color;'>%node-percent-value%</span>",
                "align":"left",
                "borderWidth":0,
                "backgroundColor":"none",
              }
          },
          {
            "size":"50%",
            "values":[55],
            "backgroundColor":"#19ecd5",
            "borderWidth":46,
            "borderColor":"#19ecd5",
            "text":"Stand",
            "tooltip":{
                "x":365,    
                "y":243,
                "width":120,
                "fontSize":19,
                "padding":30,
                "anchor":"c",
                "fontFamily":"Lucida Sans Unicode",
                "text":"<span style='color:%color'>%plot-text</span><br><span style='font-size:31px;font-weight:bold;color:%color;'>%node-percent-value%</span>",
                "align":"left",
                "borderWidth":0,
                "backgroundColor":"none",
        },
          }
        ],
        "shapes":[
          {
            "type":"pie",
            "flat":true,
            "x":362,
            "y":250,
            "backgroundColor":"#F61F64",
            "alpha":0.25,
            "size":234,
            "slice":187,
            "placement":"bottom"
          },
          {
            "type":"pie", //green done
            "flat":true,
            "x":362,
            "y":250,
            "backgroundColor":"#78ff1b",
            "alpha":0.25,
            "size":182,
            "slice":134,
            "placement":"bottom"
          },
          {
            "type":"pie", //blue done
            "flat":true,
            "x":362,
            "y":250,
            "backgroundColor":"#0efbe1",
            "alpha":0.25,
            "size":129,
            "slice":82,
            "placement":"bottom"
          },
          {
            "type":"line",
            "lineWidth":3,
            "lineCap":"round",
            "lineColor":"#000",
            "points":[
              [0,0],
              [22,0],
              null,
              [10,-10],
              [22,0],
              [10,10]
            ],
            "offsetX":350,
            "offsetY":42
          },
          {
            "type":"line",
            "lineWidth":3,
            "lineCap":"round",
            "lineColor":"#000",
            "points":[
              [0,0],
              [22,0],
              null,
              [10,-10],
              [22,0],
              [10,10],
              null,
              [20,-10],
              [32,0],
              [20,10]
            ],
            "offsetX":350,
            "offsetY":95
          },
          {
            "type":"line",
            "lineWidth":3,
            "lineCap":"round",
            "lineColor":"#000",
            "points":[
              [0,0],
              [0,22],
              null,
              [-10,12],
              [0,0],
              [10,12]
            ],
            "offsetX":360,
            "offsetY":135
          }
        ]
      }
    ]
  };
   
  zingchart.render({ 
      id : 'myChart4', 
      data : myConfig4, 
      height: 500, 
      width: 725 
  });