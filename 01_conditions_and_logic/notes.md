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

--------------------------------------------------------------------------------------------------------------------------------------------------

## Assignment 04 - Secure Company Login

### Concepts Practiced

* Nested conditions
* Validation hierarchy
* Authentication logic
* Dependent checks

### Key Learning

Nested conditions are useful when one validation should only occur after a previous validation succeeds. If previous validation fails then there's no point in checking further conditions as result would be same.

### Interview Insight

Authentication systems often follow a chain of dependent validations. Avoid checking later conditions when earlier validations have already failed.

### Mistake & Learning Takeaway

My first implementation of this code checked password and account status after the username validation failed (I did not consider using else block for "if password != "python123"). 
This taught me that nested conditions should be placed inside the success path of the previous validation, not inside the failure path and this is possible by using else which works on opposite terms of if condition.

--------------------------------------------------------------------------------------------------------------------------------------------------

## Assignment 05 - Scholarship Eligibility System

### Concepts Practiced

* Independent conditions
* Logical AND operator
* Input validation
* Eligibility checking

### Key Learning

Not all problems require nested conditions. When multiple conditions are independent and must all be satisfied, they can often be combined using logical operators.

### Interview Insight

In industries we must not always use nested conditions. First determine whether conditions are dependent or independent before choosing a solution structure.

--------------------------------------------------------------------------------------------------------------------------------------------------

## Assignment 06 - Electricity Bill Calculator

### Concepts Practiced

* Conditional ranges
* Multi-branch decision making
* Bill calculation
* Input validation

### Key Learning

When multiple conditions can match the same value, the order of conditions becomes critical. More specific conditions should usually be checked before broader conditions.

### Interview Insight

When designing classification systems, always ask whether conditions overlap. If they do, condition order must be carefully planned.

--------------------------------------------------------------------------------------------------------------------------------------------------

## Assignment 07 - Employee Bonus Eligibility System

### Concepts Practiced

* Combination-based decisions
* Logical AND operator
* Multi-level eligibility checking
* Validation handling

### Key Learning

- Multiple Boolean conditions combine to produce different outcomes, and the order of those outcomes matters when conditions overlap.
- Some outcomes depend on multiple conditions being true at the same time. Combining conditions correctly is essential for implementing business rules.

### Interview Insight

When multiple categories exist, check the most specific and highest-priority outcomes first. Otherwise broader conditions may capture values that belong to higher categories.
IN this assignment highest category was (GOLD BONUS) and lowest was (BRONZE BONUS).





