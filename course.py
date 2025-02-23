from datetime import datetime
from graded_work import Graded_Work

class Course:
    def __init__(self, course_meta):
        """Initialisiert ein Course-Objekt.

        Args:
            course (Course_Meta): Das Metadaten-Objekt für den Kurs.
        """
        self.course_meta = course_meta
        self.pruefungsleistung = None
        self.abschluss = None

    def set_pruefungsleistung(self, type, grade, abschlussdatum=None):
        """Setzt die Prüfungsleistung für den Kurs.

        Args:
            type (str): Die Art der Prüfungsleistung (z.B. 'Klausur', 'Portfolio').
            grade (float): Die erhaltene Note für die Prüfungsleistung.
            abschlussdatum (datetime.date, optional): Das Abschlussdatum der Prüfungsleistung.
        """
        self.pruefungsleistung = Graded_Work(type, grade, abschlussdatum)
        self.abschluss = abschlussdatum

    def get_pruefungsleistung(self):
        """Gibt die Prüfungsleistung des Kurses zurück.

        Returns:
            Graded_Work: Das Prüfungsleistungs-Objekt oder None, wenn nicht gesetzt.
        """
        return self.pruefungsleistung

    def is_completed(self):
        """Überprüft, ob der Kurs abgeschlossen ist.

        Returns:
            bool: True, wenn der Kurs ein Abschlussdatum hat, sonst False.
        """
        return self.abschluss is not None

    def get_info(self):
        """Gibt alle Informationen über den Kurs zurück.

        Returns:
            dict: Ein Dictionary mit Course-Metadaten, Prüfungsleistungsinformationen und Abschlussdatum.
        """
        info = self.course_meta.get_info()
        info.update({
            'pruefungsleistung': self.pruefungsleistung.get_info() if self.pruefungsleistung else None,
            'abschluss': self.abschluss.strftime("%d.%m.%Y") if self.abschluss else None
        })
        return info

    def get_time_status(self):
        """Ermittelt den aktuellen Status des Kurses (ist der Abschluss evtl. überfällig?)

        Returns:
            tuple: Status und Farbe zur Visualisierung
        """
        today = datetime.now().date()
        if self.course_meta.beginn and today < self.course_meta.beginn:
            return "Noch nicht begonnen", "gray"
        elif self.abschluss:
            return "Abgeschlossen", "green"
        elif self.course_meta.ende and today > self.course_meta.ende:
            ueberfaellige_tage = (today - self.course_meta.ende).days
            ueberfaellige_wochen = ueberfaellige_tage // 7
            return f"Überfällig ({ueberfaellige_wochen} Wochen)", "red"
        else:
            return "Laufend", "blue"

