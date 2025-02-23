import math


class Graded_Work:
    def __init__(self, type, grade, datum):
        """Initialisiert ein Graded_Work-Objekt.

        Args:
            type (str): Die Art der Prüfungsleistung (z.B. 'Klausur', 'Portfolio').
            grade (float): Die erhaltene Note für die Prüfungsleistung.
            datum (datetime.date): Das Datum der Prüfungsleistung.
        """
        self.type = type
        self.grade = grade

    def get_info(self):
        """Gibt Informationen über die Prüfungsleistung zurück.

        Returns:
            dict: Art der Prüfungsleistung und Note
        """
        return {
            'type': self.type,
            'grade': self.grade if not math.isnan(self.grade) else 'Noch nicht eingetragen'
        }
