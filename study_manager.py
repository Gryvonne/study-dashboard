import pandas as pd
from datetime import datetime
from course import Course
from course_meta import Course_Meta
from semester import Semester
from study import Studium
from study_meta import Studium_Meta

class StudyManager:
    def __init__(self, studium=None):
        """Initialisiert den StudyManager

        Args:
            studium (Studium, optional): Ein Studium-Objekt
        """
        self.studium = studium
        self.kurse_csv_file = None
        self.studium_csv_file = None
        self.semester_csv_file = None

    def load_data_from_csv(self, kurse_csv_file, studium_csv_file, semester_csv_file):
        """Lädt Daten aus CSV-Dateien und aktualisiert das Studium-Objekt

        Args:
            kurse_csv_file (str): Pfad zur CSV-Datei mit Kursinformationen
            studium_csv_file (str): Pfad zur CSV-Datei mit Studiumsinformationen
            semester_csv_file (str): Pfad zur CSV-Datei mit Semesterinformationen
        """
        self.kurse_csv_file = kurse_csv_file
        self.studium_csv_file = studium_csv_file
        self.semester_csv_file = semester_csv_file
        
        self.studium.semester.clear()

        # Laden der Studium-Informationen
        studium_df = pd.read_csv(studium_csv_file)
        studium_info = studium_df.iloc[0]

        studium_meta = Studium_Meta(
            name=studium_info['Studium'],
            gesamt_semester=studium_info['Semesterzahl'],
            beginn=datetime.strptime(studium_info['Beginn'], "%d.%m.%Y").date(),
            ende=datetime.strptime(studium_info['Ende'], "%d.%m.%Y").date(),
            abschluss=studium_info['Abschluss'],
            ects=studium_info['ects'],
            geplanter_durchschnitt=studium_info.get('geplanter_durchschnitt', None)
        )

        self.studium.studium_meta = studium_meta

        # Laden der Semesterinformationen
        semester_df = pd.read_csv(semester_csv_file)
        for _, row in semester_df.iterrows():
            semester = Semester(
                nummer=row['Semester'],
                start_datum=datetime.strptime(row['Semesterbeginn'], "%d.%m.%Y").date(),
                end_datum=datetime.strptime(row['Semesterende'], "%d.%m.%Y").date()
            )
            self.studium.add_semester(semester)

        self.studium.courses.clear()
        # Laden der Kurse
        courses_df = pd.read_csv(kurse_csv_file)
        for _, row in courses_df.iterrows():
            course_meta = Course_Meta(
                name=row['Kurs'],
                ects=row['ECTS'] if pd.notnull(row['ECTS']) else None,
                beginn=datetime.strptime(row['Beginn'], "%d.%m.%Y").date() if pd.notnull(row['Beginn']) else None,
                ende=datetime.strptime(row['Ende'], "%d.%m.%Y").date() if pd.notnull(row['Ende']) else None
            )
            course = Course(course_meta)
            
            course.set_pruefungsleistung(row['Prüfungsart'], row['Note'], datetime.strptime(row['Abschluss'], "%d.%m.%Y").date() if pd.notnull(row['Abschluss']) else None)

            self.studium.add_course(course)

    def get_studium(self):
        """Gibt das aktuelle Studium-Objekt zurück

        Returns:
            Studium: Das aktuelle Studium-Objekt
        """
        return self.studium
    
    def update_course_pruefungsleistung(self, course_name, type, grade, abschlussdatum):
        """Aktualisiert die Prüfungsleistung eines Kurses

        Args:
            kurs_name (str): Name des Kurses
            type (str): Art der Prüfungsleistung
            grade (float): Note der Prüfungsleistung
            abschlussdatum (str): Abschlussdatum der Prüfungsleistung

        Returns:
            bool: True, wenn die Aktualisierung erfolgreich war, sonst False
        """
        course = self.studium.get_course(course_name)
        if course:
            course.set_pruefungsleistung(type, grade, datetime.strptime(abschlussdatum, "%d.%m.%Y").date())
            self.update_csv(course_name, type, grade, abschlussdatum)
            return True
        return False
    
    def save_geplanter_durchschnitt(self, geplanter_durchschnitt):
        """Speichert den geplanten Durchschnitt im Studium-Objekt und in der CSV-Datei

        Args:
            geplanter_durchschnitt (float): Der geplante Durchschnitt
        """
        self.studium.studium_meta.geplanter_durchschnitt = geplanter_durchschnitt
        studium_df = pd.read_csv(self.studium_csv_file)
        studium_df.loc[0, 'geplanter_durchschnitt'] = geplanter_durchschnitt
        studium_df.to_csv(self.studium_csv_file, index=False)

    def update_csv(self, course_name, type, grade, abschlussdatum):
        """Aktualisiert die Kursinformationen in der CSV-Datei

        Args:
            kurs_name (str): Name des Kurses
            type (str): Art der Prüfungsleistung
            grade (float): Note der Prüfungsleistung
            abschlussdatum (str): Abschlussdatum der Prüfungsleistung
        """
        if self.kurse_csv_file:
            df = pd.read_csv(self.kurse_csv_file)
            df.loc[df['Kurs'] == course_name, 'Prüfungsart'] = type
            df.loc[df['Kurs'] == course_name, 'Note'] = grade
            df.loc[df['Kurs'] == course_name, 'Abschluss'] = abschlussdatum
            df.to_csv(self.kurse_csv_file, index=False)
