% Define initial state
at(monkey, floor).
at(box, room_center).
at(banana, ceiling).

% Define actions
% Monkey can move from one place to another
action(move(From, To), [at(monkey, From), at(Object, From)], [at(monkey, To), at(Object, To)]) :-
    valid_move(From, To),
    \+ blocked(Object, To).

% Define valid moves
valid_move(floor, room_center).
valid_move(room_center, floor).
valid_move(room_center, ceiling).
valid_move(ceiling, room_center).

% Define blocked situations
blocked(box, ceiling).

% Define the goal state
goal_state([at(monkey, floor), at(banana, floor)]).

% Solve the problem using depth-first search with path accumulation
solve(State, State, _, []) :- goal_state(State).
solve(State, Goal, Visited, [Action|Actions]) :-
    action(Action, State, NextState),
    \+ member(NextState, Visited),
    solve(NextState, Goal, [NextState|Visited], Actions).

% Execute the solve predicate to find a sequence of actions to reach the goal state
% This query will output the sequence of actions to reach the banana
?- solve([at(monkey, floor), at(box, room_center), at(banana, ceiling)], GoalState, [at(monkey, floor), at(box, room_center), at(banana, ceiling)], Actions), write(Actions).