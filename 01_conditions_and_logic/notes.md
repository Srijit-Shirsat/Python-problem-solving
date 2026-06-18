## Assignment 01 - Smart Access Control System

### Concepts Practiced

- if / elif / else
- Comparison operators
- Validation chains
- Priority-based conditions

### Key Learning

When multiple validations exist, conditions should be checked in a predefined order. The first failed validation determines the final outcome.

### Interview Insight

Use `if-elif-else` when only one result should be produced. This avoids unnecessary checks and mirrors real-world business validation systems.

--------------------------------------------------------------------------------------------------------------------------------------------------

## Assignment 02 - Movie Ticket Eligibility System

### Concepts Practiced

* Logical operators (and, or)
* Compound conditions
* Input validation
* Decision trees

### Key Learning

Many businesses and industries often require prioritizing conditions and that could be multiple conditions check. Multiple conditions must be valid to pass the checks and criteria.

### Interview Insight

When checking for eligibilities , a common practice is to validate the input first and then validate the eligibility.
This is known as Condition Prioritizing.

--------------------------------------------------------------------------------------------------------------------------------------------------

## Assignment 03 - Employee Performance Rating System

### Concepts Practiced

* Range validation
* Multi-level classification
* Logical operators
* Ordered condition checks

### Key Learning

When multiple categories exist, conditions must be arranged carefully to avoid other ranges catching values before specific ranges are checked.
Ex. 90 score = Outstanding 
but "if score > 0 or score < 50" condition check comes first. Score=90 passes the first condition & prints ("Poor") even for "Outstanding" score
Therefore, Ordered condition checks are important.

### Interview Insight

Many classification problems fail because conditions are checked in the wrong order. Always think about which conditions are most specific and which are more general.

