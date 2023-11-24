% Facts about birds and their ability to fly
bird(canary).
bird(sparrow).
bird(ostrich).
bird(penguin).

can_fly(canary).
can_fly(sparrow).
cannot_fly(ostrich).
cannot_fly(penguin).

% Queries to check if a particular bird can fly or not
% Example queries:
% To check if a canary can fly:
% ?- can_fly(canary).
% This will return true.

% To check if an ostrich can fly:
% ?- can_fly(ostrich).
% This will return false.

% To check if a penguin cannot fly:
% ?- cannot_fly(penguin).
% This will return true.

% To check if a sparrow cannot fly (this will return false as sparrow can fly):
% ?- cannot_fly(sparrow).
% This will return false.