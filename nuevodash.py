import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import pickle
import plotly.tools as tls
import plotly.graph_objects as go


# Initialize the application

app = dash.Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.MORPH,
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
    ],
    suppress_callback_exceptions=True
)
server=app.server

app.layout = dbc.Container(
    [
        dcc.Location(id="url"),
        dbc.Row(
            [
                # Sidebar
                dbc.Col(
                    [
                        html.H2("Proyecto ML", className="display-5", style={'textAlign': 'center'}),
                        html.Hr(),
                        dbc.Nav(
                            [
                                dbc.NavLink("Inicio", href="/", id="link-inicio", active="exact"),
                                dbc.NavLink("Microeconómicos Generales", href="/micro-generales", id="link-micro-generales", active="exact"),
                                dbc.NavLink("Microeconómicos Específicos", href="/micro-especificos", id="link-micro-especificos", active="exact"),
                                dbc.NavLink("Mapa", href="/mapa", id="link-macro-especificos", active="exact"),
                                dbc.NavLink("Modelo", href="/modelo", id="link-modelo", active="exact"),
                                dbc.NavLink("Supuestos", href="/supuestos", id="link-supuestos", active="exact"),
                            ],
                            vertical=True,
                            pills=True,
                            style={'marginTop': '100px'}
                        ),
                        html.Hr(style={'marginTop': '120px'}),
                        html.Div(
                            [
                                html.P("Curso: Machine Learning - Visualización de datos", className="text-secondary-emphasis text-center"),
                                html.P("Creadores: Kelly y Henry", className="text-secondary-emphasis text-center")
                            ],
                            style={'text-align': 'center', 'width': '100%'}
                        )
                    ],
                    width=2, style={'backgroundColor': '#f8f9fa', 'height': '100%', 'paddingTop': '25px'}
                ),
                
                # Main content
                dbc.Col(
                    html.Div(id="page-content", style={'padding': '20px'}),
                    width=10
                ),
            ]
        )
    ],
    fluid=True
)

# Callback to update content based on selected tab
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)

