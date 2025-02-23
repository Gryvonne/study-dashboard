class Studium_Meta:
    def __init__(self, name, gesamt_semester, beginn, ende, abschluss, ects, geplanter_durchschnitt = None):
        self.name = name
        self.gesamt_semester = gesamt_semester
        self.beginn = beginn
        self.ende = ende
        self.abschluss = abschluss
        self.ects = ects
        self.geplanter_durchschnitt = geplanter_durchschnitt

    def get_info(self):
        """Gibt ein Dictionary mit den Metainformationen des Studiums zurück.

        Returns:
            dict: benötigte Informationen
        """
        return {
            'name': self.name,
            'gesamt_semester': self.gesamt_semester,
            'beginn': self.beginn.strftime("%d.%m.%Y"),
            'ende': self.ende.strftime("%d.%m.%Y"),
            'abschluss': self.abschluss,
            'ects': self.ects,
            'geplanter_durchschnitt': self.geplanter_durchschnitt
        }