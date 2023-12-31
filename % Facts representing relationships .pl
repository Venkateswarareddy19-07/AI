% Facts representing relationships between students, teachers, subjects, and codes
teaches(john_doe, mathematics, math101).
teaches(susan_smith, physics, phys102).
teaches(alex_jones, computer_science, cs105).

enrolled(jack, math101).
enrolled(emily, phys102).
enrolled(kate, cs105).
enrolled(peter, math101).
enrolled(lily, cs105).

% Query to find which teacher teaches a specific subject
% Usage: ?- teaches(Teacher, Subject, Code).
% Example: ?- teaches(Teacher, physics, Code).
% This will return the teacher who teaches Physics and the corresponding code.

% Query to find which students are enrolled in a specific subject
% Usage: ?- enrolled(Student, Code).
% Example: ?- enrolled(Student, cs105).
% This will return the students enrolled in Computer Science with the code cs105.
students_enrolled_in_subject(Code, Students) :-
    setof(Student, enrolled(Student, Code), Students).