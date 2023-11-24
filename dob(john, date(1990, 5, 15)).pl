dob(john, date(1990, 5, 15)).
dob(susan, date(1985, 10, 28)).
dob(mike, date(1993, 3, 9)).
dob(lisa, date(1988, 7, 4)).
exists(Person) :- dob(Person, _).
age(Person, Age) :-
    dob(Person, date(YearOfBirth, MonthOfBirth, DayOfBirth)),
    date(YearToday, MonthToday, DayToday),
    Age is YearToday - YearOfBirth - (
        (MonthToday, DayToday) @< (MonthOfBirth, DayOfBirth)
    ).
date(2023, 11, 22).