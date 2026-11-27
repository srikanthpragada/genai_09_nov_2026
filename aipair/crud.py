"""Validated CRUD operations for courses stored in ``courses.db``."""

import math
import sqlite3
from contextlib import closing, contextmanager
from typing import Any, Dict, Iterator, List, Optional, Tuple


DATABASE_NAME = "courses.db"
MAX_TITLE_LENGTH = 200
MAX_SQLITE_INTEGER = 2**63 - 1


def _validate_course_id(course_id: int) -> int:
    if isinstance(course_id, bool) or not isinstance(course_id, int):
        raise TypeError("course_id must be an integer.")
    if not 1 <= course_id <= MAX_SQLITE_INTEGER:
        raise ValueError("course_id must be a positive SQLite integer.")
    return course_id


def _validate_title(title: str) -> str:
    if not isinstance(title, str):
        raise TypeError("title must be a string.")
    title = title.strip()
    if not title:
        raise ValueError("title must not be empty.")
    if len(title) > MAX_TITLE_LENGTH:
        raise ValueError(f"title must be at most {MAX_TITLE_LENGTH} characters.")
    return title


def _validate_duration(duration: int) -> int:
    if isinstance(duration, bool) or not isinstance(duration, int):
        raise TypeError("duration must be an integer number of units.")
    if not 1 <= duration <= MAX_SQLITE_INTEGER:
        raise ValueError("duration must be a positive SQLite integer.")
    return duration


def _validate_fee(fee: float) -> float:
    if isinstance(fee, bool) or not isinstance(fee, (int, float)):
        raise TypeError("fee must be a number.")
    try:
        fee_value = float(fee)
    except OverflowError as error:
        raise ValueError("fee must be a finite number.") from error
    if not math.isfinite(fee_value):
        raise ValueError("fee must be a finite number.")
    if fee_value < 0:
        raise ValueError("fee must not be negative.")
    return fee_value


def _validate_course(
    title: str, duration: int, fee: float
) -> Tuple[str, int, float]:
    return (
        _validate_title(title),
        _validate_duration(duration),
        _validate_fee(fee),
    )


def _create_table(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL CHECK (length(trim(title)) BETWEEN 1 AND 200),
            duration INTEGER NOT NULL CHECK (duration > 0),
            fee REAL NOT NULL CHECK (fee >= 0)
        )
        """
    )


@contextmanager
def _database_connection() -> Iterator[sqlite3.Connection]:
    with closing(sqlite3.connect(DATABASE_NAME)) as connection:
        connection.row_factory = sqlite3.Row
        with connection:
            _create_table(connection)
            yield connection


def initialize_database() -> None:
    """Create the courses table if it does not already exist."""
    with _database_connection():
        pass


def create_course(title: str, duration: int, fee: float) -> int:
    """Insert a validated course and return its generated ID."""
    title, duration, fee = _validate_course(title, duration, fee)
    with _database_connection() as connection:
        cursor = connection.execute(
            "INSERT INTO courses (title, duration, fee) VALUES (?, ?, ?)",
            (title, duration, fee),
        )
        return int(cursor.lastrowid)


def read_course(course_id: int) -> Optional[Dict[str, Any]]:
    """Return one course as a dictionary, or ``None`` if it does not exist."""
    course_id = _validate_course_id(course_id)
    with _database_connection() as connection:
        row = connection.execute(
            "SELECT id, title, duration, fee FROM courses WHERE id = ?",
            (course_id,),
        ).fetchone()
        return dict(row) if row is not None else None


def list_courses() -> List[Dict[str, Any]]:
    """Return all courses ordered by ID."""
    with _database_connection() as connection:
        rows = connection.execute(
            "SELECT id, title, duration, fee FROM courses ORDER BY id"
        ).fetchall()
        return [dict(row) for row in rows]


def update_course(
    course_id: int, title: str, duration: int, fee: float
) -> None:
    """Replace a course's title, duration, and fee.

    Raises:
        LookupError: If no course has the supplied ID.
    """
    course_id = _validate_course_id(course_id)
    title, duration, fee = _validate_course(title, duration, fee)
    with _database_connection() as connection:
        cursor = connection.execute(
            """
            UPDATE courses
            SET title = ?, duration = ?, fee = ?
            WHERE id = ?
            """,
            (title, duration, fee, course_id),
        )
        if cursor.rowcount == 0:
            raise LookupError(f"Course with id {course_id} does not exist.")


def delete_course(course_id: int) -> None:
    """Delete a course by ID.

    Raises:
        LookupError: If no course has the supplied ID.
    """
    course_id = _validate_course_id(course_id)
    with _database_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM courses WHERE id = ?", (course_id,)
        )
        if cursor.rowcount == 0:
            raise LookupError(f"Course with id {course_id} does not exist.")