def render_page_content(pathname):
    if pathname == "/":
        with open("df_head.pkl", "rb") as f:
            df_head = pickle.load(f)
        return html.Div([
           html.H1("Desempeño Financiero de PYMEs Colombianas", style={"textAlign": "center", "marginBottom": "20px"}),

    # Filas principales
        dbc.Row([
            # Parte izquierda con dos cuadros grandes
            dbc.Col([
                html.Div([
                    html.Div(
                    "Las PYMEs son fundamentales para la economía colombiana, pero enfrentan desafíos en el acceso a financiamiento e inversión debido a la falta de herramientas precisas para evaluar su desempeño financiero. Los benchmarks sectoriales tradicionales, basados en promedios generales, no reflejan las particularidades de cada empresa, lo que puede sesgar decisiones financieras. Dado que la gestión financiera de estas empresas involucra múltiples variables clave como liquidez, rentabilidad y endeudamiento, el uso de modelos de clasificación basados en Machine Learning se presenta como una solución innovadora para identificar patrones complejos, mejorar la evaluación del desempeño financiero y optimizar la toma de decisiones estratégicas.",
                    style={
                        'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '250px'
                    }
                    ),
                    html.Div(
                    [
                        html.H4("Objetivos Específicos", style={"marginBottom": "15px"}),
                        html.Ul([
                            html.Li("Recolección y preprocesamiento de datos: Compilar y limpiar datos financieros de las PYMEs y variables macroeconómicas relevantes."),
                            html.Li("Construcción de variables de desempeño financiero: Calcular indicadores clave como ratios de liquidez, rentabilidad y endeudamiento."),
                            html.Li("Exploración de datos: Analizar patrones y características relevantes para definir las variables respuesta."),
                            html.Li("Visualización de datos: Diseñar visualizaciones que faciliten el análisis y comparación del desempeño financiero entre sectores y regiones."),
                            html.Li("Desarrollo y comparación de modelos: Implementar y evaluar algoritmos de Machine Learning considerando datos micro y macroeconómicos.")
                        ])
                    ],
                    style={
                        'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '330px', 'marginTop': '20px'
                    }
                )
            ])
            ], width=7),
            dbc.Col([
                dbc.Row([
                    dbc.Col([
                        html.Div(
                        [
                            html.H4("Variables Categoricas: 8", style={"marginBottom": "15px"}),
                        
                        ],
                        style={
                            'border': '1px solid #dee2e6', 'padding': '20px', 'borderRadius': '5px',
                            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '110px', 'marginTop': '20px','backgroundColor': 'white'
                        }
                    )
                    ], width=6),
                    dbc.Col([
                        html.Div(
                        [
                            html.H4("Variables Númericas: 21", style={"marginBottom": "15px"}),
                            
                        ],
                        style={
                            'border': '1px solid #dee2e6', 'padding': '20px', 'borderRadius': '5px',
                            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '110px', 'marginTop': '20px','backgroundColor': 'white'
                        }
                    )
                    ], width=6)
                ], style={'marginBottom': '20px'}),

                html.Div(
                    html.Img(src="/assets/lol3.png", style={"width": "100%", "borderRadius": "5px"}),
                    style={'height': '400px', 'border': '1px solid #dee2e6', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'}
                )
            ], width=5)
        ], style={'marginBottom': '20px'}),
            html.Div([
                    html.H3("Vista previa de los datos", style={"textAlign": "center", "marginBottom": "20px"}),
                    html.Div(
                        dbc.Table.from_dataframe(df_head, striped=True, bordered=True, hover=True, responsive=True),
                        style={
                            "maxHeight": "300px",  # Altura máxima del contenedor
                            "overflowY": "auto",  # Habilitar scroll vertical
                            "overflowX": "auto",  # Habilitar scroll horizontal si es necesario
                            "border": "1px solid #dee2e6",  # Borde alrededor del contenedor
                            "padding": "10px",  # Espaciado interno
                            "borderRadius": "5px",  # Bordes redondeados
                            "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)"
                        }
                    )
                ])
        ])

    # Pestaña de Microeconómicos Generales: Código modificado
    elif pathname == "/micro-generales":
        variables = [
            'Razón corriente', 'Rotación inventario producto terminado',
            'Rotación cartera', 'Rotación proveedores', 'Productividad KTNO', 'ROA',
            'ROE', 'Nivel de endeudamiento', 'Generación Efectivo',
            'SD', 'Generación FLC'
        ]  # Variables disponibles para los histogramas

        return html.Div([
            html.H3("Microeconómicos Generales", style={"textAlign": "center", "marginBottom": "20px"}),

            # Dropdown para seleccionar la variable
            html.Div([
                html.Label("Selecciona una variable para visualizar:"),
                dcc.Dropdown(
                    id='dropdown-variable',
                    options=[{'label': var, 'value': var} for var in variables],
                    value=variables[0],  # Valor inicial
                    style={'width': '300px'}  
                )
            ], style={'marginBottom': '20px'}),

            # Contenedor con los cuadros y el histograma
            dbc.Row([
                # Columna para el histograma
                dbc.Col([
                    html.Div(
                        [
                            dcc.Graph(id='histograma-container', style={"height": "300px"})
                        ],
                        style={
                            'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '330px','backgroundColor': 'white'
                        }
                    )
                ], width=6),
                # Segunda caja grande
               dbc.Col([
                    html.Div(
                        [
                            dcc.Graph(id="cuadro-2-graph")  # Contenedor para el gráfico de violin
                        ],
                        style={
                            'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '330px','backgroundColor': 'white'
                        }
                    )
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div(
                        [
                            dcc.Graph(id="cuadro-3-graph") 
                        ],
                        style={
                            'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '470px','backgroundColor': 'white'
                        }
                    )
                ], width=6),
                dbc.Col([
                    html.Div(
                        [
                            html.H4("Tabla de Estadísticas", style={'textAlign': 'center'}),
                            html.Div(id="cuadro-4-table")  # Contenedor para la tabla dinámica
                        ],
                        style={
                            'border': '1px solid #dee2e6', 'padding': '20px', 'borderRadius': '5px',
                            'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '470px','backgroundColor': 'white' # Añade scroll si la tabla es grande
                        }
                    )
                ], width=6)
            ], style={'marginTop': '20px'})
        ])

    elif pathname == "/micro-especificos":
        años = [
            '2017','2018', '2019',
            '2020', '2021', '2022', '2023'
        ]
        return html.Div([
                html.H3("Variable Objetivo", style={"textAlign": "center", "marginBottom": "20px"}),

                html.Div([
                    html.Label("Selecciona un año para visualizar:"),
                    dcc.Slider(
                        id='slider-variable',
                        min=0,  # Índice inicial
                        max=len(años) - 1,  # Índice final
                        step=1,
                        marks={i: años[i] for i in range(len(años))},  # Etiquetas para los años
                        value=0,  # Valor inicial (el primer índice, correspondiente a '2017')
                    )
                ], style={'marginBottom': '20px','width': '50%'}),  # Ajusta el padding horizontal
        
                dbc.Row([
                    # Columna para el histograma
                    dbc.Col([
                        html.Div(
                            [
                                dcc.Graph(id="histograma-graph", style={"height": "300px"})
                            ],
                            style={
                                'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                                'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '330px','backgroundColor': 'white'
                            }
                        )
                    ], width=6),
                    dbc.Col([
                            html.Div(
                                [
                                    dcc.Graph(id="barras-graph",style={"height": "316px"})   # Contenedor para el gráfico de violin
                                ],
                                style={
                                    'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                                    'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '330px','backgroundColor': 'white'
                                }
                            )
                        ], width=6)
                ]),
                dbc.Row([
                    dbc.Col([
                        html.Div(
                            [
                                
                                dcc.Graph(id="matriz-graph",style={"height": "300px"})
                            ],
                            style={
                                'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                                'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '470px','backgroundColor': 'white'
                            }
                        )
                    ], width=7),
                dbc.Col([
                        html.Div(
                            [
                    
                                dcc.Graph(id="violin-graph")   # Contenedor para la tabla dinámica
                            ],
                            style={
                                'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                                'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'height': '470px','backgroundColor': 'white' # Añade scroll si la tabla es grande
                            }
                        )
                    ], width=5)
                ], style={'marginTop': '20px'})
            ])     

    elif pathname == "/mapa":
        with open("promindi.pkl", "rb") as f:
            grafica_estatica = pickle.load(f)
        anios = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']  # Años disponibles
        return html.Div([
            html.H3("Mapa Interactivo", style={"textAlign": "center", "marginBottom": "20px"}),
            html.Div([
                        html.Label("Selecciona un año para visualizar:", style={"fontWeight": "bold"}),
                        dcc.Slider(
                            id="slider-mapa",
                            min=0,  # Índice inicial
                            max=len(anios) - 1,  # Índice final
                            step=1,
                            marks={i: anios[i] for i in range(len(anios))},  # Etiquetas para los años
                            value=0,  # Valor inicial
                        )
                    ], style={"marginBottom": "20px", "padding": "10px"}),

            dbc.Row([
                dbc.Col([
                    html.Div([
                        dcc.Graph(figure=grafica_estatica, style={"height": "300px"})  # Contenedor dinámico
                    ], style={
                        'border': '1px solid #dee2e6', 'padding': '20px', 'borderRadius': '5px',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px', 'backgroundColor': 'white'
                    }),
                    html.Div([
                        dcc.Graph(id="grafica-dos-dos", style={"height": "320px"})
                    ], style={
                        'border': '1px solid #dee2e6', 'padding': '20px', 'borderRadius': '5px',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px', 'backgroundColor': 'white'
                    })
                    
                ], width=6),
                # Columna derecha con el mapa
                
                dbc.Col([
                    html.Div(id="mapa-contenedor", style={
                        "border": "1px solid #dee2e6",  'padding': '10px',"borderRadius": "5px",
                        "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
                        "width": "100%", "height": "630px"
                    })
                ], width=6),  # Ancho de la columna derecha
                
            ]),
            html.Div([
                        dcc.Graph(id="grafica-cuadro-uno", style={"height": "450px","width": "900px",'text-align': 'center'})
                        
                    ], style={
                        'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'backgroundColor': 'white'
                    })
    
        ])

    elif pathname == "/modelo":
        anios = [ '2018', '2019', '2020', '2021', '2022', '2023']  # Años disponibles
        metricas = ['<0', '[0, 0.67)', '[0.67, 0.80)', '[0.80, 1)', '[1, ∞)']  # Métricas para el dropdown

        return html.Div([
            html.H3("Modelo XGBoost + LightGBM", style={"textAlign": "center", "marginBottom": "20px"}),

            dbc.Row([
                
                # Cuadros para tablas
                dbc.Col([
                    html.Div([
                    html.Label("Selecciona un año para visualizar:", style={"fontWeight": "bold"}),
                    dcc.Slider(
                        id="slider-modelo",
                        min=0,  # Índice inicial
                        max=len(anios) - 1,  # Índice final
                        step=1,
                        marks={i: anios[i] for i in range(len(anios))},  # Etiquetas para los años
                        value=0,  # Valor inicial
                    )
                    ], style={"marginBottom": "20px", "padding": "10px"}),
                    html.Div([
                        html.Img(id="imagen-cuadro-uno", style={"width": "100%", "height": "auto", "borderRadius": "5px"})
                    ], style={
                        'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px', 'backgroundColor': 'white'
                    }),
                    
                ], width=6),  # Ancho de la columna izquierda

                # Cuadros y dropdown en la columna derecha
                dbc.Col([
                    html.Div([
                        html.H4("Metricas", style={"textAlign": "center"}),
                    ], style={
                        'border': '1px solid #dee2e6', 'padding': '20px', 'borderRadius': '5px',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px', 'backgroundColor': 'white'
                    }),
                    html.Div([
                        html.Img(src="/assets/tablaf.png", style={"width": "100%", "height": "auto", "borderRadius": "5px"})
                    ], style={
                        'border': '1px solid #dee2e6', 'padding': '20px', 'borderRadius': '5px',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px', 'backgroundColor': 'white'
                    }),
                    dcc.Dropdown(
                        id="dropdown-metricas",
                        options=[
                            {"label": "< 0", "value": "<0"},
                            {"label": "[0, 0.67)", "value": "[0, 0.67)"},
                            {"label": "[0.67, 0.80)", "value": "[0.67, 0.80)"},
                            {"label": "[0.80, 1)", "value": "[0.80, 1)"},
                            {"label": "[1, ∞)", "value": "[1, ∞)"}
                        ],
                        value="<0",  # Valor por defecto
                        style={"width": "100%"}
                    )
                    ,
                    html.Div([
                        html.Img(
                            id="imagen-cuadro-dos",
                            style={"width": "100%", "height": "auto", "borderRadius": "5px"}
                        )
                    ], style={
                        'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px', 'backgroundColor': 'white'
                    })
                ], width=6)  # Ancho de la columna derecha
            ]),
            html.Div([
                        html.Img(src="/assets/evo.png", style={"width": "100%", "height": "500px", "borderRadius": "5px"})
                    ], style={
                        'border': '1px solid #dee2e6', 'padding': '20px', 'borderRadius': '5px',
                        'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'marginBottom': '20px', 'backgroundColor': 'white'
                    }),
        ])


    elif pathname == "/supuestos":
        with open("matriz_general.pkl", "rb") as f:
            matrizhene = pickle.load(f)
        anios = ['2017', '2018', '2019', '2020', '2021', '2022', '2023']
        return html.Div([
            html.H3("Evaluación de Supuestos", style={"textAlign": "center", "marginBottom": "20px"}),

            html.Div([
                html.Label("Selecciona un año para visualizar:"),
                dcc.Slider(
                    id='slider-supuestos',
                    min=0,  # Índice inicial
                    max=len(anios) - 1,  # Índice final
                    step=1,
                    marks={i: anios[i] for i in range(len(anios))},  # Etiquetas para los años
                    value=0,  # Valor inicial (el primer índice, correspondiente a '2017')
                )
            ], style={'marginBottom': '20px', 'width': '50%'}),

            dbc.Row([
                # Columna para mostrar la tabla
                dbc.Col([
                    html.Div([
                        html.H4("Resultados de Normalidad", style={"marginBottom": "15px"}),
                        html.Div(id="tabla-supuestos", style={
                            "border": "1px solid #dee2e6", 'padding': '20px',
                            'borderRadius': '5px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
                            "maxHeight": "400px", "overflowY": "auto",
                        })
                    ])
                ], width=6),

                # Columna para mostrar la tabla VIF
                dbc.Col([
                    html.Div([
                        html.H4("Resultados de VIF", style={"marginBottom": "15px"}),
                        html.Div(id="tabla-vif", style={
                            "border": "1px solid #dee2e6", 'padding': '20px',
                            'borderRadius': '5px', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)',
                            "maxHeight": "400px", "overflowY": "auto",
                        })
                    ])
                ], width=6),
            ]),
            html.Div([
            html.Div([
                dcc.Graph(figure=matrizhene, style={"height": "700px", "width": "60%", "margin": "0 auto"})
            ], style={
                'border': '1px solid #dee2e6', 'padding': '10px', 'borderRadius': '5px',
                'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)', 'backgroundColor': 'white',
                'margin': '0 auto', 'textAlign': 'center'
            })
        ])
        ])
    else:
        return html.H3("Página no encontrada - 404")
