sum_integers(1, 1).
sum_integers(N, Sum) :-
    N > 1,            % Ensure N is greater than 1
    N1 is N - 1,      % Calculate N-1
    sum_integers(N1, SumNMinus1),  % Calculate sum from 1 to N-1
    Sum is SumNMinus1 + N.  % Calculate sum from 1 to N