import datetime


class Semester:
    def __init__(self, nummer, start_datum, end_datum):
        """Initialisiert ein Semester-Objekt.

        Args:
            nummer (int): Semester.
            start_datum (str oder datetime.date): Das Startdatum des Semesters.
            end_datum (str oder datetime.date): Das Enddatum des Semesters.
        """
        # Konvertiert das Startdatum in ein datetime.date-Objekt, falls es als String übergeben wurde
        if isinstance(start_datum, str):
            self.start_datum = datetime.strptime(start_datum, "%d.%m.%Y").date()
        else:
            self.start_datum = start_datum

        # Konvertiert das Enddatum in ein datetime.date-Objekt, falls es als String übergeben wurde
        if isinstance(end_datum, str):
            self.end_datum = datetime.strptime(end_datum, "%d.%m.%Y").date()
        else:
            self.end_datum = end_datum

        self.nummer = nummer

    
    # def get_dauer(self):
    #     """Berechnet die Dauer des Semesters in Tagen.

    #     Returns:
    #         int: Die Anzahl der Tage zwischen Start- und Enddatum.
    #     """
    #     return (self.end_datum - self.start_datum).days

    # def ist_aktuell(self, datum=None):
    #     """Überprüft, ob das gegebene Datum innerhalb des Semesters liegt.

    #     Args:
    #         datum (datetime.date, optional): Das zu überprüfende Datum. 
    #                                          Standardmäßig wird das aktuelle Datum verwendet.

    #     Returns:
    #         bool: True, wenn das Datum innerhalb des Semesters liegt, sonst False.
    #     """
    #     if datum is None:
    #         datum = datetime.date.today()
    #     return self.start_datum <= datum <= self.end_datum