# Callback para actualizar el histograma
@app.callback(
    [Output('histograma-container', 'figure'),
     Output('cuadro-4-table', 'children'),
     Output('cuadro-3-graph', 'figure'),
     Output('cuadro-2-graph', 'figure')],
    [Input('dropdown-variable', 'value')]
)
def update_content(variable):
    # Actualización del histograma
    try:
        hist_filename = f"histograma_{variable.replace(' ', '_').lower()}.pkl"
        with open(hist_filename, "rb") as f:
            hist_fig = pickle.load(f)
    except FileNotFoundError:
        hist_fig = go.Figure().update_layout(
            title="Histograma no encontrado",
            annotations=[
                dict(
                    text=f"No se encontró el archivo para la variable '{variable}'",
                    x=0.5, y=0.5, showarrow=False, font=dict(size=16))
            ]
        )

    # Actualización de la tabla en Cuadro 4
    try:
        table_filename = f"summary_{variable.replace(' ', '_').lower()}.pkl"
        with open(table_filename, "rb") as f:
            table_data = pickle.load(f)

        cuadro_4_table = dbc.Table.from_dataframe(
            table_data.reset_index(),  # Incluye el índice como columna
            striped=True,
            bordered=True,
            hover=True,
            responsive=True
        )
    except FileNotFoundError:
        cuadro_4_table = html.P(f"No se encontró el archivo '{table_filename}'. Por favor, verifica que exista.")

    # Actualización del gráfico de correlaciones en Cuadro 3
    try:
        corr_filename = f"correlacion_{variable.replace(' ', '_').lower()}.pkl"
        with open(corr_filename, "rb") as f:
            corr_fig = pickle.load(f)
    except FileNotFoundError:
        corr_fig = go.Figure().update_layout(
            title="Gráfico de correlación no encontrado",
            annotations=[
                dict(
                    text=f"No se encontró el archivo para la variable '{variable}'",
                    x=0.5, y=0.5, showarrow=False, font=dict(size=16))
            ]
        )

    # Actualización del gráfico de violin en Cuadro 2
    try:
        violin_filename = f"violin_{variable.replace(' ', '_').lower()}.pkl"
        with open(violin_filename, "rb") as f:
            violin_fig = pickle.load(f)
        violin_fig.update_layout(
            margin=dict(l=20, r=20, t=20, b=20),  # Márgenes compactos
            width=520,  # Ajusta el tamaño si es necesario
            height=300  # Ajusta el tamaño si es necesario
        )
    except FileNotFoundError:
        violin_fig = go.Figure().update_layout(
            title="Gráfico de violin no encontrado",
            annotations=[
                dict(
                    text=f"No se encontró el archivo para la variable '{variable}'",
                    x=0.1, y=0.1, showarrow=False, font=dict(size=8))
            ]
        )

    return hist_fig, cuadro_4_table, corr_fig, violin_fig

