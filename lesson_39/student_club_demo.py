#!/usr/bin/env python3

import sqlite3
from pathlib import Path


DB_FILE = "student_clubs_demo.sqlite"


SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Student (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Club (
    club_id INTEGER PRIMARY KEY,
    club_name TEXT NOT NULL
);

-- TODO: Create the StudentClub table.
-- TODO: Think carefully about which columns it needs.
-- TODO: Think about how StudentClub should connect Student and Club.
-- TODO: Think about what should happen if a linked student or club is deleted.
"""


SAMPLE_STUDENTS = [
    (1, "Ava Chen"),
    (2, "Noah Singh"),
]


SAMPLE_CLUBS = [
    (1, "Robotics Club"),
]


def connect(db_file: str) -> sqlite3.Connection:
    conn = sqlite3.connect(db_file)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)
    conn.commit()


def insert_sample_data(conn: sqlite3.Connection) -> None:
    conn.executemany(
        "INSERT OR IGNORE INTO Student (student_id, name) VALUES (?, ?)",
        SAMPLE_STUDENTS,
    )

    conn.executemany(
        "INSERT OR IGNORE INTO Club (club_id, club_name) VALUES (?, ?)",
        SAMPLE_CLUBS,
    )

    # TODO: Insert rows into StudentClub after you create that table.
    # TODO: Decide which student should belong to which club.
    # TODO: Check that the student_id and club_id values actually exist first.

    conn.commit()


def show_students(conn: sqlite3.Connection) -> None:
    print("Students:")
    for student_id, name in conn.execute(
        "SELECT student_id, name FROM Student ORDER BY student_id"
    ):
        print(f"  {student_id}: {name}")


def show_clubs(conn: sqlite3.Connection) -> None:
    print("\nClubs:")
    for club_id, club_name in conn.execute(
        "SELECT club_id, club_name FROM Club ORDER BY club_id"
    ):
        print(f"  {club_id}: {club_name}")


def show_student_clubs(conn: sqlite3.Connection) -> None:
    # TODO: Replace this placeholder with a query that shows each student
    # TODO: and the club or clubs they belong to.
    # TODO: You will need to use the StudentClub table once it exists.
    print("\nStudent club memberships:")
    print("  TODO: complete this section")


def main() -> None:
    db_path = Path(DB_FILE)

    with connect(db_path) as conn:
        create_schema(conn)
        insert_sample_data(conn)

        show_students(conn)
        show_clubs(conn)
        show_student_clubs(conn)

    print(f"\nDatabase created: {db_path.resolve()}")


if __name__ == "__main__":
    main()
