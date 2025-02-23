from datetime import datetime

class Studium:
    def __init__(self, studium_meta):
        """Initialisiert ein Studium-Objekt

        Args:
            studium_meta (Studium_Meta): Metadaten des Studiums
        """
        self.studium_meta = studium_meta
        self.courses = []
        self.semester = []

    def add_course(self, course):
        """Fügt einen Course zum Studium hinzu

        Args:
            course (Course): Der hinzuzufügende Course
        """
        self.courses.append(course)

    def add_semester(self, semester):
        """Fügt ein Semester zum Studium hinzu

        Args:
            semester (Semester): Das hinzuzufügende Semester
        """
        self.semester.append(semester)

    def get_all_courses(self):
        """Gibt alle Courses des Studiums zurück

        Returns:
            list: Liste aller Courses
        """
        return self.courses

    def get_course(self, name):
        """Sucht einen Course anhand seines Namens

        Args:
            name (str): Name des gesuchten Courses

        Returns:
            Course: Der gefundene Course oder None, wenn nicht gefunden
        """
        for course in self.courses:
            if course.course_meta.name == name:
                return course
        return None

    def calculate_average(self):
        """Berechnet den Durchschnitt aller abgeschlossenen Courses

        Returns:
            float: Der berechnete Durchschnitt oder 0, wenn keine Courses abgeschlossen sind
        """
        completed_courses = [course for course in self.courses if course.is_completed()]
        if not completed_courses:
            return 0
        return sum(course.get_pruefungsleistung().grade for course in completed_courses) / len(completed_courses)

    def get_info(self):
        """Gibt Informationen über das Studium zurück

        Returns:
            dict: Ein Dictionary mit Studiumsinformationen
        """
        return {
            'name': self.studium_meta.name,
            'gesamt_semester': self.studium_meta.gesamt_semester,
            'beginn': self.studium_meta.beginn.strftime("%d.%m.%Y"),
            'ende': self.studium_meta.ende.strftime("%d.%m.%Y"),
            'abschluss': self.studium_meta.abschluss,
            'ects': self.studium_meta.ects,
            'geplanter_durchschnitt': self.studium_meta.geplanter_durchschnitt
        }

    def get_semester_courses(self, semester):
        """Gibt alle Courses für ein bestimmtes Semester zurück

        Args:
            semester (Semester): Das Semester, für das Courses gesucht werden

        Returns:
            list: Liste der Courses im angegebenen Semester
        """
        return [course for course in self.courses if course.course_meta.beginn <= semester.end_datum and course.course_meta.ende >= semester.start_datum]

    def get_current_semester(self):
        """Berechnet das aktuelle Semester basierend auf dem heutigen Datum

        Returns:
            int: Die Nummer des aktuellen Semesters
        """
        today = datetime.now().date()
        months_passed = (today.year - self.studium_meta.beginn.year) * 12 + today.month - self.studium_meta.beginn.month
        current_semester = (months_passed // 6) + 1
        return min(current_semester, self.studium_meta.gesamt_semester)

    def get_remaining_months(self):
        """Berechnet die verbleibenden Monate des Studiums

        Returns:
            int: Anzahl der verbleibenden Monate
        """
        today = datetime.now().date()
        remaining_months = (self.studium_meta.ende.year - today.year) * 12 + self.studium_meta.ende.month - today.month
        return max(0, remaining_months)

    def get_all_semesters(self):
        """Gibt alle Semester des Studiums zurück

        Returns:
            list: Liste aller Semester
        """
        return self.semester
    
    def calculate_overall_progress(self):
        """Berechnet den Gesamtfortschritt des Studiums basierend auf den ECTS-Punkten

        Returns:
            float: Prozentualer Fortschritt des Studiums
        """
        total_ects = self.studium_meta.ects
        completed_ects = sum(course.course_meta.ects for course in self.courses if course.is_completed() and course.course_meta.ects is not None)
        if total_ects > 0:
            return (completed_ects / total_ects) * 100
        return 0
