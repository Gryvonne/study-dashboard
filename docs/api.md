<a id="course"></a>

# course

<a id="course.Course"></a>

## Course

```python
class Course()
```

<a id="course.Course.__init__"></a>

#### \_\_init\_\_

```python
def __init__(course_meta)
```

Initialisiert ein Course-Objekt.

**Arguments**:

- `course` _Course_Meta_ - Das Metadaten-Objekt für den Kurs.

<a id="course.Course.set_pruefungsleistung"></a>

#### set\_pruefungsleistung

```python
def set_pruefungsleistung(type, grade, abschlussdatum=None)
```

Setzt die Prüfungsleistung für den Kurs.

**Arguments**:

- `type` _str_ - Die Art der Prüfungsleistung (z.B. 'Klausur', 'Portfolio').
- `grade` _float_ - Die erhaltene Note für die Prüfungsleistung.
- `abschlussdatum` _datetime.date, optional_ - Das Abschlussdatum der Prüfungsleistung.

<a id="course.Course.get_pruefungsleistung"></a>

#### get\_pruefungsleistung

```python
def get_pruefungsleistung()
```

Gibt die Prüfungsleistung des Kurses zurück.

**Returns**:

- `Graded_Work` - Das Prüfungsleistungs-Objekt oder None, wenn nicht gesetzt.

<a id="course.Course.is_completed"></a>

#### is\_completed

```python
def is_completed()
```

Überprüft, ob der Kurs abgeschlossen ist.

**Returns**:

- `bool` - True, wenn der Kurs ein Abschlussdatum hat, sonst False.

<a id="course.Course.get_info"></a>

#### get\_info

```python
def get_info()
```

Gibt alle Informationen über den Kurs zurück.

**Returns**:

- `dict` - Ein Dictionary mit Course-Metadaten, Prüfungsleistungsinformationen und Abschlussdatum.

<a id="course.Course.get_time_status"></a>

#### get\_time\_status

```python
def get_time_status()
```

Ermittelt den aktuellen Status des Kurses (ist der Abschluss evtl. überfällig?)

**Returns**:

- `tuple` - Status und Farbe zur Visualisierung

<a id="course_meta"></a>

# course\_meta

<a id="course_meta.Course_Meta"></a>

## Course\_Meta

```python
class Course_Meta()
```

<a id="course_meta.Course_Meta.__init__"></a>

#### \_\_init\_\_

```python
def __init__(name, ects=None, beginn=None, ende=None, pruefungsoptionen=[])
```

Initialisiert ein Course_Meta-Objekt mit den gegebenen Attributen.

**Arguments**:

- `name` _str_ - Der Name des Kurses.
- `ects` _float, optional_ - Die ECTS-Punkte des Kurses. Defaults to None.
- `beginn` _datetime.date, optional_ - Das Startdatum des Kurses. Defaults to None.
- `ende` _datetime.date, optional_ - Das Enddatum des Kurses. Defaults to None.
- `pruefungsoptionen` _list, optional_ - Liste der möglichen Prüfungsarten. Defaults to [].

<a id="course_meta.Course_Meta.get_info"></a>

#### get\_info

```python
def get_info()
```

Gibt ein Dictionary mit den Meta Kursinformationen zurück.

**Returns**:

- `dict` - Ein Dictionary mit den benötigten Informationen

<a id="graded_work"></a>

# graded\_work

<a id="graded_work.Graded_Work"></a>

## Graded\_Work

```python
class Graded_Work()
```

<a id="graded_work.Graded_Work.__init__"></a>

#### \_\_init\_\_

```python
def __init__(type, grade, datum)
```

Initialisiert ein Graded_Work-Objekt.

**Arguments**:

- `type` _str_ - Die Art der Prüfungsleistung (z.B. 'Klausur', 'Portfolio').
- `grade` _float_ - Die erhaltene Note für die Prüfungsleistung.
- `datum` _datetime.date_ - Das Datum der Prüfungsleistung.

<a id="graded_work.Graded_Work.get_info"></a>

#### get\_info

```python
def get_info()
```

Gibt Informationen über die Prüfungsleistung zurück.

**Returns**:

- `dict` - Art der Prüfungsleistung und Note

<a id="semester"></a>

# semester

<a id="semester.Semester"></a>

## Semester

```python
class Semester()
```

<a id="semester.Semester.__init__"></a>

#### \_\_init\_\_