@app.callback(
    [Output('histograma-graph', 'figure'),
     Output('matriz-graph', 'figure'),
     Output('barras-graph', 'figure'),
     Output('violin-graph', 'figure')],
    [Input('slider-variable', 'value')]
)
def up_content(año):
    # Actualización del histograma
    try:
        hist_filename = f"histograma_{año}.pkl"
        with open(hist_filename, "rb") as f:
            hist_a = pickle.load(f)
    except FileNotFoundError:
        hist_a = go.Figure().update_layout(
            title="Histograma no encontrado",
            annotations=[
                dict(
                    text=f"No se encontró el archivo para la variable '{año}'",
                    x=0.5, y=0.5, showarrow=False, font=dict(size=16))
            ]
        )
    try:
        hist_filename = f"matriz_{año}.pkl"
        with open(hist_filename, "rb") as f:
            matriz_a = pickle.load(f)
        matriz_a.update_layout(
            margin=dict(l=10, r=10, t=10, b=10),  # Márgenes compactos
            width=650,  # Ajusta el tamaño si es necesario
            height=450  # Ajusta el tamaño si es necesario
        )
    except FileNotFoundError:
        matriz_a = go.Figure().update_layout(
            title="Histograma no encontrado",
            annotations=[
                dict(
                    text=f"No se encontró el archivo para la variable '{año}'",
                    x=0.5, y=0.5, showarrow=False, font=dict(size=16))
            ]
        )
    try:
        barra_filename = f"barras_{año}.pkl"
        with open(barra_filename, "rb") as f:
            barras_fig = pickle.load(f)
        
    except FileNotFoundError:
        barras_fig = go.Figure().update_layout(
            title="Gráfico de correlación no encontrado",
            annotations=[
                dict(
                    text=f"No se encontró el archivo para la variable '{año}'",
                    x=0.5, y=0.5, showarrow=False, font=dict(size=16))
            ]
        )
    
    try:
        barra_filename = f"violin_{año}.pkl"
        with open(barra_filename, "rb") as f:
            violin_figu = pickle.load(f)
    except FileNotFoundError:
        violin_figu = go.Figure().update_layout(
            title="Gráfico de correlación no encontrado",
            annotations=[
                dict(
                    text=f"No se encontró el archivo para la variable '{año}'",
                    x=0.5, y=0.5, showarrow=False, font=dict(size=16))
            ]
        )
    return hist_a,matriz_a, barras_fig, violin_figu

