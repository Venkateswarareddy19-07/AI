% Diet suggestions based on diseases

% Facts defining diseases and their associated diet suggestions
disease(diabetes, ['Avoid sugary foods.', 'Limit carbohydrates intake.', 'Consume more vegetables and lean protein.']). 
disease(hypertension, ['Reduce sodium intake.', 'Eat more fruits and vegetables.', 'Limit alcohol and caffeine consumption.']). 
disease(high_cholesterol, ['Consume foods rich in omega-3 fatty acids.', 'Reduce saturated fats intake.', 'Eat more soluble fiber.']). 
disease(celiac_disease, ['Avoid gluten-containing grains (wheat, barley, rye).', 'Consume gluten-free alternatives like quinoa, rice, and corn.']). 

% Predicate to suggest a diet based on a given disease
suggest_diet(Disease) :-
    disease(Disease, Suggestions),
    write('Diet suggestions for '), write(Disease), write(':'), nl,
    print_suggestions(Suggestions).

% Helper predicate to print suggestions
print_suggestions([]).
print_suggestions([Suggestion|Rest]) :-
    write('- '), write(Suggestion), nl,
    print_suggestions(Rest).