```python
def __init__(nummer, start_datum, end_datum)
```

Initialisiert ein Semester-Objekt.

**Arguments**:

- `nummer` _int_ - Semester.
- `start_datum` _str oder datetime.date_ - Das Startdatum des Semesters.
- `end_datum` _str oder datetime.date_ - Das Enddatum des Semesters.

<a id="study"></a>

# study

<a id="study.Studium"></a>

## Studium

```python
class Studium()
```

<a id="study.Studium.__init__"></a>

#### \_\_init\_\_

```python
def __init__(studium_meta)
```

Initialisiert ein Studium-Objekt

**Arguments**:

- `studium_meta` _Studium_Meta_ - Metadaten des Studiums

<a id="study.Studium.add_course"></a>

#### add\_course

```python
def add_course(course)
```

Fügt einen Course zum Studium hinzu

**Arguments**:

- `course` _Course_ - Der hinzuzufügende Course

<a id="study.Studium.add_semester"></a>

#### add\_semester

```python
def add_semester(semester)
```

Fügt ein Semester zum Studium hinzu

**Arguments**:

- `semester` _Semester_ - Das hinzuzufügende Semester

<a id="study.Studium.get_all_courses"></a>

#### get\_all\_courses

```python
def get_all_courses()
```

Gibt alle Courses des Studiums zurück

**Returns**:

- `list` - Liste aller Courses

<a id="study.Studium.get_course"></a>

#### get\_course

```python
def get_course(name)
```

Sucht einen Course anhand seines Namens

**Arguments**:

- `name` _str_ - Name des gesuchten Courses
  

**Returns**:

- `Course` - Der gefundene Course oder None, wenn nicht gefunden

<a id="study.Studium.calculate_average"></a>

#### calculate\_average

```python
def calculate_average()
```

Berechnet den Durchschnitt aller abgeschlossenen Courses

**Returns**:

- `float` - Der berechnete Durchschnitt oder 0, wenn keine Courses abgeschlossen sind

<a id="study.Studium.get_info"></a>

#### get\_info

```python
def get_info()
```

Gibt Informationen über das Studium zurück

**Returns**:

- `dict` - Ein Dictionary mit Studiumsinformationen

<a id="study.Studium.get_semester_courses"></a>

#### get\_semester\_courses

```python
def get_semester_courses(semester)
```

Gibt alle Courses für ein bestimmtes Semester zurück

**Arguments**:

- `semester` _Semester_ - Das Semester, für das Courses gesucht werden
  

**Returns**:

- `list` - Liste der Courses im angegebenen Semester

<a id="study.Studium.get_current_semester"></a>

#### get\_current\_semester

```python
def get_current_semester()
```

Berechnet das aktuelle Semester basierend auf dem heutigen Datum

**Returns**:

- `int` - Die Nummer des aktuellen Semesters

<a id="study.Studium.get_remaining_months"></a>

#### get\_remaining\_months

```python
def get_remaining_months()
```

Berechnet die verbleibenden Monate des Studiums

**Returns**:

- `int` - Anzahl der verbleibenden Monate

<a id="study.Studium.get_all_semesters"></a>

#### get\_all\_semesters

```python
def get_all_semesters()
```

Gibt alle Semester des Studiums zurück

**Returns**:

- `list` - Liste aller Semester

<a id="study.Studium.calculate_overall_progress"></a>

#### calculate\_overall\_progress

```python
def calculate_overall_progress()
```

Berechnet den Gesamtfortschritt des Studiums basierend auf den ECTS-Punkten

**Returns**:

- `float` - Prozentualer Fortschritt des Studiums

<a id="study_dashboard"></a>

# study\_dashboard

<a id="study_dashboard.StudyDashboard"></a>

## StudyDashboard

```python
class StudyDashboard()
```

<a id="study_dashboard.StudyDashboard.__init__"></a>

#### \_\_init\_\_

```python
def __init__(kurse_csv_file, studium_csv_file, semester_csv_file)
```

Initialisiert das StudyDashboard.

**Arguments**:

- `kurse_csv_file` _str_ - Pfad zur CSV-Datei mit Kursinformationen.
- `studium_csv_file` _str_ - Pfad zur CSV-Datei mit Studiumsinformationen.
- `semester_csv_file` _str_ - Pfad zur CSV-Datei mit Semesterinformationen.

<a id="study_dashboard.StudyDashboard.create_studium_info"></a>

