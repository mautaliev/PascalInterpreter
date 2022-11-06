from bin_digits import BinaryDigit


TEST_TYPES_TEXT = """
    VAR
        a : INTEGER;
        b : CHAR
    BEGIN
        a := 10+11;
    END.
"""
TEST_VARIABLES_TEXT = """
    VAR
        a : INTEGER;
        b : CHAR
    BEGIN
        a := 10+11;
        b := 'tralala'
    END.
"""
TEST_PRINT_TEXT = """
    VAR
        a : INTEGER
    BEGIN
        a := 10+11;
        WRITELN(a)
    END.
"""
TEST_MANAGEMENT_STATEMENT_TEXT = """
    VAR
        a : INTEGER
    BEGIN
        a := 10+11;
        CASE a OF
            101: a := a+1;
            1010: a := a+10
        END
    END.
"""
TEST_OPERATIONS_DATA = {
    """
        VAR
            a : INTEGER
        BEGIN
            a := 10+11;
        END.
    """: {'a': BinaryDigit.from_decimal(5)},
    """
        VAR
            a : INTEGER
        BEGIN
            a := 10-11;
        END.
    """: {'a': BinaryDigit.from_decimal(-1)},
    """
        VAR
            a : INTEGER
        BEGIN
            a := 10*11;
        END.
    """: {'a': BinaryDigit.from_decimal(6)},
    """
        VAR
            a : INTEGER
        BEGIN
            a := 1000/10;
        END.
    """: {'a': BinaryDigit.from_decimal(4)},
    """
        VAR
            a : INTEGER
        BEGIN
            a := 00010101 OR 00011001;
        END.
    """: {'a': BinaryDigit('00011101')},
    """
        VAR
            a : INTEGER
        BEGIN
            a := 00010101 AND 00011001;
        END.
    """: {'a': BinaryDigit('00010001')},
    """
        VAR
            a : INTEGER
        BEGIN
            a := 100 SHL 10;
        END.
    """: {'a': BinaryDigit.from_decimal(16)},
    """
        VAR
            a : INTEGER
        BEGIN
            a := 100 SHR 10;
        END.
    """: {'a': BinaryDigit.from_decimal(1)}
}
TEST_OPTIMIZE_DATA = {
    """
        VAR
            abc : INTEGER;
            john: INTEGER;
            value: INTEGER
        BEGIN
            abc := 10+11;
            john := 11101101 + 1111110;
            value := 10
        END.
    """
    :
    """
        VAR
            abc : INTEGER;
            john: INTEGER;
            value: INTEGER
        BEGIN
            abc := 101;
            john := 101101011;
            value := 10
        END.
    """,
    """
        VAR
            a : INTEGER
        BEGIN
            a := 10+11;
            CASE a OF
                101: a := 1+1;
                1010: a := a+10
            END
        END.
    """:
    """
        VAR
            a : INTEGER
        BEGIN
            a := 101;
            CASE a OF
                101: a := 10;
                1010: a := a+10
            END
        END.
    """
}
TEST_ERRORS_DATA = {
    """VAR
            a : INTEGER;
            b : CHAR
        BEGN
            a := 10+11;
        END.
    """: 'Ошибка в строке 4: неверный синтаксис',
    """
        VAR
            a : INTEGER;
            b : CHAR
        BEGIN
            a := 10+13;
        END.
    """: 'Ошибка в строке 6: неверный символ'
}
