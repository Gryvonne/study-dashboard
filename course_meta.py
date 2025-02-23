class Course_Meta:
    def __init__(self, name, ects=None, beginn=None, ende=None, pruefungsoptionen=[]):
        """Initialisiert ein Course_Meta-Objekt mit den gegebenen Attributen.

        Args:
            name (str): Der Name des Kurses.
            ects (float, optional): Die ECTS-Punkte des Kurses. Defaults to None.
            beginn (datetime.date, optional): Das Startdatum des Kurses. Defaults to None.
            ende (datetime.date, optional): Das Enddatum des Kurses. Defaults to None.
            pruefungsoptionen (list, optional): Liste der möglichen Prüfungsarten. Defaults to [].
        """
        self.name = name
        self.ects = ects
        self.beginn = beginn
        self.ende = ende
        self.pruefungsoptionen = pruefungsoptionen

    def get_info(self):
        """Gibt ein Dictionary mit den Meta Kursinformationen zurück.

        Returns:
            dict: Ein Dictionary mit den benötigten Informationen
        """
        return {
            'name': self.name,
            'ects': self.ects,
            'beginn': self.beginn.strftime("%d.%m.%Y") if self.beginn else None,
            'ende': self.ende.strftime("%d.%m.%Y") if self.ende else None
        }