#### create\_studium\_info

```python
def create_studium_info()
```

Erstellt eine Karte mit Informationen zum Studium.

**Returns**:

  dbc.Card oder html.Div: Eine Karte mit Studiumsinformationen oder eine Meldung, wenn keine Informationen verfügbar sind.

<a id="study_dashboard.StudyDashboard.create_layout"></a>

#### create\_layout

```python
def create_layout()
```

Erstellt das Layout für das Dashboard.

<a id="study_dashboard.StudyDashboard.run"></a>

#### run

```python
def run()
```

Startet den Server

<a id="study_dashboard.StudyDashboard.register_callbacks"></a>

#### register\_callbacks

```python
def register_callbacks()
```

Registriert alle Callback-Funktionen für das Dashboard

<a id="study_dashboard.StudyDashboard.create_pruefungsleistung_visualization"></a>

#### create\_pruefungsleistung\_visualization

```python
def create_pruefungsleistung_visualization(grade)
```

Erstellt eine Visualisierung für eine Prüfungsleistung.

**Arguments**:

- `grade` _float_ - Die Note, die visualisiert werden soll.
  

**Returns**:

- `go.Figure` - Eine Plotly-Figur, die die Note als Kreisdiagramm darstellt.

<a id="study_manager"></a>

# study\_manager

<a id="study_manager.StudyManager"></a>

## StudyManager

```python
class StudyManager()
```

<a id="study_manager.StudyManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(studium=None)
```

Initialisiert den StudyManager

**Arguments**:

- `studium` _Studium, optional_ - Ein Studium-Objekt

<a id="study_manager.StudyManager.load_data_from_csv"></a>

#### load\_data\_from\_csv

```python
def load_data_from_csv(kurse_csv_file, studium_csv_file, semester_csv_file)
```

Lädt Daten aus CSV-Dateien und aktualisiert das Studium-Objekt

**Arguments**:

- `kurse_csv_file` _str_ - Pfad zur CSV-Datei mit Kursinformationen
- `studium_csv_file` _str_ - Pfad zur CSV-Datei mit Studiumsinformationen
- `semester_csv_file` _str_ - Pfad zur CSV-Datei mit Semesterinformationen

<a id="study_manager.StudyManager.get_studium"></a>

#### get\_studium

```python
def get_studium()
```

Gibt das aktuelle Studium-Objekt zurück

**Returns**:

- `Studium` - Das aktuelle Studium-Objekt

<a id="study_manager.StudyManager.update_course_pruefungsleistung"></a>

#### update\_course\_pruefungsleistung

```python
def update_course_pruefungsleistung(course_name, type, grade, abschlussdatum)
```

Aktualisiert die Prüfungsleistung eines Kurses

**Arguments**:

- `kurs_name` _str_ - Name des Kurses
- `type` _str_ - Art der Prüfungsleistung
- `grade` _float_ - Note der Prüfungsleistung
- `abschlussdatum` _str_ - Abschlussdatum der Prüfungsleistung
  

**Returns**:

- `bool` - True, wenn die Aktualisierung erfolgreich war, sonst False

<a id="study_manager.StudyManager.save_geplanter_durchschnitt"></a>

#### save\_geplanter\_durchschnitt

```python
def save_geplanter_durchschnitt(geplanter_durchschnitt)
```

Speichert den geplanten Durchschnitt im Studium-Objekt und in der CSV-Datei

**Arguments**:

- `geplanter_durchschnitt` _float_ - Der geplante Durchschnitt

<a id="study_manager.StudyManager.update_csv"></a>

#### update\_csv

```python
def update_csv(course_name, type, grade, abschlussdatum)
```

Aktualisiert die Kursinformationen in der CSV-Datei

**Arguments**:

- `kurs_name` _str_ - Name des Kurses
- `type` _str_ - Art der Prüfungsleistung
- `grade` _float_ - Note der Prüfungsleistung
- `abschlussdatum` _str_ - Abschlussdatum der Prüfungsleistung

<a id="study_meta"></a>

# study\_meta

<a id="study_meta.Studium_Meta"></a>

## Studium\_Meta

```python
class Studium_Meta()
```

<a id="study_meta.Studium_Meta.get_info"></a>

#### get\_info

```python
def get_info()
```

Gibt ein Dictionary mit den Metainformationen des Studiums zurück.

**Returns**:

- `dict` - benötigte Informationen

