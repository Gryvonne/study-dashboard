import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
from study_manager import StudyManager
from datetime import datetime
from study import Studium
from study_meta import Studium_Meta

class StudyDashboard:
    def __init__(self, kurse_csv_file, studium_csv_file, semester_csv_file):
        """Initialisiert das StudyDashboard.

        Args:
            kurse_csv_file (str): Pfad zur CSV-Datei mit Kursinformationen.
            studium_csv_file (str): Pfad zur CSV-Datei mit Studiumsinformationen.
            semester_csv_file (str): Pfad zur CSV-Datei mit Semesterinformationen.
        """
        self.studium = Studium(Studium_Meta("", 0, datetime.now(), datetime.now(), "", ""))
        self.studium_manager = StudyManager(self.studium)
        self.studium_manager.load_data_from_csv(kurse_csv_file, studium_csv_file, semester_csv_file)
        self.app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
        self.create_layout()
        self.register_callbacks()

    def create_studium_info(self):
        """Erstellt eine Karte mit Informationen zum Studium.

        Returns:
            dbc.Card oder html.Div: Eine Karte mit Studiumsinformationen oder eine Meldung, wenn keine Informationen verfügbar sind.
        """
        studium_info = self.studium_manager.studium.get_info()
        if studium_info:
            current_semester = self.studium_manager.studium.get_current_semester()
            remaining_months = self.studium_manager.studium.get_remaining_months()
            return dbc.Card([
                dbc.CardBody([
                    html.H2(studium_info['name']),
                    html.P(f"Abschluss: {studium_info['abschluss']}"),
                    html.P(f"Gesamtdauer: {studium_info['gesamt_semester']} Semester"),
                    html.P(f"Beginn: {studium_info['beginn']}"),
                    html.P(f"Ende: {studium_info['ende']}"),
                    html.P(f"Aktuelles Semester: {current_semester}"),
                    html.P(f"Verbleibende Monate: {remaining_months}"),
                    html.P(f"Gesamt ECTS: {studium_info['ects']}")
                ])
            ], className='mb-4', style={'height': '100%'})
        return html.Div("Keine Studieninformationen verfügbar.")

    def create_layout(self):
        """Erstellt das Layout für das Dashboard."""
        semesters = self.studium_manager.studium.get_all_semesters()
        current_semester = self.studium_manager.studium.get_current_semester()
        semester_options = [
            {'label': f"Semester {semester.nummer} (aktuelles Semester)" if semester.nummer == current_semester else f"Semester {semester.nummer}", 
             'value': semester.nummer} 
            for semester in semesters
        ]

        self.app.layout = dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1('Angewandte künstliche Intelligenz',
                            className='text-center mb-4 mt-3',
                            style={'color': '#2C3E50'})
                ])
            ], className='header-gradient mb-4'),
            dbc.Row([
                dbc.Col([
                    self.create_studium_info()
                ], width=6, className='mb-4'),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4("Gesamtfortschritt"),
                            dbc.Progress(id='progress-bar', value=0, max=100, striped=False, animated=False, style={"height": "30px"}, color="gray"),
                            html.P(id='progress-text', className="text-center mt-2")
                        ])
                    , dbc.CardBody([
                html.H4("Geplanter Durchschnitt"),
                html.Div([
                    html.Span(id="geplanter-durchschnitt-anzeige", className="mr-2"),
                    dbc.Button("Ändern", id="geplanter-durchschnitt-button", color="primary", size="sm")
                ], className="d-flex justify-content-between align-items-center")
            ])], className='mb-4'),
                    
                ], width=6),
                
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(
                        id='semester-dropdown',
                        options=semester_options,
                        value=current_semester,
                        clearable=False,
                        className='mb-4'
                    )
                ], width=6),
                dbc.Col([
                    dcc.Dropdown(
                        id='course-dropdown',
                        options=[{'label': course.course_meta.name, 'value': course.course_meta.name} for course in self.studium_manager.studium.get_all_courses()],
                        value=self.studium_manager.studium.get_all_courses()[0].course_meta.name if self.studium_manager.studium.get_all_courses() else None,
                        clearable=False,
                        className='mb-4'
                    )
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Div(id='course-info'),
                            dbc.Button('Note eintragen', id='pruefungsleistung-button', color='success', className='mt-3')
                        ])
                    ], className='h-100')
                ], width=6),
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    html.Div(id='pruefungsleistung-viz', className='d-flex justify-content-center'),
                                    html.H3(id='course-name', className='text-center mt-3')
                                ])
                            ], className='h-100')
                        ], width=6),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardBody([
                                    dcc.Graph(id='gesamt-viz', className='d-flex justify-content-center'),
                                    html.H3("Gesamtdurchschnitt", className='text-center mt-3')
                                ], className='d-flex flex-column align-items-center')  # Neue Klasse hinzugefügt
                            ], className='h-100')
                        ], width=6)

                    ])
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Button('Daten aktualisieren', id='reload-button', color='primary', className='mt-4')
                ], width=12, className='text-center')
            ]),
            dbc.Modal([
                dbc.ModalHeader("Note eintragen"),
                dbc.ModalBody([
                    dcc.Dropdown(
                        id="pruefungsart-dropdown",
                        options=[
                            {'label': 'Klausur', 'value': 'Klausur'},
                            {'label': 'Portfolio', 'value': 'Portfolio'},
                            {'label': 'Advanced Workbook', 'value': 'Advanced Workbook'},
                            {'label': 'Fallstudie', 'value': 'Fallstudie'}
                        ],
                        placeholder="Prüfungsart auswählen"
                    ),
                    dbc.Input(id="pruefungsleistung-input", type="number", placeholder="Note eingeben", min=1, max=5, step=0.1),
                    dbc.Input(id="abschlussdatum-input", type="text", placeholder="Abschlussdatum eingeben (TT.MM.JJJJ)")
                ]),
                dbc.ModalFooter([
                    dbc.Button("Abbrechen", id="close-modal", className="ms-auto", n_clicks=0),
                    dbc.Button("Speichern", id="save-pruefungsleistung", className="ms-2", n_clicks=0),
                ]),
            ], id="pruefungsleistung-modal", is_open=False),
            dbc.Modal([
    dbc.ModalHeader("Geplanten Durchschnitt ändern"),
    dbc.ModalBody([
        dbc.Input(id="geplanter-durchschnitt-input", type="number", min=1, max=5, step=0.1, placeholder="Geplanter Durchschnitt")
    ]),
    dbc.ModalFooter([
        dbc.Button("Abbrechen", id="close-geplanter-durchschnitt-modal", className="ms-auto"),
        dbc.Button("Speichern", id="save-geplanter-durchschnitt", className="ms-2")
    ])
], id="geplanter-durchschnitt-modal", is_open=False)

        ], fluid=True, className='dashboard-container')

    def run(self):
        """Startet den Server"""
        self.app.run_server(debug=True)

    def register_callbacks(self):
        """Registriert alle Callback-Funktionen für das Dashboard"""
        @self.app.callback(
            Output('semester-info', 'children'),
            Input('semester-dropdown', 'value')
        )
        def update_semester_info(selected_semester):
            """Aktualisiert die Semesterinformationen basierend auf der Auswahl.

            Args:
                selected_semester (int): Die Nummer des ausgewählten Semesters.

            Returns:
                html.Div: Ein Div-Element mit Informationen zum ausgewählten Semester.
            """
            semester = next((s for s in self.studium_manager.studium.get_all_semesters() if s.nummer == selected_semester), None)
            if semester:
                semester_courses = self.studium_manager.studium.get_semester_courses(semester)
                courses_list = html.Ul([html.Li(course.course_meta.name) for course in semester_courses])
                return html.Div([
                    html.H4(f"Semester {semester.nummer}"),
                    html.P(f"Startdatum: {semester.start_datum.strftime('%d.%m.%Y')}"),
                    html.P(f"Enddatum: {semester.end_datum.strftime('%d.%m.%Y')}"),
                    html.H5("Kurse:"),
                    courses_list
                ])
            return html.Div("Keine Informationen für das ausgewählte Semester verfügbar.")
        @self.app.callback(
            Output("geplanter-durchschnitt-modal", "is_open"),
            [Input("geplanter-durchschnitt-button", "n_clicks"), Input("close-geplanter-durchschnitt-modal", "n_clicks"), Input("save-geplanter-durchschnitt", "n_clicks")],
            [State("geplanter-durchschnitt-modal", "is_open")]
        )
        def toggle_geplanter_durchschnitt_modal(n1, n2, n3, is_open):
            """Steuert das Öffnen und Schließen des Modals für den geplanten Durchschnitt. Wird einer der relevanten Buttons geklickt, schließt oder öffnet sich das Modal

            Args:
                n1 (int): Klicks auf den "Ändern"-Button.
                n2 (int): Klicks auf den "Abbrechen"-Button.
                n3 (int): Klicks auf den "Speichern"-Button.
                is_open (bool): Aktueller Zustand des Modals.

            Returns:
                bool: Neuer Zustand des Modals (geöffnet oder geschlossen).
            """
            if n1 or n2 or n3:
                return not is_open
            return is_open

        @self.app.callback(
            Output("geplanter-durchschnitt-anzeige", "children"),
            Output("geplanter-durchschnitt-anzeige", "style"),
            Input("save-geplanter-durchschnitt", "n_clicks"),
            Input('reload-button', 'n_clicks'),
            Input('gesamt-viz', 'figure'),  # Neuer Input für den Gesamtdurchschnitt
            State("geplanter-durchschnitt-input", "value")
        )
        def update_geplanter_durchschnitt(save_clicks, reload_clicks, gesamt_viz, geplanter_durchschnitt):
            """Aktualisiert die Anzeige des geplanten Durchschnitts.

            Args:
                save_clicks (int): Anzahl der Klicks auf den "Speichern"-Button.
                reload_clicks (int): Anzahl der Klicks auf den "Daten aktualisieren"-Button.
                gesamt_viz (dict): Die Gesamtvisualisierung (wird für Aktualisierungen verwendet).
                geplanter_durchschnitt (float): Der eingegebene geplante Durchschnitt.

            Returns:
                tuple: Ein Tupel mit dem anzuzeigenden Text und dem Stil für die Anzeige.
            """
            ctx = dash.callback_context
            if not ctx.triggered:
                button_id = 'No clicks yet'
            else:
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]

            if button_id == 'save-geplanter-durchschnitt' and geplanter_durchschnitt is not None:
                self.studium_manager.save_geplanter_durchschnitt(geplanter_durchschnitt)
            elif button_id == 'reload-button':
                self.studium_manager.load_data_from_csv(self.studium_manager.kurse_csv_file, self.studium_manager.studium_csv_file, self.studium_manager.semester_csv_file)
            
            geplanter_durchschnitt = self.studium_manager.studium.studium_meta.geplanter_durchschnitt
            if geplanter_durchschnitt is None:
                return "Nicht festgelegt", {}

            tatsaechlicher_durchschnitt = self.studium_manager.studium.calculate_average()
            
            def get_color(diff):
                if diff == 0:
                    return "#239B56"
                elif diff <= 0.3:
                    return "#2ECC71"
                elif diff <= 0.6:
                    return "#F4D03F"
                elif diff <= 0.9:
                    return "#E67E22"
                else:
                    return "#E74C3C"
            
            diff = tatsaechlicher_durchschnitt - geplanter_durchschnitt
            color = get_color(diff)
            
            return f"{geplanter_durchschnitt:.1f}", {
                "color": "black",
                "font-weight": "bold",
                "font-size": "20px",
                "background-color": color,
                "padding": "5px 10px",
                "border-radius": "5px"
            }


        @self.app.callback(
            Output('course-info', 'children'),
            Output('course-name', 'children'),
            Output('pruefungsleistung-viz', 'children'),
            Output('gesamt-viz', 'figure'),
            Output('course-dropdown', 'options'),
            Output('progress-bar', 'value'),
            Output('progress-text', 'children'),
            Output('pruefungsleistung-button', 'style'),
            Input('semester-dropdown', 'value'),
            Input('course-dropdown', 'value'),
            Input('reload-button', 'n_clicks'),
            Input('save-pruefungsleistung', 'n_clicks'),
            State('course-dropdown', 'value'),
            State('pruefungsleistung-input', 'value'),
            State('abschlussdatum-input', 'value')
        )
        def update_dashboard(selected_semester, selected_course, reload_clicks, save_clicks, current_course, pruefungsleistung, abschlussdatum):
            """Aktualisiert das Dashboard basierend auf den Benutzerinteraktionen.

            Args:
                selected_semester (int): Die Nummer des ausgewählten Semesters.
                selected_course (str): Der Name des ausgewählten Kurses.
                reload_clicks (int): Anzahl der Klicks auf den "Daten aktualisieren"-Button.
                save_clicks (int): Anzahl der Klicks auf den "Speichern"-Button für Prüfungsleistungen.
                current_course (str): Der aktuell ausgewählte Kurs.
                pruefungsleistung (float): Die eingegebene Note für die Prüfungsleistung.
                abschlussdatum (str): Das eingegebene Abschlussdatum für die Prüfungsleistung.

            Returns:
                tuple: Ein Tupel mit allen aktualisierten Elementen des Dashboards.
            """
            ctx = dash.callback_context
            if not ctx.triggered:
                button_id = 'No clicks yet'
            else:
                button_id = ctx.triggered[0]['prop_id'].split('.')[0]

            if button_id == 'reload-button' and reload_clicks:
                self.studium_manager.load_data_from_csv(self.studium_manager.kurse_csv_file, self.studium_manager.studium_csv_file, self.studium_manager.semester_csv_file)
            elif button_id == 'save-pruefungsleistung' and save_clicks:
                if pruefungsleistung is not None and abschlussdatum:
                    self.studium_manager.update_course_pruefungsleistung(current_course, "Klausur", pruefungsleistung, abschlussdatum)

            # Filtern der Kurse für das ausgewählte Semester
            semester = next((s for s in self.studium_manager.studium.get_all_semesters() if s.nummer == selected_semester), None)
            if semester:
                semester_courses = self.studium_manager.studium.get_semester_courses(semester)
                course_options = [{'label': course.course_meta.name, 'value': course.course_meta.name} for course in semester_courses]
            else:
                course_options = []

            # Berechnung des Gesamtfortschritts
            progress = self.studium_manager.studium.calculate_overall_progress()
            progress_text = f"{progress:.1f}% abgeschlossen"

            course = self.studium_manager.studium.get_course(selected_course)
            durchschnitt = self.studium_manager.studium.calculate_average()
            gesamt_viz = self.create_pruefungsleistung_visualization(durchschnitt)
            button_style = {'display': 'block'} if selected_course else {'display': 'none'}
            if course:
                info = course.get_info()
                print(info)
                pruefungsleistung_info = info['pruefungsleistung'] if info['pruefungsleistung'] else {}
                time_status, color = course.get_time_status()
                course_info = html.Div([
                    html.P(f"Prüfungsart: {pruefungsleistung_info.get('type', 'Nicht festgelegt')}"),
                    html.P(f"Note: {pruefungsleistung_info.get('grade', 'Noch nicht eingetragen')}"),
                    html.P(f"ECTS: {info['ects'] if info['ects'] is not None else 'Nicht abgeschlossen'}"),
                    html.P(f"Beginn: {info['beginn'] if info['beginn'] is not None else 'Nicht angegeben'}"),
                    html.P(f"Geplantes Ende: {info['ende'] if info['ende'] is not None else 'Nicht angegeben'}"),
                    html.P(f"Abschluss: {info['abschluss'] if info['abschluss'] is not None else 'Nicht abgeschlossen'}"),
                    html.P(time_status, style={'color': color, 'fontWeight': 'bold'})
                ])

                if course.is_completed():
                    note_viz = dcc.Graph(figure=self.create_pruefungsleistung_visualization(course.get_pruefungsleistung().grade), config={'displayModeBar': False})
                else:
                    note_viz = html.Div([
                        html.H3("Noch keine Note eingetragen"),
                    ])

                return course_info, info['name'], note_viz, gesamt_viz, course_options, progress, progress_text, button_style

            return html.Div(), "", html.Div(), gesamt_viz, course_options, progress, progress_text, button_style



        @self.app.callback(
            Output("pruefungsleistung-modal", "is_open"),
            [Input("pruefungsleistung-button", "n_clicks"), Input("close-modal", "n_clicks"), Input("save-pruefungsleistung", "n_clicks")],
            [State("pruefungsleistung-modal", "is_open")]
        )
        def toggle_modal(n1, n2, n3, is_open):
            """Steuert das Öffnen und Schließen des Modals für das Eintragen von Leistungen. Wird einer der relevanten Buttons geklickt, schließt oder öffnet sich das Modal

            Args:
                n1 (int): Klicks auf den "Note eintragen"-Button.
                n2 (int): Klicks auf den "Abbrechen"-Button.
                n3 (int): Klicks auf den "Speichern"-Button.
                is_open (bool): Aktueller Zustand des Modals.

            Returns:
                bool: Neuer Zustand des Modals (geöffnet oder geschlossen).
            """
            if n1 or n2 or n3:
                return not is_open
            return is_open

    def create_pruefungsleistung_visualization(self, grade):
        """Erstellt eine Visualisierung für eine Prüfungsleistung.

        Args:
            grade (float): Die Note, die visualisiert werden soll.

        Returns:
            go.Figure: Eine Plotly-Figur, die die Note als Kreisdiagramm darstellt.
        """
        colors = ['#239B56', '#2ECC71', '#F4D03F', '#E67E22', '#E74C3C']

        def get_color(value):
            if value is None:
                return '#BDC3C7'  # Eine neutrale Farbe für nicht gesetzte Werte
            if 1 <= value < 1.5:
                return colors[0]
            elif 1.5 <= value < 2.5:
                return colors[1]
            elif 2.5 <= value < 3.5:
                return colors[2]
            elif 3.5 <= value < 4:
                return colors[3]
            else:
                return colors[4]

        fig = go.Figure()

        # Innerer Ring für die spezifische Note
        fig.add_trace(go.Pie(
            values=[1],
            labels=[''],
            marker_colors=[get_color(grade)],
            textinfo='none',
            hoverinfo='skip',
            hole=0,
            showlegend=False,
            
        ))

        # Äußerer Ring für den Leistungsbereich
        fig.add_trace(go.Pie(
        values=[0.5, 1, 1, 0.5, 1],
        labels=['1.0-1.5', '1.5-2.5', '2.5-3.5', '3.5-4.0', '4.0-5.0'],
        marker_colors=colors,
        textinfo='none',
        hoverinfo='label',
        hole=0.85,
        direction='clockwise',
        sort=False,
        showlegend=True
    ))

        # Text für die Note
        fig.add_annotation(
            text=f"{grade:.1f}" if grade is not None else "---",
            font=dict(size=50, color='black', family="Arial Black"),
            showarrow=False,
            x=0.5,
            y=0.5,
            xanchor='center',
            yanchor='middle'
        )

        fig.update_layout(
            width=250,
            height=250,
            margin=dict(l=0, r=0, t=0, b=0),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            showlegend=False
        )

        return fig

if __name__ == '__main__':
    dashboard = StudyDashboard('data/kurse.csv', 'data/studium.csv', 'data/semester.csv')
    dashboard.run()