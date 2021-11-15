"""Utility functions."""

__author__ = "730245854"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]: 
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")
    
    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(column_table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Returns the first n number of rows of a table."""
    result: dict[str, list[str]] = {}
    if number_of_rows >= len(column_table): 
        return column_table 
    else:
        for column in column_table:
            empty_list = []
            for i in range(number_of_rows):
                empty_list.append(column_table[column][i])
            result[column] = empty_list
    return result 


def select(column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Selecting columns to analyze."""
    result: dict[str, list[str]] = {}
    for column in column_names:
        result[column] = column_table[column]
    return result 


def concat(column_table_1: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]: 
    """Combines two dictionaries."""
    result: dict[str, list[str]] = {}
    for column in column_table_1:
        result[column] = column_table_1[column]
    for column in column_table_2:
        if column in result: 
            result[column] += column_table_2[column]
        else:
            result[column] = column_table_2[column]
    return result


def count(list: list[str]) -> dict[str, int]:
    """Counts the occurrences of a value in a dictionary."""
    result: dict[str, int] = {}
    for item in list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result