@app.callback(
    [Output("tabla-supuestos", "children"),
     Output("tabla-vif", "children")],
    [Input("slider-supuestos", "value")]
)
def update_supositions_table(anio_index):
    try:
        filename = f"normality_results_{anio_index}.pkl"
        with open(filename, "rb") as f:
            normality_data = pickle.load(f)

        tabla_suposiciones = dbc.Table.from_dataframe(
            normality_data,
            striped=True,
            bordered=True,
            hover=True,
            responsive=True
        )
    except FileNotFoundError:
        tabla_suposiciones = html.P(f"No se encontró el archivo para el año {anio_index}.")
    try:
        vif_filename = f"vif_data_{anio_index}.pkl"
        with open(vif_filename, "rb") as f:
            vif_data = pickle.load(f)

        tabla_vif = dbc.Table.from_dataframe(
            vif_data,
            striped=True,
            bordered=True,
            hover=True,
            responsive=True
        )
    except FileNotFoundError:
        tabla_vif = html.P(f"No se encontró el archivo para el año {anio_index}.")
    return tabla_suposiciones, tabla_vif


@app.callback(
    [Output("grafica-cuadro-uno", "figure"),
     Output("grafica-dos-dos", "figure"),
     Output("mapa-contenedor", "children")],
    [Input("slider-mapa", "value")]
)
def update_mapa_y_grafica(anio_index):
    # Actualización del mapa
    mapa_filename = f"mapa_interactivo_colores_flc_{anio_index}.html"
    try:
        mapa_content = html.Iframe(
            srcDoc=open(mapa_filename, "r").read(),
            style={"width": "100%", "height": "600px", "border": "none"}
        )
    except FileNotFoundError:
        mapa_content = html.Div("Mapa no disponible para el año seleccionado.")

    # Actualización de la gráfica
    pickle_filename = f"depa_{anio_index}.pkl"
    try:
        with open(pickle_filename, "rb") as f:
            datadep = pickle.load(f)

    except FileNotFoundError:
        datadep = go.Figure().update_layout(
            title="Datos no disponibles",
            annotations=[
                dict(
                    text=f"No se encontró el archivo para el año {anio_index}",
                    x=0.5, y=0.5, showarrow=False, font=dict(size=16)
                )
            ]
        )
    
    pickle_fi= f"ciiu_{anio_index}.pkl"
    try:
        with open(pickle_fi, "rb") as f:
            ciiuda = pickle.load(f)

    except FileNotFoundError:
        ciiuda = go.Figure().update_layout(
            title="Datos no disponibles",
            annotations=[
                dict(
                    text=f"No se encontró el archivo para el año {anio_index}",
                    x=0.5, y=0.5, showarrow=False, font=dict(size=16)
                )
            ]
        )

    return datadep, ciiuda, mapa_content


@app.callback(
    Output("imagen-cuadro-uno", "src"),  # Solo necesitas un Output aquí
    [Input("slider-modelo", "value")]
)
def update_modelo(anio_index):
    # Generar el nombre del archivo de imagen dinámico
    imagen_filename = f"/assets/im_{anio_index}.png"
    return imagen_filename

@app.callback(
    Output("imagen-cuadro-dos", "src"),
    [Input("dropdown-metricas", "value")]
)
def update_dropdown_image(selected_value):
    # Mapear las selecciones del dropdown a los nombres de las imágenes
    metric_to_image_map = {
        "<0": "impor_0.png",
        "[0, 0.67)": "impor_1.png",
        "[0.67, 0.80)": "impor_2.png",
        "[0.80, 1)": "impor_3.png",
        "[1, ∞)": "impor_4.png"
    }
    # Obtener el nombre del archivo basado en la selección
    imagen_filename = f"/assets/{metric_to_image_map[selected_value]}"
    return imagen_filename



if __name__ == '__main__':
    app.run_server()
